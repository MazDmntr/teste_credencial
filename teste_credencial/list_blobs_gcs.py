from google.cloud import storage


gcs_storage = "" #storage name

def list_blobs(bucket_name):

    #google credentials
    #credentials = "path/to/credentials.json"
    #storage_client = storage.Client(credentials=credentials)
    
    storage_client = storage.Client()#for testing autenticated user-gcloud

    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        print(blob.name)


list_blobs(gcs_storage)
