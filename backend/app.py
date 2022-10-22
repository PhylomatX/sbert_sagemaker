import json
from os import environ
import boto3

# Global variables that are reused
sm_runtime_client = boto3.client('sagemaker-runtime')
s3_client = boto3.client('s3')


def get_features(sm_runtime_client, sagemaker_endpoint, payload):
    response = sm_runtime_client.invoke_endpoint(
        EndpointName=sagemaker_endpoint,
        ContentType='text/plain',
        Body=payload)
    response_body = json.loads((response['Body'].read()))
    features = response_body

    return features


def lambda_handler(event, context):

    # sagemaker variables
    sagemaker_endpoint = environ['SM_ENDPOINT']

    api_payload = json.loads(event['body'])
    payload = api_payload['searchString']

    features = get_features(sm_runtime_client, sagemaker_endpoint, payload)
    
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin":  "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*"
        },
        "body": json.dumps({
            "features": features,
        }),
    }
