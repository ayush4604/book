from fastapi import APIRouter, Query,Path,HTTPException , status
from fastapi.responses import JSONResponse
from typing import Optional
from book_modal import bookadd,update_info
router=APIRouter()

# @router.get("/")
# def welcome():
#     return{"greet":"this is book section"}

book_list=[
        {"Name":"IOP",
                 "book_id":24,
                 "access_code":123,
                 "email_id":"IOP@fastapi.com"}
        ,
        {"Name":"AOP",
                 "book_id":22,
                "access_code":124,
                "email_id":"AOP@fastapi.com"}
        ,
        {"Name":"IOF",
                 "book_id":23,
                 "access_code":125,
                 "email_id":"IOF@fastapi.com"}
        
    ]
@router.get("/books")
def book_lists(q:Optional[str]=Query(None)):
    if q is None:
        return book_list
    good_query=["book_id","access_code","Name"] 
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
        if(book["book_id"]==book_id):
            res={"books":book}
            return res

    raise HTTPException(status_code=404,detail="Books not found")  
@router.post("/create",status_code=status.HTTP_201_CREATED)
def add_book(book:bookadd):
    book_dict=book.model_dump()

    book_list.append(book_dict)
    return {"books":book_list,"message": "book added successfully "}

@router.put("/update/{book_id}")
def update_detail(book_id:int,book_info:update_info):
    new_data=book_info.model_dump(exclude_unset=True)
    for book in book_list:
        if book["book_id"]==book_id:
            for key,value in new_data.items():
                book[key]=value
            return{"books" :book_list, "message":"book updated successfully"}
    raise HTTPException(status_code=404,detail="book not found to update")
    