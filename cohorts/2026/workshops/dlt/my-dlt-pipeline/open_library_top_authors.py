import marimo as mo


app = mo.App()


@app.cell
def _():
    import marimo as mo
    import dlt
    import ibis
    import pandas as pd

    return mo, dlt, ibis, pd


@app.cell
def _(dlt):
    """Connect to the dlt dataset via ibis."""
    pipeline = dlt.pipeline("open_library_pipeline")
    dataset = pipeline.dataset()
    con = dataset.ibis()

    return con


@app.cell
def _(con, ibis):
    """Compute top 10 authors by book count."""
    books = con.table("books")
    author_names = con.table("books__author_name")

    # Join author names to their parent books
    joined = author_names.join(
        books,
        author_names["_dlt_parent_id"] == books["_dlt_id"],
    )

    # Aggregate: count distinct books per author name
    author = author_names["value"].name("author")
    agg = joined.group_by(author).aggregate(
        book_count=books["_dlt_id"].nunique()
    )

    top_authors_expr = agg.order_by(ibis.desc("book_count")).limit(10)

    return top_authors_expr


@app.cell
def _(top_authors_expr):
    top_authors_df = top_authors_expr.execute()

    return top_authors_df


@app.cell
def _(top_authors_df):
    import plotly.express as px

    bar_fig = px.bar(
        top_authors_df,
        x="author",
        y="book_count",
        title="Top 10 authors by book count",
    )
    bar_fig.update_layout(xaxis_title="Author", yaxis_title="Number of books", xaxis_tickangle=-45)

    return bar_fig


@app.cell
def _(mo, top_authors_df, bar_fig):
    """Visualize the top 10 authors by book count."""
    table = mo.ui.table(top_authors_df)
    bar_chart = mo.ui.plotly(bar_fig)

    mo.vstack(
        [
            mo.md("# Top 10 authors by book count"),
            bar_chart,
            table,
        ]
    )


if __name__ == "__main__":
    app.run()

