from fastapi import FastAPI
from book import router as Books_detail
app = FastAPI()

@app.get("/")
def read_root():
    dir={"Name": "AYUSH RAJPUT",
         "greet":"WELCOME TO THE CLASS"}
    return [dir["Name"] ,dir["greet"]]
app.include_router(Books_detail, tags=["Books details"]) # we can also use pri"efix="/api" to add prefix to path