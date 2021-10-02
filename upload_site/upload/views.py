from django.http import HttpResponse, JsonResponse
from django.template import loader
from google.cloud import storage
from django.conf import settings
import os

bucket_name = "cps-630-bucket"

def index(request):
    template = loader.get_template('upload/index.html')
    context = { 'test': 'johnny' }
    return HttpResponse(template.render(context, request))

def upload_file(upload_file, destination_blob_name):
    """Uploads file to bucket"""
    # upload_file is the file to upload
    # destination_blob_name is the id of GCS object

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = settings.GOOGLE_APPLICATION_CREDENTIALS

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_file(upload_file)

    print("File {} uploaded to {}".format(str(upload_file), destination_blob_name))

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
    
def test_post(request):
    print('received a request')
    print(request.FILES)

    upload_file(request.FILES['file'], request.FILES['file'].name)

    template = loader.get_template('upload/success.html')
    context = { 'url': f'https://storage.googleapis.com/cps-630-bucket/{request.FILES["file"].name}' }
    return HttpResponse(template.render(context, request))
