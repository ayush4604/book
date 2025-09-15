from pydantic import BaseModel,model_validator,EmailStr,Field
from typing import Annotated,Optional
class bookadd(BaseModel):
    Name:Annotated[str,Field(...,description="Name of the book ")]
    book_id:Annotated[int,Field(...,description="id must be unique ",examples=["129897"])]
    access_code:str
    email_id:EmailStr

    @model_validator(mode="before")
    @classmethod
    def input_validator(cls,value):
        access_code=value.get("access_code")
        email_id=value.get("email_id")
        name=value.get("Name")
        if name:
            value["Name"]= name.upper()
        if access_code is None or email_id is None:
            raise ValueError("Both access_code and email_id is required ")
        if not access_code.startswith("12"):
            raise ValueError("access_code must start with 12")
        if not email_id.endswith("@fastapi.com"):
            raise ValueError("email_id must be valid , ends with @fastapi.com")
        
        return value


class update_info(BaseModel):
    Name:Annotated[Optional[str],Field(default=None,description="Name of the book ")]
    access_code:Annotated[Optional[str],Field(default=None,description="code to access book")]
    email_id:Annotated[Optional[EmailStr],Field(default=None,description="Add @fastapi email_id")]





