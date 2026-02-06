# dbt Course

## dbt Tests
[![](https://markdown-videos-api.jorgenkh.no/youtube/bvZ-rJm7uMU)](https://youtu.be/bvZ-rJm7uMU)

[00:00:01]  
**Summary of Causes for Wrong KPIs and Data Errors**  
- Wrong KPIs or incorrect dashboard information typically arise from two primary causes:  
  1. **Underlying data issues**: The data might be incorrect or misunderstood regarding its content.  
  2. **User errors in SQL or data processing**: Bugs in SQL queries, unintended edge cases, or faulty joins that exclude necessary data.  
- As an analytics or data engineer, **identifying the root cause of errors is critical**, as failure to do so implies accountability for both data and query faults.  
- The goal is to be **proactive in error detection and resolution** to maintain data integrity.

[00:01:03]  
**Introduction to dbt Testing Capabilities**  
- dbt (data build tool) provides a **large suite of potential tests** applicable to SQL models.  
- The video presenter shares a prior presentation highlighting **common and essential dbt test types**.  
- Tests help ensure data quality and correctness throughout the analytics pipeline.  
- The concept of an "iceberg" of tests is introduced, implying many more tests exist beyond the common ones discussed.

[00:01:35]  
**Singular Tests: Simple SQL-Based Checks**  
- Singular tests are basic SQL statements placed in the test directory.  
- They work by returning rows when an error condition is met (i.e., **if the query returns > 0 rows, an error exists**).  
- Example: Monitoring truck data to ensure every truck is accounted for 24 hours daily (sum of minutes = 1440).  
- This test was effective in catching logic errors and data quality issues repeatedly.  
- **Singular tests provide straightforward, high-impact validation** at the row or aggregated level.

[00:02:45]  
**Source Freshness Tests: Checking Data Timeliness**  
- These tests are configured via YAML files with parameters such as `freshness`, `error_after`, and a timestamp field indicating data load time.  
- Running the `dbt source freshness` command verifies if the data is updated as expected.  
- While useful, **source freshness tests are not widely adopted**, although they can be critical in certain scenarios where data latency impacts decisions.  

[00:03:52]  
**Generic Tests: Built-In Referential and Integrity Checks**  
- Generic tests are defined in YAML alongside columns and descriptions.  
- dbt provides four built-in generic tests:  
  | Test Type          | Purpose                                 | Example Usage                                             |  
  |--------------------|-----------------------------------------|----------------------------------------------------------|  
  | Unique             | Ensures column values are unique         | Order IDs must be unique                                  |  
  | Not Null           | Ensures column values are not null       | Customer email must not be null                           |  
  | Accepted Values    | Limits column values to accepted set    | Status must be one of ['pending', 'complete', 'canceled']|  
  | Relationships     | Enforces referential integrity between models | Every order ID should have a matching customer ID       |  
- Users can **create custom generic tests** by writing SQL files using dbt's Jinja templating and placing them in the generic test folder.  
- The speaker shared examples of custom tests for tax codes based on vehicle attributes, emphasizing flexibility for unique organizational needs.  
- The dbt community has developed many test packages with pre-built tests, reducing the need to build from scratch.

[00:05:43]  
**Unit Tests: Input-Output Based Model Validation**  
- Available since dbt version 1.8.8, unit tests are a relatively new feature and not yet widespread.  
- Unit tests use **fixture files** specifying sample input data and expected output.  
- This allows for **defensive testing of complex SQL logic**, such as rolling windows or regular expressions, before encountering real-world data cases.  
- Unit tests help catch potential data quality errors proactively by simulating scenarios.  

[00:06:57]  
**Model Contracts: Enforcing Schema and Data Contracts**  
- Model contracts involve defining constraints and data types within the model configuration in YAML.  
- By adding a `config` block with `contract: enforced: true`, dbt will **fail the build if the model does not meet the specified schema constraints or data types**.  
- This feature supports the concept of **data contracts**: formal agreements between data producers and consumers on schema, freshness, and data quality expectations.  
- Enables negotiation with stakeholders upfront, ensuring the data delivered matches agreed-upon criteria.  
- Model contracts provide a strong guardrail to prevent unexpected schema changes or data issues.

[00:08:03]  
**Additional Notes and Future Considerations**  
- Beyond these tests, there are **automated testing frameworks and CI/CD pipeline integrations** for dbt, which will be covered separately.  
- The examples provided are basic but serve to **illustrate the breadth of testing possibilities within dbt**.  
- In mature data environments, two key priorities are:  
  - Detecting errors promptly.  
  - Understanding root causes to implement fixes efficiently.  
- dbt tests are an essential step toward achieving these goals and improving data reliability.

### Key Insights  
- **Error sources in analytics are primarily data issues or SQL bugs; both require root cause identification.**  
- **dbt offers multiple testing types: singular tests, source freshness, generic tests, unit tests, and model contracts.**  
- **Singular tests catch presence of error conditions via SQL queries returning rows.**  
- **Source freshness tests monitor data update timeliness but are less commonly used.**  
- **Generic tests enforce uniqueness, non-null constraints, accepted values, and referential integrity.**  
- **Custom generic tests allow for tailored data validation aligned with organizational rules.**  
- **Unit tests enable input-output verification of model logic before data anomalies occur.**  
- **Model contracts formalize schema and data expectations, enforcing them at build time.**  
- **Mature data environments depend on proactive, comprehensive testing to maintain trustworthiness.**

### Summary Table of dbt Test Types

| Test Type          | Description                                          | Implementation Method             | Typical Use Case                                      | Adoption Level          |
|--------------------|------------------------------------------------------|---------------------------------|------------------------------------------------------|------------------------|
| Singular Tests     | SQL queries that return error rows if conditions met | SQL files in test directory      | Validating aggregated metrics (e.g., 24-hour truck data) | Common                 |
| Source Freshness Tests | Verifies timeliness of source data                  | YAML config + `dbt source freshness` command | Ensuring data updates within SLA windows             | Niche, less common      |
| Generic Tests      | Predefined tests for uniqueness, nulls, values, relationships | YAML configuration + built-in or custom SQL | Referential integrity, uniqueness, accepted values   | Very common             |
| Unit Tests         | Input-output test using fixtures for complex logic    | Fixture files + model SQL        | Defensive testing of complex SQL transformations      | Newer, growing usage    |
| Model Contracts    | Enforced data contracts at build time                 | YAML config + `contract: enforced` | Schema validation, stakeholder agreements on data    | Emerging feature        |

### Conclusion  
The video thoroughly explores the **various dbt testing methodologies**, emphasizing their importance in maintaining **data quality, accuracy, and trust** in analytics environments. It highlights how dbt empowers data practitioners to implement **robust, proactive testing** at multiple levels—from simple checks to complex unit tests and enforceable contracts—thereby fostering reliable data products and dashboards.