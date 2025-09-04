from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    dir={"Name": "AYUSH RAJPUT",
         "greet":"WELCOME TO THE CLASS"}
    return [dir["Name"] ,dir["greet"]]
