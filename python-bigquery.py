from google.cloud import bigquery
from google.oauth2.service_account import Credentials

service_account_file = "C:\\Users\\huypv\\Documents\\class-data-analytics-engineer-bigquery-admin.json"
credentials = Credentials.from_service_account_file(service_account_file)
bigquery_client = bigquery.Client(credentials=credentials)

employees_sql = f"""
    SELECT * FROM sql_practice.employees LIMIT 10
"""

query_job = bigquery_client.query(employees_sql)

results = query_job.result()
for row in results:
    print(f"{row.emp_no} - {row.first_name} - {row.last_name}")