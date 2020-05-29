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
                dataObject["id"] = resultData["user"]["id"]

        except:
            print(traceback.format_exc())
            pass

        return dataObject

    def register(self, user):
        Data = {
            "email": user.email,
            "password": user.password,
            "phone": user.phone,
            "username" : ""
        }

        dataObject = self.getObject()
        try:
            result = requests.post('http://localhost:1337/auth/local/register', data=Data)
            print(result)
            if (result.status_code == 200) :
                resultData = result.json()

                dataObject["resultCode"] = result.status_code
                dataObject["jwt"] = resultData["jwt"]
                dataObject["username"] = resultData["user"]["username"]
                dataObject["email"] = resultData["user"]["email"]
                dataObject["setUserInfo"] = resultData["user"]["setUserInfo"]
                dataObject["id"] = resultData["user"]["id"]

        except:
            print(traceback.format_exc())
            pass

        return dataObject
    def setUser(self, user):

        Data = {
            "username" : user.name,
            "age" : user.age,
            "language" : user.language,
            "math" : user.math,
            "place" : user.place,
            "physical" : user.physical,
            "music" : user.music,
            "relationship" : user.relationship,
            "personal" : user.personal,
            "nature" : user.nature,
            "setUserInfo" : 1
        }

        dataObject = {
            "resultCode" : 500
        }
        try:
            result = requests.put('http://localhost:1337/users/'+user.id, data=Data)
            dataObject["resultCode"] = result.status_code;


        except:
            pass

        return dataObject;


    def getObject(self):
        dataObject = {
            "resultCode": 500,
            "id" : "",
            "jwt": "",
            "username": "",
            "email": "",
            "setUserInfo" : ""
        }
        return dataObject