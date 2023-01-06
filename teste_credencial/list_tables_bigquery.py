from google.cloud import bigquery
from google.oauth2 import service_account

# como fazer credenciais
# credentials = service_account.Credentials.from_service_account_file('/path/to/key.json')# path to json credentials
# client = bigquery.Client(credentials=credentials)

client = bigquery.Client() # client with gcloud authentication

project_id = "" #set project_id
dataset_id = "" #set dataset_id

tables = client.list_tables(f"{project_id}.{dataset_id}")

for table in tables:
    print(table)