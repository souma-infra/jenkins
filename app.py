from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message" : "hello , from the hello route"}

@app.get("/jenkins")
def jenkins():
    return {"message" : "hello , from jenkins"}


@app.get("/")
def read_root():
      return {"message": "Hello, World!"}



