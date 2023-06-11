import json

def get(event, context):
    body = {
        "message": "TODO GET USER",
        "input": event
    }

    user = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return user

def create(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    createUser = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return createUser