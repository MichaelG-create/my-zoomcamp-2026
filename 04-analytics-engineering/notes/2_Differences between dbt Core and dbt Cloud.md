# Differences between dbt Core and dbt Cloud

[![](https://markdown-videos-api.jorgenkh.no/youtube/auzcdLRyEIk)](https://www.youtube.com/auzcdLRyEIk)

[00:00:01]  
**Introduction to dbt Core vs. dbt Cloud**  
- The video explains the differences between **dbt Core** and **dbt Cloud**.  
- There is an official webpage listing all features of both products, but additional context is provided here for better understanding.  
- **dbt** originated in **2016** as a fully **open-source**, **command-line tool**, running locally on a user's machine.  
- The code for dbt Core was (and remains) available on GitHub, allowing users to fork and customize it freely.  
- Initially, dbt Core was **100% free to use**.

[00:00:33]  
**The Emergence of dbt Cloud**  
- Two years after launching dbt Core, the company (then called Fishtown Analytics, now dbt Labs) introduced **dbt Cloud**, a **paid SaaS platform**.  
- dbt Cloud is a **cloud-based application** that eliminates the need for users to manage their own infrastructure and architecture.  
- It automates several operational tasks including:  
  - Hosting dbt documentation  
  - Orchestration of jobs  
  - Environment setup  
  - Backups of dbt artifacts (important for CI/CD pipelines like SlimCI)  
- dbt Cloud also introduces **collaboration** and **security features**, appealing to enterprise users.

[00:01:50]  
**Hybrid Usage and Coexistence of Both Products**  
- Around 2022, it was common for organizations to adopt a **hybrid approach**:  
  - Some users used dbt Core (more technical users)  
  - Others used dbt Cloud (less technical users)  
  - Production runs typically executed via dbt Cloud  
- An article from October 2024 explains the intended coexistence strategy for both products.  

[00:02:30]  
**Introduction of dbt Fusion – The New Engine**  
- Shortly after the coexistence article, dbt Labs undertook a **complete rewrite** of the dbt codebase, launching a new engine named **Fusion**.  
- Fusion brings two main improvements:  
  - **Significantly faster compilation** of code  
  - Enhanced **developer experience** by detecting many errors before execution, saving time and money  
- Despite Fusion’s improvements, **dbt Core remains available but Fusion is the future focus**.

[00:03:46]  
**Limitations and Adapter Support of dbt Fusion**  
- Fusion is **not yet fully supported by all database adapters**.  
- Notably, **DOC DV** (likely a typo or shorthand for a specific adapter, *Not specified exactly*) is not supported, which is a significant limitation for some users.  
- Fusion works well with major adapters like:  
  - **Redshift**  
  - **BigQuery**  
  - **Databricks**  
  - **Snowflake**  
- Users with less common adapters may not be able to use Fusion or the newest dbt Cloud versions effectively.

[00:04:26]  
**Licensing and User Experience with Fusion**  
- Fusion envisions a model where **all users have a dbt license**.  
- Users can choose their preferred interface:  
  - **Cloud IDE** via dbt Cloud  
  - **Local development** with VS Code using an official dbt Labs extension  
- The speaker anticipates updating their course to focus fully on Fusion and the VS Code extension in the near future.  

[00:05:03]  
**Current Course Focus and Practical Advice**  
- For now, the course uses **DOC DV and dbt Core** running locally in VS Code.  
- dbt Cloud abstracts much complexity, so users working with dbt Cloud and BigQuery are expected to follow along without major issues.  
- The dbt documentation and courses are highly recommended for those wanting to deepen knowledge of dbt Cloud.  

[00:05:37]  
**Closing Remarks on Learning dbt Core vs. dbt Cloud**  
- The course aims to highlight the **commonalities rather than differences** between dbt Core and dbt Cloud.  
- Many consultants work with both platforms, so understanding the shared concepts is valuable.  
- The core skills learned are applicable regardless of the platform used.

---

### Summary Table: dbt Product Evolution and Features

| Aspect                  | dbt Core                         | dbt Cloud                            | dbt Fusion (New Engine)                 |
|-------------------------|---------------------------------|------------------------------------|---------------------------------------|
| Launch Year             | 2016                            | 2018                               | *After 2024* (exact year *Not specified*)  |
| Nature                  | Open-source CLI tool, local run | Paid SaaS cloud platform            | Rewritten engine with faster compile & dev features |
| Code Availability       | Fully open on GitHub            | Proprietary SaaS                   | Proprietary (part of dbt Cloud)         |
| Infrastructure Needed   | User-managed                   | Managed by dbt Labs                 | Managed, with options for local VS Code |
| Key Features            | Free, customizable             | Hosting, orchestration, backups, collaboration, security | Faster compilation, pre-run error detection |
| Adapter Support         | Wide adapter support           | Wide adapter support                | Limited adapter support, excludes some like DOC DV |
| User Target             | Technical users, developers    | Less technical users, production   | Developers with licenses, cloud or local IDE |
| Future Outlook          | Still supported but legacy     | Evolving towards Fusion integration| Future focus and preferred engine       |

---

### Key Insights

- **dbt Core remains a robust, open-source tool** but is gradually being superseded by Fusion.  
- **dbt Cloud offers significant operational advantages** by managing infrastructure and enabling collaboration/security.  
- The **Fusion engine marks a significant technological advancement** with faster compilation and better developer tooling.  
- **Adapter support is a critical factor** when choosing to adopt Fusion or remaining with dbt Core.  
- The dbt ecosystem encourages a **hybrid usage model** during this transition phase.  
- Learning foundational dbt principles is valuable **regardless of platform choice**.

---

### Keywords and Concepts

- **dbt Core**: Original open-source command-line interface tool.  
- **dbt Cloud**: Managed SaaS platform with enhanced features.  
- **Fusion Engine**: New, faster dbt engine with improved developer experience.  
- **Adapter**: Database connectors that allow dbt to work with various data warehouses.  
- **Orchestration**: Managing and scheduling data pipeline runs.  
- **Collaboration & Security**: Features designed for team environments and enterprise use.  
- **VS Code Extension**: Official plugin enabling local development with dbt Fusion.  
- **SlimCI**: CI/CD approach for managing dbt artifacts and deployments.

---

### FAQ

**Q: Can I still use dbt Core?**  
A: Yes, it is still available and supported, but the future focus is on dbt Fusion.

**Q: What are the main benefits of dbt Cloud?**  
A: It handles infrastructure, orchestration, backups, collaboration, and security, reducing user overhead.

**Q: Is dbt Fusion compatible with all databases?**  
A: No, it currently supports major adapters like Redshift, BigQuery, Snowflake, but not all, e.g., DOC DV.

**Q: Should I learn dbt Core or dbt Cloud?**  
A: Learning the core concepts applies to both, and many professionals work with both platforms.

**Q: Does dbt Fusion require a license?**  
A: Yes, the vision is that all users have a dbt license, whether using cloud or local IDEs.

---

This summary captures the detailed explanation of the evolution, features, and strategic positioning of dbt Core, dbt Cloud, and the new Fusion engine as presented in the video transcript.