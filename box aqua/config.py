# config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    AWS_ACCESS_KEY_ID = 'your_aws_access_key_id'
    AWS_SECRET_ACCESS_KEY = 'your_aws_secret_access_key'
    AWS_REGION = 'your_aws_region'
    S3_BUCKET = 'your_s3_bucket_name'
