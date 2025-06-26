import json
# not using boto as simple example
def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name'] # gives the bucket name 
    key    = event['Records'][0]['s3']['object']['key'] # gives the filename
    size    = event['Records'][0]['s3']['object']['size'] # gives size of the file

  # printing all the values
    print("this is bucket =",bucket)
    print("This is the key =",key)
    print("This is the size =", size)

  #checking if the file size is greater than 10 MB
    if size > 10485760 :
        print("Image is too large")
        return {
        'statusCode': 413,
        'body': json.dumps('Image size exceeds 10 MB')
    }
    else:
        print("Image is within size limit")
        return {
        'statusCode': 200,
        'body': json.dumps('Image size is within limit')
    }
    # TODO implement
    print(event)
