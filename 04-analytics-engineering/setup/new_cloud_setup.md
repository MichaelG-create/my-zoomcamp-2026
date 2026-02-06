
## Step 4: Configure the BigQuery Connection (No Test Button Here)

### Choose the BigQuery adapter

1. When prompted to choose a data platform, select **BigQuery** (not “BigQuery (Legacy)”). 
2. Click **Next** to open the BigQuery connection settings. 

### Upload Service Account JSON

1. In the BigQuery connection form, choose **Service account JSON** as the authentication method if prompted. 
2. Click **Upload a Service Account JSON file**. 
3. Select the JSON key file you downloaded earlier. 
4. dbt Cloud will auto‑populate your **Project ID** and service account details. 

### Configure Location and Limits

In the same connection form:

1. **Location / Region**  
   - Set this to the same location as your `nytaxi` dataset (for example, `US` or `EU`). 
2. **Timeout**  
   - Use `300` seconds as a safe default.  
3. **Maximum bytes billed** (optional)  
   - Leave blank for no limit, or set something like `1000000000` (1 GB).  


Click **Save** to finish creating the BigQuery connection.


***

## Step 5: Set Up Your Repository

dbt Cloud needs a Git repository for your project code. You can: 

- Let dbt **manage the repository** (simplest for this course), or  
- Connect your own GitHub repository.

Either option works for Zoomcamp.

***

## Step 6: Create an Environment (Orchestration → Environments)

The environment is where you:

- Attach the BigQuery connection  
- Define the **schema** (dataset prefix)  
- **Test** the BigQuery connection

### 6.1 Go to Orchestration → Environments

1. In the left sidebar, click **Orchestration → Environments**. [docs.getdbt](https://docs.getdbt.com/docs/dbt-cloud-environments)
2. Click **Create new environment**. [docs.getdbt](https://docs.getdbt.com/docs/dbt-cloud-environments)
3. Give it a name, for example: `Development`.

### 6.2 Attach the BigQuery connection

In the environment form:

1. Choose your **Project** (for example, `taxi_rides_ny`). [docs.getdbt](https://docs.getdbt.com/docs/dbt-cloud-environments)
2. Under **Connection / Warehouse**, select the BigQuery connection you created in Step 4. [docs.getdbt](https://docs.getdbt.com/docs/dbt-cloud-environments)

This is the place where a **Test connection** button appears in the new UI.

### 6.3 Set schema (equivalent of “Dataset: dbt_prod”)

Still in the environment form:

1. Find the **Schema** or **Default schema** field.  
2. Set it to: `dbt_prod`.  

This acts as your base dataset name. dbt will then use this together with `schema:` configs to create datasets such as `dbt_prod_staging`, `dbt_prod_intermediate`, `dbt_prod_marts`. [docs.getdbt](https://docs.getdbt.com/reference/resource-configs/bigquery-configs)

Make sure the **Location / Region** matches the location of your `nytaxi` dataset (for example, `US`). [docs.getdbt](https://docs.getdbt.com/docs/core/connect-data-platform/bigquery-setup)

### 6.4 Test the connection (here only)

At the bottom of the environment connection section:

1. Click **Test connection**. [docs.getdbt](https://docs.getdbt.com/docs/dbt-cloud-environments)
2. If the test succeeds, click **Save** to create the environment. [docs.getdbt](https://docs.getdbt.com/docs/dbt-cloud-environments)

If the test fails, check:

- Project ID is correct in the connection.  
- Service account has the required BigQuery permissions. [docs.getdbt](https://docs.getdbt.com/docs/core/connect-data-platform/bigquery-setup)
- Location matches your BigQuery datasets. [docs.getdbt](https://docs.getdbt.com/docs/core/connect-data-platform/bigquery-setup)

***

## Step 7: dbt Schemas for Staging / Intermediate / Marts

To mirror the original tutorial’s idea of separate schemas, you now configure them in `dbt_project.yml` instead of in the connection UI. [docs.getdbt](https://docs.getdbt.com/reference/resource-configs/bigquery-configs)

For example:

```yaml
models:
  taxi_rides_ny:
    +schema: dbt_prod

    staging:
      +schema: dbt_prod_staging

    intermediate:
      +schema: dbt_prod_intermediate

    marts:
      +schema: dbt_prod_marts
```

dbt will create or use BigQuery datasets named `dbt_prod_staging`, `dbt_prod_intermediate`, and `dbt_prod_marts` when you run `dbt run`. [docs.getdbt](https://docs.getdbt.com/reference/resource-configs/bigquery-configs)

***

## Step 8: Initialize the IDE and Run dbt

1. From your project page, click **Start developing** to open the dbt Cloud IDE. [docs.getdbt](https://docs.getdbt.com/guides/bigquery)
2. In the IDE, select the **Development** environment you just created. [docs.getdbt](https://docs.getdbt.com/docs/dbt-cloud-environments)
3. In the command bar, run:
   - `dbt debug` to verify your profile and connection. [docs.getdbt](https://docs.getdbt.com/docs/core/connect-data-platform/bigquery-setup)
   - `dbt run` to build models once they exist.

If `dbt debug` fails, the error will point you to connection or permission problems.

***

## Additional Resources

- dbt + BigQuery quickstart: [docs.getdbt](https://docs.getdbt.com/guides/bigquery)
- dbt Cloud BigQuery connection docs: [docs.getdbt](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-bigquery)
- BigQuery setup / location considerations: [docs.getdbt](https://docs.getdbt.com/docs/core/connect-data-platform/bigquery-setup)
- BigQuery configs in dbt (schema, location, etc.): [docs.getdbt](https://docs.getdbt.com/reference/resource-configs/bigquery-configs)

If you want, you can paste your current `dbt_project.yml` and environment screenshots, and I’ll align all names (`dbt_prod`, `nytaxi`, environment name) for you exactly.