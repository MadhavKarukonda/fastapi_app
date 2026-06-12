from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_rout():
    return {"message": "Hello Madhav"}


@app.get("/greet")
def greet():
    return {"message": "Hello Deepa"}


@app.get("/greet/{name}")
def greet_name(name: str, age: Optional[int] = None):
    return {"message": f"Hello {name} and your are {age} yrs old"}