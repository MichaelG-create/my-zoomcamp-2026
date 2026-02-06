# Project Setup option A - Cloud

[![](https://markdown-videos-api.jorgenkh.no/youtube/GFbwlrt6f54)](https://www.youtube.com/watch?v=GFbwlrt6f54&list=PL12GPe_RDEGRfNWxAMj6ThiU0zO4OiJWT&index=2)

[00:00:01]  
This video provides a **step-by-step walkthrough for setting up a cloud environment** with BigQuery, Google Cloud’s native dashboard tool Looker Studio, and DBT platform (formerly DBT cloud). The speaker emphasizes that all instructions are also available in a written guide within the Git repository’s setup directory. This video serves as a visual aid to complement the written material and is targeted at users who have already ingested the New York taxi dataset into BigQuery (covered in a prior lesson).

Key points:  
- The focus is on setup, not detailed DBT usage.  
- Assumes prior completion of data ingestion (New York taxi data).  
- The video complements, but does not replace, the written guide.

---

[00:01:15]  
The first technical step is to **ensure the BigQuery API is enabled** in your Google Cloud project. This is done by searching for “BigQuery API” in the Google Cloud console and enabling it if not already active.

Next, the video instructs to **create a service account specifically for DBT** rather than using personal credentials. This is a best practice to improve security and manageability in production environments.

Key details about service accounts:  
- Created under “IAM & Admin” → “Service Accounts.”  
- Service accounts are intended for applications, not human users.  
- Naming should be descriptive, e.g., “DBT BigQuery service account.”

---

[00:01:56]  
After creating the service account, it is necessary to **assign appropriate roles/permissions**. While a broad role like “BigQuery Admin” is acceptable for learning, the video stresses best practices for production:

- Principle of least privilege: assign only the minimum required permissions.  
- Recommended roles for DBT service account:  
  1. **BigQuery Data Editor**  
  2. **BigQuery Job User**  
  3. **BigQuery User**

Security rationale: If the service account credentials leak, overly permissive roles could allow malicious users to delete or modify critical data.

---

[00:04:16]  
Once the service account and permissions are configured, the next step is to **generate a private key for authentication**. This key is downloaded as a JSON file containing sensitive credentials, including a private key and key ID.

Important notes:  
- The JSON key file must be kept **private and secure**.  
- The video briefly shows the JSON content but cautions viewers not to share it.  
- This file is essential for authenticating DBT to BigQuery.

---

[00:06:24]  
The video advises verifying that the **New York taxi datasets (“green trip data” and “yellow trip data”) are present in BigQuery**. These datasets serve as the foundation for the course exercises.

Additional notes on datasets:  
- Partitioned versions of the datasets (from homework) are recommended for cost efficiency.  
- For compatibility, the speaker prefers using non-partitioned dataset names by renaming partitioned datasets.

---

[00:07:42]  
The focus shifts to the **DBT platform setup**:

- Visit [getdbt.com](https://getdbt.com) and create a free developer account.  
- Developer accounts are free and allow trial usage of other account types.  
- Upon login, the new user sees an empty DBT platform workspace.

Terminology update:  
- The platform was recently renamed from “DBT cloud” to “DBT platform,” although both terms may be used interchangeably.

---

[00:08:58]  
Within DBT platform:  
- Create a new project (e.g., name it “my taxi”).  
- Set up a **connection to BigQuery**, selecting BigQuery as the data warehouse type.  
- The platform supports uploading the previously downloaded **JSON key file** for authentication, which simplifies connection setup.  
- Avoid the legacy BigQuery adapter; use the new one.  
- Save the connection once validated.

---

[00:10:25]  
Additional recommended setup steps:  
- **Git integration:** Link your GitHub, GitLab, or Azure DevOps account to DBT for version control and collaboration. This step is optional but beneficial.  
- The video also notes that DBT has its own built-in Git repository management for those who do not want to integrate external Git providers.

---

[00:11:01]  
Next, configure **environments within DBT Studio**, which is the main coding interface:  
- At minimum, create one development (dev) environment.  
- Recommended to create both dev and production (prod) environments for better workflow management.  
- Use the BigQuery connection with JSON authentication.  
- Assign a unique name to the environment for clarity, especially in team contexts.  
- Environments correspond to BigQuery datasets in which DBT will create and manage tables, allowing parallel work without conflicts.

---

[00:12:23]  
The environment setup includes:  
- Naming the target environment (e.g., “default”).  
- Optionally specifying number of threads (left empty in demo).  
- Testing the connection to ensure proper setup before proceeding.  
- Saving the environment configuration once tests pass.

---

[00:13:17]  
Regarding **Git repository management within DBT**:  
- The speaker prefers GitHub integration but demonstrates using DBT’s **managed Git repository** for simplicity.  
- Create a new repository (e.g., “taxis_rides_NY”).  
- Names are flexible but can aid continuity when returning to the project or collaborating.  
- Repository creation is quick and integrated into the DBT platform UI.

---

[00:15:06]  
After Git is set up, initialize the **DBT project structure** within the platform:  
- This creates the standard directory layout including folders like:  
  - analysis  
  - macros  
  - models  
  - seeds  
  - tests  
- Example models are included by default.  
- This structure confirms that the project is correctly initialized and ready for development.

---

[00:15:42]  
For advanced development workflows, the video recommends:  
- Using the **DBT CLI (command-line interface)** and a **VS Code extension** for enhanced Git control and local development.  
- However, for beginners or simple setups, the web-based Git tools in DBT platform suffice.

---

[00:16:26]  
Final steps include:  
- Creating a new Git branch (e.g., named after the user).  
- Committing initial project files with a message like “initial commit.”  
- Confirming branch creation and commit success.  
- Once this is done, the user is fully set up and ready to proceed with the course content.

---

### Key Insights and Best Practices

- **Always use dedicated service accounts for applications like DBT** instead of personal credentials, following security best practices.  
- **Grant only necessary permissions** to service accounts following the principle of least privilege to prevent accidental or malicious data loss.  
- **Keep the JSON key file private and secure**; it contains sensitive authentication information.  
- Partitioned datasets are recommended to optimize cost but may require renaming for compatibility.  
- DBT platform supports native BigQuery integration with JSON key authentication and flexible Git management options.  
- Setting up **dev and prod environments** in DBT allows for safer collaboration and testing workflows.  
- The standard DBT project structure is automatically generated, containing essential subdirectories and example models.  
- For advanced usage, combining DBT platform with CLI and VS Code extensions is advisable.  
- The video and written guide together provide a comprehensive resource for cloud-based data transformation workflows using DBT and BigQuery.

---

### Summary Table: Roles Recommended for DBT Service Account

| Role Name            | Purpose                                     | Notes                                   |
|----------------------|---------------------------------------------|-----------------------------------------|
| BigQuery Data Editor | Allows modification of datasets and tables | Least privilege alternative to Admin   |
| BigQuery Job User    | Allows running BigQuery jobs                 | Needed for executing queries and tasks  |
| BigQuery User        | Basic access to BigQuery resources           | Enables general usage capabilities      |

---

### Timeline Table of Setup Steps

| Timestamp  | Step Description                                       |
|------------|--------------------------------------------------------|
| 00:01:15   | Enable BigQuery API                                    |
| 00:01:56   | Create DBT-specific service account                   |
| 00:04:16   | Assign appropriate BigQuery roles to service account  |
| 00:04:57   | Generate and download JSON key for service account    |
| 00:06:24   | Verify presence of New York taxi datasets in BigQuery |
| 00:07:42   | Create free DBT platform account                       |
| 00:08:58   | Create DBT project and BigQuery connection             |
| 00:10:25   | (Optional) Setup Git integration                       |
| 00:11:01   | Configure DBT environments (dev and prod)              |
| 00:13:17   | Set up Git repository (managed or external)            |
| 00:15:06   | Initialize DBT project structure                        |
| 00:15:42   | (Optional) Use CLI and VS Code for advanced Git        |
| 00:16:26   | Commit initial project files and create Git branch     |

---

This summary covers all the **critical setup steps, best practice recommendations, and technical details** presented in the video, providing a comprehensive reference for users preparing their cloud environment with DBT and BigQuery.