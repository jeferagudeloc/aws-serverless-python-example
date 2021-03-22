import json
import jwt

def login(event, context):
    key = "secret"
    encoded = jwt.encode({"user":"jeferson.agudelo@gmail.com"}, key, algorithm="HS256")
    
    body = {
        "message": "TODO GET USER",
        "jwt": encoded,
        "input": event
    }


            
    response = {
        "statusCode": 302,
        "headers": {
            "Location": "http://localhost:3000/",
            "Content-Type": "text/plain",
            "Set-Cookie": "user_session="+encoded+"; domain=localhost; expires=68120; path=/"
        },
    }

    return response