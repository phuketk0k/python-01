import boto3

client = boto3.client('s3')

response = client.delete_bucket(
    Bucket='don-boto3-demo1',
)