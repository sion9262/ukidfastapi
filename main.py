from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import requests

import Auth.Auth as AuthModel
import Util.Movies as MoviesModel
app = FastAPI()

Auth = AuthModel.Auth()
Movies = MoviesModel.Movies()
class LoginUser(BaseModel):
    email : str
    password : str

class RegisterUser(BaseModel):
    email : str
    password : str
    phone : str

class setUser(BaseModel):
    name: str
    age: int
    language: int
    math: int
    place: int
    physical: int
    music: int
    relationship: int
    personal: int
    nature: int
    token : str
    id : str

class UserMovies(BaseModel):
    user = str
    movieID = str
    movieTitle = str
    movieCategory = str
    playDate = str
    playTime = str

@app.get("/root")
def root():
    return {
        "Hello world"
    }
@app.post("/register")
def register(user:RegisterUser):

    data = Auth.register(user)
    return data

@app.post("/login")
def login(user:LoginUser):
    data = Auth.login(user)
    return data

@app.post("/setupuser")
def setupuser(user:setUser):
    data = Auth.setUser(user)
    return data
@app.get("/movies")
def movies():
    data = Movies.getMovieData()
    return data
@app.get("/movies/{category}")
def movies(category : str):
    data = Movies.getCategoryData(category)
    return data
@app.post("/userPlayMovies")
def userPlayMovies(playMovie:UserMovies):
    data = Movies.postUserMoives(playMovie)
    return data
if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port="3000", log_level='info', access_log=False)
