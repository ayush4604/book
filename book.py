from fastapi import FastAPI
from typing import Optional
app=FastAPI()

@app.get("/")
def welcome():
    return{"greet":"this is book section"}

@app.get("/books")
def book_list():
    dic={
        "book1":{"Name":"IOP",
                 "books_id":22},
        "book2":{"Name":"AOP",
                 "books_id":23},
        "book3":{"Name":"IOF",
                 "books_id":24}
    }

    return dic
@app.get("/books/{book_id}")
def books_list(book_id:int,q:Optional[str]=None,limit:int=10):
    dic={
        "book1":{"Name":"IOP",
                 "books_id":22},
        "book2":{"Name":"AOP",
                 "books_id":23},
        "book3":{"Name":"IOF",
                 "books_id":24}
    }
    for book in dic.values():
        if(book["books_id"]==book_id):
            res={"books":book}
            
            if (q):
                res["query"]=q
            res["limit"]=limit
            return res

        
    else:
        return {"Invalid Book Id"}
