from fastapi import APIRouter
from app.schemas.email import CreateEmail,UpdateEmail,EmailResponse
from sqlalchemy.orm import Session
from app.models.email import Email
from app.database import get_db
from fastapi import Depends
router = APIRouter()


@router.post("/emails",response_model=EmailResponse)
async def create_email(email: CreateEmail,db: Session = Depends(get_db),):
    
    new_email = Email(
        sender=email.sender,
        receiver=email.receiver,
        subject=email.subject,
        body=email.body,
    )

    db.add(new_email)

    db.commit()

    db.refresh(new_email)


    return {
        "message": "Email created successfully",
        "id": new_email.id,
    }
  
      
    

@router.get("/emails", response_model=list[EmailResponse])
async def fetch_email(db: Session = Depends(get_db),):
    emails=db.query(Email).all()
    return emails
    
    
@router.get("/emails/{id}",response_model=EmailResponse)
async def get_email_byid(id:int,db: Session = Depends(get_db),):
    email= db.query(Email).filter(Email.id == id).first()


    if email is None:
        return {"message": "Email not found"}

    return email
     
   
     
@router.delete("/emails/{id}")
async def delete_email(id:int,db: Session = Depends(get_db),):
    email= db.query(Email).filter(Email.id==id).first()
    if email is None:
        return{"message":"Email doesnt exist"}
    db.delete(email)
    db.commit()
    return{"message":"Email deleted sucessfully"}
     

    
@router.put("/emails/{id}",response_model=EmailResponse)
async def update_email(id: int, updated_email: UpdateEmail,db: Session = Depends(get_db),):

    email=db.query(Email).filter(Email.id==id).first()
    if email is None:
        return {"message": "Email not found"}
    email.subject=updated_email.subject
    email.body=updated_email.body
    db.commit()

    db.refresh(email)


    return email

