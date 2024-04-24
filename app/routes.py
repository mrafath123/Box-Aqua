# app/routes.py

from flask import render_template, current_app
from app import app
import boto3

@app.route('/')
def index():
    s3 = boto3.client(
        's3',
        aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
        region_name=current_app.config['AWS_REGION']
    )

    # Example: list objects in the S3 bucket
    response = s3.list_objects_v2(Bucket=current_app.config['S3_BUCKET'])

    # Extract object keys from the response
    if 'Contents' in response:
        object_keys = [obj['Key'] for obj in response['Contents']]
    else:
        object_keys = []

    return render_template('index.html', object_keys=object_keys)
