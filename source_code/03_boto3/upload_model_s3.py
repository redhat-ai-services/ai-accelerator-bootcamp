#!/usr/bin/env python
# coding: utf-8

import boto3
from botocore.client import Config

# Configuration
minio_url = "https://minio-api-ai-example-training.apps.cluster-5nrzb.dynamic.redhatworkshops.io"
access_key = "minio"
secret_key = "minio123"
bucket_name = "pipelines"
file_path = "accident_detect.onnx"
object_name = "accident_model/accident_detect.onnx"  # You can change this if you want with a different object name and a folder name

# Setting up the MinIO client
s3 = boto3.client(
    's3',
    endpoint_url=minio_url,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    # config=Config(signature_version='s3v4'),
)

# Function to upload a file to a bucket
def upload_file(file_path, bucket_name, object_name):
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"File '{file_path}' successfully uploaded to bucket '{bucket_name}' as '{object_name}'.")
    except Exception as e:
        print(f"Error uploading file '{file_path}' to bucket '{bucket_name}': {e}")

# Upload the file
upload_file(file_path, bucket_name, object_name)





