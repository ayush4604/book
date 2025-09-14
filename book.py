from fastapi import APIRouter, Query,Path,HTTPException
from typing import Optional
from book_modal import bookadd
router=APIRouter()

# @router.get("/")
# def welcome():
#     return{"greet":"this is book section"}

book_list=[
        {"Name":"IOP",
                 "books_id":24,
                 "access_code":123,
                 "email_id:":"IOP@fastapi.com"}
        ,
        {"Name":"AOP",
                 "books_id":22,
                "access_code":124,
                "email_id:":"AOP@fastapi.com"}
        ,
        {"Name":"IOF",
                 "books_id":23,
                 "access_code":125,
                 "email_id:":"IOF@fastapi.com"}
        
    ]
@router.get("/books")
def book_lists(q:Optional[str]=Query(None)):
    if q is None:
        return book_list
    good_query=["books_id","access_code","Name"] 
    if q not in good_query:
         raise HTTPException(status_code=400,detail="invalid query")
    try:
        sorted_data = sorted(book_list, key=lambda x: x[q])
    except KeyError:
        raise HTTPException(status_code=400, detail=f"Key '{q}' not found in some books")

    return sorted_data
@router.get("/books/{book_id}")
def books_list(book_id:int=Path(...,gt=20)):
    for book in book_list:
        if(book["books_id"]==book_id):
            res={"books":book}
            return res

    raise HTTPException(status_code=404,detail="Books not found")  
@router.post("/")
def add_book(book:bookadd):
    book_dict=book.dict()

    book_list.append(book_dict)
    return book_list


