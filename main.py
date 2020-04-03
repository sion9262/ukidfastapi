from fastapi import FastAPI
from pydantic import BaseModel

import requests

app = FastAPI()

class LoginUser(BaseModel):
    email : str
    password : str

class RegisterUser(BaseModel):
    email : str
    password : str
    username : str
    phone : str

@app.post("/register")
def register(user:RegisterUser):
    data = {
        "email" : user.email,
        "password" : user.password,
        "username" : user.username,
        "phone" : user.phonenumber
    }
    result = requests.post('http://localhost:1337/auth/local/register', data=data)
    print(result)
    return {
        "Hello world"
    }

@app.post("/login")
def login(user:LoginUser):

    Data = {
        "identifier" : user.email,
        "password" : user.password
    }

    result = requests.post('http://localhost:1337/auth/local', data=Data)
    print(result)

    return {
        "Login Sucess"
    }
