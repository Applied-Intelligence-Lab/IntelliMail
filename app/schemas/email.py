from pydantic import BaseModel
class CreateEmail(BaseModel):
    sender:str
    receiver:str
    subject:str | None=None
    body:str
    
class EmailResponse(BaseModel):
    id: int
    sender:str
    receiver:str
    subject:str | None=None
    body:str
    

    
class UpdateEmail(BaseModel):
    subject:str | None=None
    body:str
    

   