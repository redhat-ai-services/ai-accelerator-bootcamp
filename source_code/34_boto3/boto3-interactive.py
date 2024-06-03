#!/usr/bin/env python
# coding: utf-8

# Boto3 interactive exploration
import boto3
from botocore.client import Config

# Configuration
minio_url = "https://minio-api-ai-example-training.apps.cluster-5nrzb.dynamic.redhatworkshops.io"
access_key = "minio"
secret_key = "minio123"

# Setting up the MinIO client
s3 = boto3.client(
    's3',
    endpoint_url=minio_url,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    config=Config(signature_version='s3v4'),
)

# Function to get MinIO server info
def get_minio_info():
    # This function retrieves the list of buckets as an example. 
    # MinIO admin info is not directly supported by boto3; you'd need to use MinIO's admin API.
    response = s3.list_buckets()
    print("Buckets:")
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

# Setting alias (not applicable in Boto3, but setup is similar to configuring the client)
print("MinIO client configured successfully.")

# Getting MinIO server info
get_minio_info()



