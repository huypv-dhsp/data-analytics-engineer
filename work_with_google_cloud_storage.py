# Imports the Google Cloud client library
from google.cloud import storage
from google.oauth2.service_account import Credentials

service_account_file = "C:\\Users\\huypv\\Documents\\class-data-analytics-engineer-bigquery-admin.json"
credentials = Credentials.from_service_account_file(service_account_file)
# Instantiates a client
storage_client = storage.Client(credentials=credentials)
# The name for the new bucket
bucket_name = "data-analytics-engineer"
# Creates the new bucket
bucket = storage_client.bucket(bucket_name)
if not bucket.exists():
    bucket = storage_client.create_bucket(bucket_name)
    print(f"Bucket {bucket.name} created.")

#
# # The name of bucket
# bucket_name = "data-analytics-engineer"
# bucket = storage_client.bucket(bucket_name)
#
# file_name = "./employees.csv"  # path of local file
# upload_filename = "data/employees.csv"  # the name of blob
# blob = bucket.blob(upload_filename)
# blob.upload_from_filename(file_name)
#
# print(f"File {blob.name} is uploaded.")
