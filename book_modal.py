from pydantic import BaseModel,model_validator,EmailStr
class bookadd(BaseModel):
    Name:str
    books_id:int
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


