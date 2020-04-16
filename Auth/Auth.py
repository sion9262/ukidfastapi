import json
import traceback

import requests

class Auth:

    def login(self, user):

        Data = {
            "identifier": user.email,
            "password": user.password
        }
        dataObject = self.getObject()

        try:
            result = requests.post('http://localhost:1337/auth/local', data=Data)

            if (result.status_code == 200) :
                resultData = result.json()

                dataObject["resultCode"] = result.status_code
                dataObject["jwt"] = resultData["jwt"]
                dataObject["username"] = resultData["user"]["username"]
                dataObject["email"] = resultData["user"]["email"]
                dataObject["setUserInfo"] = resultData["user"]["setUserInfo"]

        except:
            print(traceback.format_exc())
            pass

        return dataObject

    def register(self, user):
        Data = {
            "email": user.email,
            "password": user.password,
            "phone": user.phone
        }

        dataObject = self.getObject()
        try:
            result = requests.post('http://localhost:1337/auth/local/register', data=Data)

            if (result.status_code == 200) :
                resultData = result.json()

                dataObject["resultCode"] = result.status_code
                dataObject["jwt"] = resultData["jwt"]
                dataObject["username"] = resultData["user"]["username"]
                dataObject["email"] = resultData["user"]["email"]
                dataObject["setUserInfo"] = resultData["user"]["setUserInfo"]

        except:
            print(traceback.format_exc())
            pass

        return dataObject

    def getObject(self):
        dataObject = {
            "resultCode": 500,
            "jwt": "",
            "username": "",
            "email": "",
            "setUserInfo" : ""
        }
        return  dataObject