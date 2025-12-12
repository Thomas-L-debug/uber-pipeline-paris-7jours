import boto3
from botocore.exceptions import NoCredentialsError

s3 = boto3.client('s3')
bucket_name = 'uber-raw-paris-2025'

try:
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        print(f"Files in bucket: {[obj['Key'] for obj in response['Contents']]}")
    else:
        print("Bucket empty – ingestion not started yet.")
except NoCredentialsError:
    print("AWS credentials not set. Run 'aws configure'.")