from google.cloud import bigquery
from google.oauth2.service_account import Credentials

service_account_file = "C:\\Users\\huypv\\Documents\\class-data-analytics-engineer-bigquery-admin.json"
credentials = Credentials.from_service_account_file(service_account_file)
# Construct a BigQuery client object.
client = bigquery.Client(credentials=credentials)

# TODO(developer): Set table_id to the ID of the table to create.
table_id = "class-data-analytics-engineer.sql_practice.employees"

job_config = bigquery.LoadJobConfig(
   source_format=bigquery.SourceFormat.CSV,
   skip_leading_rows=1,
   write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
)
job = client.load_table_from_uri(
   source_uris="gs://data-analytics-engineer/data/employees.csv",
   destination=table_id,
   job_config=job_config
)
job.result()  # Waits for the job to complete