import json
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def lambda_handler(event, context):

    print("Hello Lambda")
    print("Current time is", current_time)

    return {
        'statusCode': 200,
        'body': json.dumps("Hello from Lambda!") 
    }

# lambda_handler('s3', 'context')