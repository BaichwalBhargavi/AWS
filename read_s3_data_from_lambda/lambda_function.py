import json
from io import StringIO
import boto3 
import pandas as pd
s3_client = boto3.client('s3')
sns_client = boto3.client('sns')
sns_arn ='arn:aws:sns:eu-north-1:178070228754:first-sns'

def lambda_handler(event, context):
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        print("bucket: ", bucket)
        print("key: ", key)
        response = s3_client.get_object(Bucket=bucket, Key=key)
        file_content = response["Body"].read().decode('utf-8')
        data = StringIO(file_content)
        new_content=pd.read_csv(data)
        print(new_content)

        message = "Input file has been uploaded to S3 bucket"
        sns_client.publish(Subject="SUCCESS - Daily Data Processing",TargetArn=sns_arn, Message=message, MessageStructure='text')

    except Exception as err:
        message = "Input file has not been uploaded to S3 bucket"
        sns_client.publish(Subject="FAILED - Daily Data Processing", TargetArn=sns_arn, Message=message, MessageStructure='text')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
