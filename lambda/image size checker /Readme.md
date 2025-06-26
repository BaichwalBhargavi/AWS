Creating a simple Lambda function which the size of the image uploaded in S3 bucket and creates an alert if the size of the image is more than 100 MB.
To achieve this we would be following the below steps.
1. Create a new S3 bucket with name image-size-checker
2. Create a new IAM role which has access to both S3 and Amazon cloudwatch
3. Create a lambda function to check the size of the image and raise an alert if the file is greater than 10 MB -> check image_size_alert.py for the lambda function.
4. Upload various images with varying sizes and check for the logs on cloudwatch

Below is the result when the file exceeds 10 MB


![image](https://github.com/user-attachments/assets/aafa6fde-4d82-4864-982c-b879a78a7912)

