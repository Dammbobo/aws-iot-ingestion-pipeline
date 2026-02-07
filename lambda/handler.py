import json

def lambda_handler(event, context):
    """
    Demonstrates processing shop-floor or IoT data
    uploaded to Amazon S3.
    """

    print("Received event:", json.dumps(event))

    return {
        "statusCode": 200,
        "body": "Data processed successfully"
    }
