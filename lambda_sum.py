def lambda_handler(event, context):
    # TODO implement
    print (event)
    print(context)
    a=event['a']
    b=event['b']
    total =a+b
    return {
        'statusCode': 200,
        'body': json.dumps({'total_sum':total})
    }
