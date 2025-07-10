📊This project demonstrates how to build a serverless data ingestion pipeline using AWS Lambda to read a CSV file from an S3 bucket and process it using pandas. The CSV data is fetched from S3, converted into a pandas DataFrame, and then logged or further processed inside the Lambda function.

Now enhanced with SNS email notifications when a file is successfully uploaded to S3.

🛠️ Key Skills and AWS Services Used

AWS Lambda Trigger: S3 trigger configured to invoke the Lambda function automatically on file upload.

Lambda Layers: Used to include the pandas library and its dependencies.

IAM Permissions: Lambda execution role configured with the necessary permissions to access the S3 bucket (s3:GetObject).

CloudWatch Logs: Used to monitor function output, errors, and debug logs.

Boto3: AWS SDK for Python used to interact with S3 from within Lambda.

Pandas: For structured data processing and analysis.

Amazon SNS: Sends an email notification when a CSV file is successfully received in the S3 bucket and processed.



![image](https://github.com/user-attachments/assets/f50b0a0b-e074-4319-951c-d702467ba6a4)


