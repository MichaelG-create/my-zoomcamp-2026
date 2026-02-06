# dbt Course

## Documentation
[![](https://markdown-videos-api.jorgenkh.no/youtube/UqoWyMjcqrA)](https://www.youtube.com/UqoWyMjcqrA)

[00:00:01]  
The video begins with the presenter mentioning recent efforts to **polish and clean up various data models**. The associated code for these models will be made publicly available on the Zoom Camp GitHub repository, enabling viewers to review, reverse engineer, or rebuild the models independently. The main focus of this video is introduced: **documentation in DVT (Data Versioning Tool)**. The presenter highlights that documentation is a key feature of DVT, which was briefly touched on in a previous video, but will now be explored in greater detail.

[00:00:34]  
The presenter elaborates on the importance of documentation beyond just generating sources. One essential feature is the ability to **add descriptions to database tables and columns**. For example, each table can have a description field, which can be basic (e.g., “AI generated”) or more detailed. Importantly, documentation is extendable to the column level, allowing descriptions to be added for individual columns. The presenter hints that **column-level testing** is another feature but will be covered in a future video.

[00:01:10]  
Further customization of documentation is possible by adding **data types, metadata tags, and other annotations**. These metadata tags are user-defined and can be tailored to the needs of a development team or organization. Several examples of metadata tags include:  
- **PII (Personally Identifiable Information)**: flags sensitive data columns  
- **Ownership**: identifies the person or team responsible for a data asset, useful for contact when issues arise  
- **Importance and Formatting**: other customizable tags to indicate priority or specific formatting rules

The presenter demonstrates correcting a typo in a sample value (“vendor ID was lowercase”) to underline the flexibility of editing metadata. Additionally, documentation can accommodate **multi-line descriptions** using YAML syntax, specifically the pipe operator (`|`) followed by proper indentation.

[00:02:26]  
The presenter demonstrates how to write **multi-line descriptions** in YAML, explaining the need for the pipe operator and indentation. This enables richer, more readable documentation. The presenter emphasizes that while this example shows documentation at the source (table) level, **nearly every DVT element can be documented using YAML**—including sources, staging models, marts, macros, and seeds.

[00:03:06]  
The video discusses different organizational approaches to YAML documentation files:  
- A **single schema.yaml** file containing documentation for multiple models (the most common convention)  
- Individual YAML files per model, which some teams prefer to avoid overly large YAML files

For the purpose of the course, the presenter opts for the **common convention of a single schema.yaml** file. When documenting models (not sources), the YAML structure changes slightly: the top-level key becomes `models` instead of `sources`, but the syntax remains largely consistent. The video shows how to add descriptions and columns with metadata for models similarly to sources.

[00:04:18]  
The presenter points out that tests are another component that may be added under columns but postpones detailed coverage of tests to a later video. The emphasis remains on showing that comprehensive documentation is feasible with DVT’s YAML files. The presenter encourages viewers to inspect a fully documented project available on GitHub to see how official documentation standards are applied.

[00:04:50]  
The presenter stresses that **complete documentation ideally involves collaboration with business stakeholders or domain experts**. This collaborative process ensures that every column and model is well understood and accurately described. For the training video, the documentation remains incomplete because the goal is to demonstrate concepts rather than build a fully annotated project.

[00:05:17]  
Next, the presenter introduces two key DVT commands related to documentation:  
- `dvt docs generate`: generates a JSON file representing the entire project’s documentation metadata  
- `dvt docs serve`: (specific to DVT Core) launches a local web server to view the generated documentation via a browser

The output JSON file from `dvt docs generate` contains a machine-readable, consolidated format of the documentation, although it is not easily human-readable in raw form.

[00:05:59]  
The presenter explains that the JSON documentation is primarily intended to be served as a **web-based documentation site**. For users of **DVT Cloud**, generating documentation automatically integrates with the platform, often including a checkbox to automate this step. However, for **DVT Core users**, the process requires manual generation and serving of documentation.

[00:06:39]  
Using `dvt docs serve` opens a **local website (usually at `localhost:8080`)** which displays the project’s documentation. The presenter notes that hosting this documentation for wider team access may require additional infrastructure setup outside of running it locally.

[00:06:59]  
The local documentation website provides several useful features:  
- **Overview of data assets** including database and model metadata  
- Display of **integer types and other technical details**  
- Source code with **references and compiled SQL code** used to build models, which users can copy for inspection or debugging  
- **A lineage graph** visualizing dependencies between sources and models, color-coded (e.g., green for sources), allowing users to analyze the impact of changes downstream

[00:07:50]  
The presenter highlights the **lineage graph as a critical tool** for impact analysis and debugging, enabling users to understand how changes in one model or source affect others. The graph supports filtering by tags or models, making the documentation interactive and practical for developers.

[00:08:24]  
In conclusion, the presenter characterizes DVT’s documentation as **solid, code-centric, and automatically generated**, providing a trustworthy and detailed resource for data engineers and developers. While it may not replace more visual or user-friendly data catalogs designed for non-technical users, it excels in **technical documentation and developer workflows** by exposing detailed metadata, lineage, and SQL code all in one place.

---

### Key Insights and Highlights

- **DVT supports comprehensive documentation through YAML files**, allowing descriptions and metadata at both table and column levels.  
- Metadata tags such as **PII, Ownership, and Importance** are customizable and help organize and manage data assets effectively.  
- **Multi-line descriptions** are supported in YAML using the pipe operator and indentation, enabling richer documentation.  
- Documentation can cover sources, staging models, marts, macros, and seeds, making DVT versatile for all layers of the data stack.  
- Two main commands for documentation management:  
  | Command            | Purpose                                      | Notes                          |
  |--------------------|----------------------------------------------|-------------------------------|
  | `dvt docs generate` | Creates a JSON representation of docs       | Used in both DVT Cloud & Core  |
  | `dvt docs serve`    | Serves documentation via a local web server | Required only for DVT Core     |
- The **documentation website** includes:  
  - Database and model metadata overview  
  - Code and compiled SQL snippets  
  - An **interactive lineage graph** to analyze dependencies and impact  
- Documentation generation and hosting differ between **DVT Cloud** (automated) and **DVT Core** (manual).  
- Collaboration with business stakeholders is **essential for complete, accurate documentation**.  
- DVT documentation is primarily **technical and developer-focused**, not a replacement for user-friendly data catalogs for non-technical audiences.

---

### Summary Table: Documentation Features in DVT

| Feature                     | Description                                                                 | Usage/Example                                             |
|-----------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------|
| Table and Column Descriptions | Add textual descriptions to tables and individual columns                   | `description` field in YAML                               |
| Metadata Tags               | Custom tags like PII, Ownership, Importance to annotate columns              | User-defined, e.g., `pii: true`, `owner: data_team`      |
| Multi-line Descriptions     | Use YAML pipe operator `|` for multi-line detailed descriptions              | ```description: |\n  This is a multi-line description```  |
| Supported Objects           | Sources, staging models, marts, macros, seeds                               | Document all layers of data models                         |
| Documentation Commands      | `dvt docs generate` and `dvt docs serve`                                   | Generate JSON and host docs locally                        |
| Documentation Website       | Web UI showing metadata, SQL code, and lineage graph                        | Localhost:8080 by default                                  |
| Lineage Graph               | Visualizes data dependencies and transformations                            | Helps assess downstream impact of changes                  |
| Collaboration              | Recommended to involve data experts and stakeholders for completeness       | Ensures accurate, business-aligned documentation           |

---

### Core Concepts

- **Documentation as code:** Using YAML files to annotate data models and sources directly in the project repository.  
- **Metadata extensibility:** Teams can define their own metadata tags to suit organizational needs.  
- **Automated documentation generation:** The process is integrated into the DVT workflow, promoting up-to-date documentation.  
- **Developer-centric documentation:** Emphasizes technical details, lineage, and source code visibility to assist data engineers.  

---

This video provides a thorough walkthrough of how DVT facilitates **robust, extensible, and automated documentation**, underscoring its value in maintaining high-quality, transparent data pipelines.