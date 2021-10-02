from django.http import HttpResponse
from django.template import loader
from google.cloud import storage

bucket_name = "cps-630-bucket"

def index(request):
    template = loader.get_template('upload/index.html')
    context = { 'test': 'johnny' }
    return HttpResponse(template.render(context, request))

def upload_file(source_file_name, destination_blob_name):
    """Uploads file to bucket"""
    # source_file_name is the path to the file to upload
    # destination_blob_name is the id of GCS object

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_form_filename(source_file_name)

    print("File {} uploaded to {}".format(source_file_name, destination_blob_name))

def download_blob(source_blob_name, destination_file_name):
    """Downloads a blob from the bucket"""
    # source_blob_name is the ID of our GCS object
    # destination_file_name is the path to where file is to be downloaded

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)


    blob = bucket.blob(source_blob_name)
    bloc.download_to_filename(destination_file_name)

    print(
        "Download storage object {} from bucket {} to local file {}.".format(
            source_blob_name, bucket_name, destination_file_name
        )
    )
