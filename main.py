from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
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
@app.get("/root")
def root():
    return {
        "Hello world"
    }
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

if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port="8000", log_level='info', access_log=False)
