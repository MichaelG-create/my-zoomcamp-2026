# dbt Course

## dbt Sources
[![](https://markdown-videos-api.jorgenkh.no/youtube/7CrrXazV_8k)](https://youtu.be/7CrrXazV_8k)

### Summary:

<details>
  <summary>Summary of the Video Content on DBT Project Structure and Purpose</summary>

This video tutorial provides a detailed walkthrough on **creating and configuring sources in dbt (data build tool)**, focusing on how to tell dbt where the raw data resides for transformation. The instructor uses a local project setup but notes the process is similar for cloud environments like BigQuery.

---

### Key Concepts and Workflow

- **Project Setup and Directory Structure:**
  - Work occurs primarily within the `models` directory.
  - A new subdirectory named `staging` is created following dbt naming conventions.
  - The `staging` folder initially contains no files.

- **Creating the Source YAML File:**
  - A YAML file (commonly named `sources.yml` or variants like `_sources.yml`) is created inside the `staging` directory.
  - The file starts by specifying `version: 2`.
  - Next, the file declares **sources**, which are named arbitrary but meaningful identifiers (e.g., `raw_data`).
  - Each source includes:
    - **Database** name
    - **Schema** name
    - **Tables** list

- **Naming and Matching Source Data:**
  - It is **critical that database, schema, and table names exactly match the actual names in the environment**.
  - For **local setups**, databases and schemas might have names like `taxi_rides_ny` and `prod`.
  - For **BigQuery**, the database corresponds to the **project ID**, the schema to the **dataset**, and tables to the relevant BigQuery tables.
  - Table names can vary (e.g., with suffixes like `_partitioned`).

- **Using the Source in SQL Models:**
  - Instead of hardcoding the full reference to tables (e.g., `database.schema.table`), dbt provides a `source()` function.
  - Syntax: `{{ source('source_name', 'table_name') }}` where `source_name` and `table_name` must match those declared in the YAML file.
  - This method improves maintainability and portability of SQL models.

- **Creating a Staging Model SQL File:**
  - The tutorial demonstrates creating a staging SQL model (e.g., `stg_green_trip_data.sql`) that selects all columns from the source.
  - Naming conventions often prefix staging models with `stg_` to denote their role.
  
- **Data Cleaning and Transformation in Staging:**
  - Staging models should be minimal transformations of the raw data, mainly:
    - Renaming columns to more meaningful or consistent aliases.
    - Casting columns explicitly to desired data types (e.g., integers, floats, timestamps).
    - Ordering columns logically (e.g., IDs first, timestamps next, financial info last).
  - The instructor shares a personal approach to orderly column arrangement and purposeful aliasing.
  
- **Data Type Casting Examples:**
  - Columns like `passenger_count` as integer.
  - `trip_distance` as float.
  - Timestamp columns explicitly cast as timestamp data types.
  - Financial columns cast as numeric.
  
- **Filtering Rows (Exception to Convention):**
  - Although staging models are ideally 1-to-1 copies of source tables (same rows and columns), the instructor filters out rows with null `vendor_id` values due to data quality issues.
  - This is acknowledged as a deviation from best practices for this project context.

---

### Timeline of Key Steps

| Time Range       | Activity                                               | Details                                                           |
|------------------|--------------------------------------------------------|-------------------------------------------------------------------|
| 00:00:01 - 00:02:10 | Creating `staging` directory and YAML source file        | Naming conventions; choosing file name (`sources.yml` arbitrary)   |
| 00:02:12 - 00:06:50 | Defining source in YAML: version, name, database, schema, tables | Emphasis on exact matches; BigQuery specifics explained            |
| 00:07:02 - 00:09:58 | Writing SQL model using `source()` function               | Using `{{ source('raw_data', 'green_trip_data') }}` instead of hardcoded references |
| 00:09:22 - 00:15:58 | Naming staging models and applying column renaming, casting | Naming conventions (`stg_` prefix); detailed column management      |
| 00:16:00 - 00:17:17 | Filtering rows with null vendor ID (exception)            | Data quality rationale for filtering in staging model              |
| 00:17:15 - 00:18:36 | Recap and assignment to create yellow trip data staging model | Reinforces source file setup, staging model creation, and use of `source()` |

---

### Best Practices and Recommendations

- **Source YAML files should be maintained carefully to reflect exact external database metadata.**
- **Use meaningful and consistent naming conventions** for sources and staging models to improve clarity.
- **Staging models should primarily do cosmetic and type transformations**, avoiding heavy logic.
- **Explicitly cast columns** to prevent data type ambiguities downstream.
- Keep staging models as close as possible to source data (1:1 copies), but apply filtering only if justified by data quality concerns.
- Leverage dbt’s `source()` function for referencing raw data tables instead of hardcoding database/schema/table names.
- Organize columns thoughtfully by logical groups, such as identifiers, timestamps, trip details, and financials.

---

### Key Terms

| Term              | Definition                                                                                   |
|-------------------|----------------------------------------------------------------------------------------------|
| **dbt (data build tool)** | A framework for data transformation and modeling using SQL and YAML configuration files.     |
| **Source**        | A reference in dbt to external raw data tables, declared in YAML files specifying location.  |
| **Staging Model** | A dbt model designed to do initial cleaning, renaming, and casting of raw source data.        |
| **`source()` function** | dbt Jinja macro used to reference a source table dynamically without hardcoding full path.    |
| **YAML file**     | A configuration file in dbt defining data sources with metadata like database and table names. |

---

### Conclusion

This tutorial systematically covers the **process of configuring data sources in dbt**, emphasizing the importance of **correct metadata alignment, naming conventions, and minimal staging transformations**. By using the `source()` function, dbt users can write more maintainable SQL models that are environment-agnostic. The tutorial also highlights practical tips such as column aliasing, explicit type casting, and selectively filtering data rows when necessary, while acknowledging deviations from standard best practices due to specific project needs. The user is encouraged to apply these principles by completing a similar staging model for the yellow trip data as practice.

**Overall, the video provides a foundational understanding of how to set up and use sources in dbt efficiently and professionally.**

</details>