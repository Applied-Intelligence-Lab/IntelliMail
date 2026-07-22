from fastapi import APIRouter
from app.schemas.email import CreateEmail,UpdateEmail,EmailResponse

emails=[]

router = APIRouter()

@router.post("/emails")
async def create_email(email: CreateEmail):
      new_email = {
        "id": len(emails) + 1,
        "sender": email.sender,
        "receiver": email.receiver,
        "subject": email.subject,
        "body": email.body,
    }
  
      emails.append(new_email)

      return {
        "message": "Email created successfully",
        "data": new_email,
               }

@router.get("/emails", response_model=list[EmailResponse])
async def fetch_email():
    return emails
    
    
@router.get("/emails/{id}",response_model=EmailResponse)
async def get_email_byid(id:int):
     for email in emails:
         if email["id"]==id:
             return email
     return{
        "message":"Email not found"
             }
     
@router.delete("/emails/{id}")
async def delete_email(id:int):
    for email in emails:
         if email["id"]==id:
          emails.remove(email)
          return{
        "message":"Email sucessfully deleted"
                }

@router.put("/emails/{id}")
async def update_email(id: int, updated_email: UpdateEmail):

    for email in emails:

        if email["id"] == id:

            email["subject"] = updated_email.subject
            email["body"] = updated_email.body

            return email

        return{
           "message": "Email not found"}    