import json
from io import StringIO
import boto3 
import pandas as pd

def lambda_handler(event, context):
    print("event: ", event)
    print("context: ", context)

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    print("bucket: ", bucket)
    print("key: ", key)

    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=bucket, Key=key)
    file_content = response["Body"].read().decode('utf-8')
    data = StringIO(file_content)
    new_content=pd.read_csv(data)
    print(new_content)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
