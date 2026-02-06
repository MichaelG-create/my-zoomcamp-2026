# Project Setup option B - Local

[![](https://markdown-videos-api.jorgenkh.no/youtube/GoFAbJYfvlw)](https://youtu.be/GoFAbJYfvlw)

### Summary

This video provides a comprehensive step-by-step guide to setting up a local environment for working with **dbt (Data Vault Tool)** and **Doc DV**, specifically tailored for users who prefer a completely local, open-source setup without relying on cloud services or accounts. The tutorial is aimed at helping learners follow along with **dbt and StreamD courses** through hands-on installation, initialization, data ingestion, and validation.

### Key Steps and Concepts

- **Local Setup Preference**  
  The tutorial focuses on running everything locally on the user’s computer without cloud dependencies, using open-source tools.

- **Installing Doc DV**  
  - Doc DV is introduced as a **lightweight, fast analytical database engine** ideal for local SQL experiments and prototyping.  
  - Installation can be done via its official website or command line, with the video recommending an explicit install step despite it being a prerequisite.

- **Installing dbt**  
  - The installation command `pip install dbt` installs both **dbt Core (the open-source engine)** and the **Doc DV adapter**.  
  - Users must install adapters corresponding to the warehouses they intend to work with; examples include Snowflake and BigQuery adapters.

- **Initializing a dbt Project**  
  - Running `dbt init` creates a project folder structure with essential directories such as `analysis`, `logs`, `macros`, `models`, `seeds`, `snapshots`, and `tests`.  
  - The project name is customizable, and the initialization process detects installed adapters to configure the project accordingly.  
  - The creation of a hidden `.dbt` folder in the home directory with a `profiles.yaml` file guides dbt on how to run Doc DV with environments like `dev` and `prod`.

- **Customizing the profiles.yaml**  
  - The default profiles are basic, differing mainly in database names and thread counts.  
  - The video’s instructor recommends using a **customized profile** to better handle **large datasets**, incorporating performance optimizations (e.g., memory limits, preserving insertion order, and loading extensions).  
  - Users with limited RAM (less than 8GB) may need to adjust these settings further.

- **Data Ingestion with Python Script**  
  - A provided Python script (`ingest.py`) is used to:  
    - Create a **local data lake** by saving taxi dataset files in Parquet format within a `data` directory.  
    - Modify `.gitignore` to exclude the large data folder from version control to avoid performance issues and security risks.  
    - Initialize a Doc DV database, create a schema, and load data into tables from the Parquet files.  
  - The ingestion process typically takes around 2-3 minutes depending on the machine.

- **Verification of Data Load**  
  - After ingestion, the video demonstrates verifying the presence of data by opening the Doc DV database either through a graphical interface or command line.  
  - Users are cautioned to close database instances after verification to prevent file access conflicts.

- **Running dbt Debug**  
  - Executing `dbt debug` connects to the database using the profile settings and verifies proper connectivity and configuration.  
  - Passing all checks indicates the environment is ready for course work.

- **Recommended Extension for VS Code**  
  - For local setups, the video recommends installing the **“Power User for dbt” VS Code extension** over the official dbt Labs extension because it fully supports dbt Core and Doc DV.  
  - The official extension is more cloud-oriented and may not support local Doc DV usage.  
  - The Power User extension offers useful features but is less intuitive compared to the cloud-based dbt platform.

### Timeline of Major Actions

| Time Range        | Action Description                              |
|-------------------|------------------------------------------------|
| 00:00:01 - 00:01:08 | Introduction to local setup approach and guide |
| 00:01:08 - 00:03:15 | Installing Doc DV and verifying installation   |
| 00:03:15 - 00:05:34 | Installing dbt and initializing project        |
| 00:05:34 - 00:07:31 | Editing profiles.yaml for performance and setup |
| 00:07:31 - 00:11:31 | Running Python script to ingest taxi data locally |
| 00:11:31 - 00:14:11 | Verifying data ingestion in Doc DV              |
| 00:14:11 - 00:15:21 | Running `dbt debug` and recommending VS Code extension |

### Important Notes and Recommendations

- **Profiles.yaml customization** is critical for handling large datasets efficiently in Doc DV.  
- Excluding the `data` directory from Git is essential to maintain manageable repository sizes and prevent long push times.  
- Always close open database instances before running dbt commands to avoid file locks and conflicts.  
- The Power User extension is the preferred VS Code tool for local dbt Core users.

### Key Terms

| Term           | Definition                                                                                     |
|----------------|------------------------------------------------------------------------------------------------|
| Doc DV         | Lightweight analytical database engine optimized for local SQL prototyping and analytics.      |
| dbt Core       | Open-source data transformation engine forming the core of dbt projects.                        |
| Adapter        | Plugin enabling dbt Core to connect to different data warehouses (e.g., Snowflake, BigQuery).   |
| profiles.yaml  | Configuration file specifying environment settings, database connections, and performance tweaks.|
| Local Data Lake| Directory structure storing raw data files (Parquet format) used as input for ingestion.        |
| Power User     | VS Code extension recommended for local dbt Core development supporting Doc DV workflows.       |

### Conclusion

The video thoroughly explains how to set up and verify a fully local dbt environment using Doc DV, emphasizing performance tuning, project structure, and tooling best practices. By following these instructions, users can efficiently develop and test SQL-based data transformations locally before deploying or moving to cloud environments. The guide is practical, beginner-friendly, and grounded in open-source tools, making it ideal for learners focused on data engineering and analytics workflows without cloud dependencies.