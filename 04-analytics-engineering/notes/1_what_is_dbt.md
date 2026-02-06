# What is dbt?
[![](https://markdown-videos-api.jorgenkh.no/youtube/4eCouvVOJUw)](https://www.youtube.com/watch?v=gsKuETFJr54&list=PLaNLNpjZpzwgneiI-Gl8df8GCsPYp_6Bs&index=5)

## Summary  
This video introduces **dbt (data build tool)** as a modern data transformation workflow primarily used by data engineers to manage, develop, and deploy analytical SQL (or Python) code on data warehouses such as BigQuery. It highlights dbt's role in transforming raw, multi-source data into clean, well-modeled datasets that business stakeholders or ML workflows can consume. Emphasizing software engineering best practices integrated within dbt—like version control, modularity, testing, and CI/CD—the video explains how dbt improves data pipeline quality, maintainability, and collaboration. Suitable for data engineers or analysts interested in data modeling and operationalizing analytics, viewers will learn how dbt streamlines data transformation and deployment with two usage modes: the open-source dbt Core and the cloud-based dbt Cloud platform.  

## Timeline Summary  
- **00:00 - 01:15: Introduction to dbt and Use Case Context**  
  Explains dbt as a transformation workflow enabling SQL or Python analytics code to process data from various sources (e.g., backend systems, third-party data like weather). Data is loaded into data warehouses such as BigQuery or Snowflake and transformed for consumption by business users or applications.  
  *Conclusion:* dbt serves as a bridge between raw data and business-ready datasets.  

- **01:15 - 02:55: Key Features and Benefits of dbt**  
  Discusses how dbt incorporates software engineering principles like version control, modularity (DRY - don’t repeat yourself), separate development environments, testing, documentation, and CI/CD deployment to enhance pipeline quality and reliability.  
  *Conclusion:* dbt improves analytics code development through trusted engineering workflows.  

- **02:55 - 03:29: How dbt Works Technically**  
  Shows sample SQL dbt models and explains that dbt abstracts environment complexities, compiles SQL code, and runs it in the data warehouse producing transformed tables or views.  
  *Conclusion:* dbt automates transformation execution and persistence inside the warehouse.  

- **03:29 - 05:15: Two Main Ways to Use dbt: Core and Cloud**  
  Describes dbt Core as an open-source CLI tool you run locally for development and deployment versus dbt Cloud, a SaaS that offers web IDEs, orchestration, logging, hosted documentation, API access, and semantic layers. The video clarifies that dbt Cloud simplifies management and orchestration.  
  *Conclusion:* dbt provides flexible deployment options based on user needs.  

- **05:15 - 06:49: Project Workflow and Tools Setup**  
  Describes the typical project setup with raw trip data already loaded in GCP buckets and BigQuery. Explains enhancing datasets with master tables, using dbt to transform this data, and then building dashboards for data consumption. Mentions that dbt Cloud developer plan is free and encourages viewers to get started.  
  *Conclusion:* Practical overview of workflow from raw data to dashboards using dbt.  

## Key Points  
- ⭐ **dbt integrates SQL transformation with software engineering best practices:** testing, version control, modularity, CI/CD, and separate dev environments.  
- ⭐ **Transforms raw, multi-source data deposited in data warehouses into business-meaningful tables or views automatically.**  
- ⭐ **Offers two usage modes:** open-source CLI (dbt Core) and cloud-based managed service with orchestration and collaboration tools (dbt Cloud).  
- ⭐ **dbt Cloud includes hosted documentation, logging, API for metadata, and semantic layering—streamlining enterprise usage.**  
- ⭐ **Simplifies data engineering workflows enabling better code quality, collaboration, and dataset reliability.**  

## Key Insights  
- dbt brings decades of software engineering practices to data engineering (00:01:49) — highlighting the shift from ad hoc transformations to maintainable analytics codebases.  
- The comparison of raw data ingestion to final dashboard datasets illustrates a clear transformation pipeline with dbt as the orchestrator (00:06:31).  
- The distinction between dbt Core and dbt Cloud clarifies options for teams with varying needs for infrastructure and orchestration (03:46 – 05:07).  
- Use of sandbox environments in dbt encourages parallel development and safe testing before production deployment, akin to software development best practices (01:55).  
- The end-to-end workflow from ingestion to presentation within cloud data warehouses consolidates data engineering, analytics, and BI in one coherent process (06:00+).  

## FAQs  
1. **What is dbt and why use it?**  
   dbt is a data transformation tool that lets you write modular, tested SQL or Python to transform raw data in warehouses, applying software engineering practices to analytics workflows.  

2. **What data warehouses does dbt support?**  
   dbt works with BigQuery, Snowflake, Redshift, Databricks, and others, making it versatile for different cloud environments.  

3. **How do dbt Core and dbt Cloud differ?**  
   dbt Core is a free, open-source CLI tool run locally, while dbt Cloud is a SaaS offering enhanced collaboration, orchestration, hosted docs, logging, and APIs.  

4. **Do I need programming knowledge to use dbt?**  
   Basic SQL skills are essential. Python can also be used, but the core transformation work is typically in SQL. Familiarity with version control (Git) and software development practices helps.  

5. **How does dbt improve data quality and collaboration?**  
   Through testing frameworks, documentation generation, version control, and deployment workflows, dbt ensures transformation logic is reliable, transparent, and easy to maintain across teams.  

## Conclusion  
This video presents dbt as a transformative tool that modernizes the data engineering workflow by combining traditional data modeling with best software engineering practices. By leveraging dbt, teams can produce reliable, high-quality transformed datasets that meet business needs efficiently and with maintainable codebases. The dual approach of dbt Core and dbt Cloud offers flexibility for different organizational setups. As a next step, viewers are encouraged to experiment with dbt Cloud's free developer plan or install dbt Core locally to start integrating these best practices into their data projects. This sets the stage for robust analytics pipelines that are easier to develop, test, and deploy in production environments.