"""dlt pipeline to ingest data from the Open Library REST API."""

import dlt
from dlt.sources.rest_api import rest_api_resources
from dlt.sources.rest_api.typing import RESTAPIConfig


@dlt.source
def open_library_rest_api_source():
    """Define dlt resources for the Open Library API.

    Starts with the `books` endpoint and a sample ISBN. Incremental loading is
    intentionally not configured yet.
    """
    config: RESTAPIConfig = {
        "client": {
            # Base URL for the Open Library API
            "base_url": "https://openlibrary.org/",
        },
        "resources": [
            {
                "name": "books",
                # Use the search API to retrieve many books matching a query
                "endpoint": {
                    # Corresponds to https://openlibrary.org/search.json
                    "path": "search.json",
                    # The search response has shape:
                    # { "numFound": ..., "docs": [ { ...book fields... }, ... ] }
                    # so we select the items from the docs array.
                    "data_selector": "$.docs[*]",
                    # Search for books from the Lord of the Rings collection by Tolkien
                    "params": {
                        # "q": "*:*",
                        "author": "Pratchett",
                    },
                },
            }
        ],
    }

    yield from rest_api_resources(config)


pipeline = dlt.pipeline(
    pipeline_name="open_library_pipeline",
    destination="duckdb",
    # show basic progress of resources extracted, normalized files and load-jobs on stdout
    progress="log",
)


if __name__ == "__main__":
    load_info = pipeline.run(open_library_rest_api_source())
    print(load_info)  # noqa: T201
