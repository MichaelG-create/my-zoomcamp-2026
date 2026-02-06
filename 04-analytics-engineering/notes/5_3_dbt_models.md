# dbt Course


## dbt Models
[![](https://markdown-videos-api.jorgenkh.no/youtube/JQYz-8sl1aQ)](https://youtu.be/JQYz-8sl1aQ)

[00:00:00]  
The presenter begins by explaining that initial data staging models for both green and yellow taxi trip datasets have been finalized and polished. Up to this point, all work was done independently behind a computer, without external communication. However, moving forward, two significant changes will occur:  
- **Active data exploration** is required to understand the contents and nuances of the datasets.  
- **Understanding the business context** behind the data becomes essential.  

In real organizations, this involves exhaustive querying to identify common data quality issues, understanding the meaning of columns, normal patterns, and trends, and communicating with stakeholders to clarify ambiguous codes and exception triggers. All this knowledge must be encoded into SQL models as part of the analytics engineer’s role.

[00:01:05]  
The presenter outlines the next steps focusing on building **models (denoted as M)** that support business needs. Two key model types are recommended:  
- Models that power **important dashboards or data applications**, especially if these involve manual work or spreadsheet modifications. These should be rigorously coded and version-controlled within the Data Build Tool (DBT) environment.  
- A **dimensional model** suitable for data warehousing, often structured in a Kimball-style star schema.

[00:01:41]  
Using an example, the presenter discusses building a placeholder model for a dashboard dataset named "**monthly revenue per location**". At this stage, a simple `SELECT 1` query is used as a placeholder to ensure the model does not fail before actual SQL is developed. The presenter prefers organizing models in specific subdirectories inside the models folder, such as `dashboarding` or `finance_marts`, to maintain clarity and modularity.

[00:02:27]  
Aside from dashboard models, the presenter emphasizes building a **dimensional model**, which is common in data warehouses. Two main concepts are introduced:  
- **Fact tables:** Contain transactional or event-level data (e.g., one row per trip, sale, or application).  
- **Dimension tables:** Contain attributes about entities (e.g., customers, vendors, locations).  

The presenter encourages scanning the data to identify entities such as vendors, locations, and trips, which will form the basis of dimension and fact tables respectively.

[00:03:45]  
The process of identifying entities is not solely data-driven—it often requires stakeholder input to understand what entities are important and whether these are being tracked. For the current case, the data suggests three key entities:  
- Dimension Vendors  
- Dimension Locations  
- Fact Trips  

The presenter creates placeholders for these tables in the DBT models directory, explaining that fact tables often have a "fact_" prefix and dimension tables a "dim_" prefix following Kimball conventions.

[00:05:00]  
A key advantage of a well-designed dimensional model is **query simplicity and efficiency**:  
- Counting distinct entities like vendors should be as simple as a `COUNT(*)` on the `dim_vendors` table.  
- Counting events such as trips should be a straightforward `COUNT(*)` on the `fact_trips` table.  

This modular design allows focused tables that can be joined as needed for complex queries.

[00:06:15]  
The presenter then begins focusing on the **fact trips table**, which likely requires unioning the green and yellow trip datasets, as users commonly want to see all trips regardless of taxi type. Before doing this, the presenter stresses the importance of understanding the differences between the green and yellow datasets.  

[00:06:48]  
A brief business context is shared about New York City taxi licensing:  
- Originally, only yellow taxis were licensed and operated mainly in the city center (Manhattan).  
- To improve taxi availability in outer boroughs, green taxis were introduced with licenses allowing pickups **only outside the city center**.  

This explains why there are two similar but distinct datasets.

[00:07:58]  
The presenter decides to create an **intermediate model** called `trips_union` rather than union the datasets directly in the fact table, to maintain a clean modeling structure and avoid complexity exposure.  
- The staging models for green and yellow trip data are imported using DBT conventions:  
  - `source()` is used for raw data sources defined in YAML files.  
  - `ref()` is used to reference other DBT models, including staging models.

[00:09:26]  
When attempting to union the green and yellow datasets, an error occurs:  
- A union operation requires **both datasets to have the same number of columns**, but the green dataset has two extra columns not present in the yellow dataset.  

This discrepancy provides insight into deeper data differences.

[00:09:59]  
The two extra columns in the green dataset are:  
- **Trip Type** (values 1 or 2)  
- **E-Hail Fee**

Details on these columns:  
- **Trip Type:** Indicates the method by which the taxi was hailed.  
  - Type 1 = street hail (physically flagging down a taxi)  
  - Type 2 = requested via phone or app  
- The yellow taxis do not have this column because, by regulation, yellow taxis can only be hailed on the street (type 1).  

To harmonize the datasets, the presenter suggests adding a constant column to the yellow dataset with the value "1" for trip type, simulating this missing information.

[00:11:25]  
Regarding the **E-Hail Fee** column:  
- This fee applies only to green taxis requested via an app, which sometimes charges an additional fee.  
- This feature is often inconsistently implemented or missing in the real dataset.  
- Yellow taxis always have zero e-hail fees because they cannot be hailed via app.  

The presenter decides to add a zero-value column for the e-hail fee in the yellow dataset to align schemas.

[00:12:48]  
After addressing column discrepancies, the presenter reruns the DBT models to update the data pipeline and reflect changes. The `dvt run` command is executed, successfully building the intermediate `trips_union` model that combines both green and yellow datasets with schema alignment. This unioned model forms a solid foundation for subsequent fact table construction.

---

### Key Insights

- **Data exploration and business understanding are crucial** steps after initial data staging to ensure data models reflect reality and business needs.  
- **Dimensional modeling (star schema)** is a best practice for analytical data warehouses, separating facts (events) from dimensions (entities).  
- **Unioning datasets with schema differences requires careful harmonization** of columns, often necessitating adding constant or default values to missing fields.  
- **DBT conventions:**  
  - `source()` references raw data sources defined externally.  
  - `ref()` references other DBT models, enabling modular and maintainable pipelines.  
- **Intermediate models** help abstract complex transformations and keep final models clean and understandable.

---

### Glossary

| Term            | Definition                                                                                 |
|-----------------|--------------------------------------------------------------------------------------------|
| Dimensional Model| Data warehouse design pattern using fact and dimension tables to simplify queries.         |
| Fact Table      | Contains event-level or transactional data (e.g., trips, sales).                           |
| Dimension Table | Contains descriptive attributes of entities (e.g., vendors, locations).                   |
| Staging Model   | A one-to-one copy or lightly transformed raw data source, used as a clean starting point.  |
| Intermediate Model| A DBT model used to perform complex transformations or unions before producing final models.|
| Trip Type       | Categorical indicator of how a taxi trip was requested (street hail vs. app/phone order).  |
| E-Hail Fee      | Additional fee charged for app-requested taxi rides, present only in green taxi data.      |

---

### Summary Timeline Table

| Timestamp   | Event/Topic                                                                                     |
|-------------|------------------------------------------------------------------------------------------------|
| 00:00:00    | Finalized staging models; shift to data exploration and business context understanding.         |
| 00:01:05    | Next steps: build dashboard models and dimensional models in DBT.                              |
| 00:02:27    | Introduction to dimensional modeling concepts: fact and dimension tables.                       |
| 00:03:45    | Identification of key entities: vendors, locations, trips.                                     |
| 00:05:00    | Benefits of dimensional modeling for query simplicity.                                         |
| 00:06:15    | Planning to union green and yellow trip datasets for fact trips table.                          |
| 00:06:48    | Business context for green vs yellow taxis in NYC explained.                                   |
| 00:07:58    | Creating intermediate union model in DBT; source vs ref explained.                              |
| 00:09:26    | Union error due to column mismatch between datasets identified.                                |
| 00:09:59    | Explanation of trip type and e-hail fee columns unique to green taxi data.                     |
| 00:11:25    | Handling missing columns in yellow data by adding constants.                                   |
| 00:12:48    | Running DBT models to refresh data and build unioned intermediate model.                       |

---

This summary is strictly based on the provided transcript, capturing all technical explanations, business context, and modeling decisions discussed.