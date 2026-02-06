# Introduction to data modeling

[![](https://markdown-videos-api.jorgenkh.no/youtube/uF76d5EmdtU)](https://youtu.be/uF76d5EmdtU&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=40)

## Summary  
This video introduces the concept of **analytics engineering**, a relatively new role bridging the gap between traditional data engineers and data analysts/scientists. It explains how recent developments in cloud data warehousing, ETL/ELT tools, BI platforms, and data governance have reshaped data teams and workflows. Analytics engineering brings software engineering best practices into analytics work, focusing mainly on data transformation and modeling to make data accessible and understandable for business stakeholders. The video also reviews foundational concepts such as ETL vs ELT and Kimball’s dimensional modeling—highlighting the focus on user-friendly, performant data models rather than strict normalization. This content is ideal for data professionals and teams evolving their data practices and roles. Viewers can learn about this emerging role, key tools, and practical modeling approaches crucial for effective data analytics delivery.

## Timeline Summary  
- **00:00–02:17: Introduction to Analytics Engineering & Data Team Gap**  
  Discusses recent advances in cloud warehouses, ETL tools, BI software, and governance that changed data workflows. Highlights how traditional roles (data engineer, analyst, scientist) lack overlap in coding skills and data context, creating a gap filled by the analytics engineer role. Analytics engineers combine software engineering rigor with analytic goals.

- **02:18–03:07: Analytics Engineer Tools and Focus Areas**  
  Outlines the tools an analytics engineer works with, spanning data ingestion, storage, modeling (dbt, dataform), and presentation (Google Data Studio). Emphasizes the focus on data modeling and presentation aspects this week.

- **03:08–04:05: Review of ETL vs ELT Processes**  
  Explains ETL (extract, transform, load) versus ELT (extract, load, transform), noting ELT’s advantage in speed and flexibility due to cloud warehouses letting you load all raw data upfront and transform later.

- **04:06–07:10: Introduction to Kimball Dimensional Modeling & Analogy**  
  Covers dimensional modeling principles prioritizing user understandability and query speed over strict normalization. Explains fact and dimension tables using star schema, with business process “facts” as verbs and dimensions as nouns. Presents the kitchen/restaurant analogy where raw data (ingredients) are processed in the kitchen (data modeling) before final presentation in the dining area (business consumption).

## Key Points  
- 📌 **Analytics engineering fills the skill gap** between data engineers (software-focused) and analysts/scientists (business-focused), introducing reliable software engineering practices to analytics code and workflows.  
- 📌 **Cloud data warehouses and modern ETL/ELT tools have transformed data infrastructure,** enabling cheaper storage, faster querying, and more flexible workflows.  
- 📌 **ETL vs ELT distinction:** ETL transforms data prior to loading, ensuring clean, compliant datasets at the cost of slower implementation; ELT loads raw data first, then transforms it inside the warehouse using compute power, offering speed and flexibility.  
- 📌 **Kimball’s dimensional modeling** prioritizes usability and query performance by organizing data into fact tables (business events/processes) and dimension tables (contextual attributes). This approach may tolerate redundant data for clarity and speed.  
- 📌 **Kitchen analogy** simplifies understanding of data warehousing layers: raw data (ingredients), transformation/modeling as kitchen prep, and final BI presentations as dining hall service.

## Frequently Asked Questions (FAQs)  
1. **What exactly does an analytics engineer do differently from a data engineer or analyst?**  
   Analytics engineers combine software engineering best practices with data analytics efforts, focusing on building reliable, maintainable data models and pipelines that translate raw data into business-friendly formats.

2. **Why is ELT becoming more popular than traditional ETL?**  
   ELT leverages cloud warehouses’ scalable compute and storage, enabling quicker data loading and more flexible, iterative transformations within the warehouse itself, reducing upfront processing time.

3. **What are fact and dimension tables in data modeling?**  
   Fact tables store measurable business events (e.g., sales), while dimension tables provide descriptive context (e.g., customer info), structured to support efficient querying and business understanding.

4. **Can I use standard software engineering tools for analytics engineering?**  
   Yes, many tools such as version control, testing frameworks, and CI/CD pipelines are adopted in analytics engineering to ensure code quality and reproducibility.

5. **Is analytics engineering relevant only for large companies?**  
   While larger data teams may have dedicated roles, any organization aiming to scale and professionalize its analytics efforts can benefit from incorporating analytics engineering practices.

## Conclusion  
The video carefully maps out the evolution of data roles and workflows, highlighting how analytics engineering arises to address gaps between coding expertise and analytic domain knowledge. By embracing software engineering discipline in data transformation and modeling, analytics engineers ensure data is reliable, understandable, and actionable for business stakeholders. Learning ETL/ELT processes and dimensional modeling principles is foundational. The final recommendation is to incorporate analytics engineering practices into data teams to improve collaboration, data quality, and delivery speed. Viewers should consider adopting tools like dbt for data modeling, focus on clear data structures that support business questions, and foster stronger alignment between engineering and analytics functions to maximize data’s value.