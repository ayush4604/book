from pydantic import BaseModel
class bookadd(BaseModel):
    Name:str
    books_id:int
    access_code:int

