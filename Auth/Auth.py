import json
import requests

class Auth:

    def login(self, user):

        Data = {
            "identifier": user.email,
            "password": user.password
        }


        try:
            result = requests.post('http://localhost:1337/auth/local', data=Data)
            resultCode = result.status_code
            resultData = json.dumps(result.text)

        except:
            resultCode = 500
            resultData = ""

        data = {
            "resultCode" : resultCode,
            "resultData" : resultData
        }

        return data

    def register(self, user):
        Data = {
            "email": user.email,
            "password": user.password,
            "username": user.username,
            "phone": user.phone
        }
        try:
            result = requests.post('http://localhost:1337/auth/local/register', data=Data)
            print(result)
            resultCode = result.status_code
            resultData = json.dumps(result.text)

        except:
            resultCode = 500
            resultData = ""


        data = {
            "resultCode": resultCode,
            "resultData": resultData
        }
        return data
