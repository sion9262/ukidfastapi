import json
import traceback

import requests

class Auth:
    def __init__(self):
        self.dataObject = {
            "resultCode": 500,
            "jwt": "",
            "username": "",
            "email": ""
        }
    def login(self, user):

        Data = {
            "identifier": user.email,
            "password": user.password
        }


        try:
            result = requests.post('http://localhost:1337/auth/local', data=Data)

            if (result.status_code == 200) :
                resultData = result.json()

                self.dataObject["resultCode"] = result.status_code
                self.dataObject["jwt"] = resultData["jwt"]
                self.dataObject["username"] = resultData["user"]["username"]
                self.dataObject["email"] = resultData["user"]["email"]

        except:
            print(traceback.format_exc())
            pass

        return self.dataObject

    def register(self, user):
        Data = {
            "email": user.email,
            "password": user.password,
            "username": user.username,
            "phone": user.phone
        }
        try:
            result = requests.post('http://localhost:1337/auth/local/register', data=Data)

            if (result.status_code == 200) :
                resultData = result.json()

                self.dataObject["resultCode"] = result.status_code
                self.dataObject["jwt"] = resultData["jwt"]
                self.dataObject["username"] = resultData["user"]["username"]
                self.dataObject["email"] = resultData["user"]["email"]


        except:
            print(traceback.format_exc())
            pass

        return self.dataObject
