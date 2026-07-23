from fastapi import APIRouter
from app.schemas.email import CreateEmail,UpdateEmail,EmailResponse
from app.database import connection,cursor

router = APIRouter()


@router.post("/emails")
async def create_email(email: CreateEmail):

    cursor.execute(
        """
        INSERT INTO emails
        (sender, receiver, subject, body)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
        """,
        (
            email.sender,
            email.receiver,
            email.subject,
            email.body,
        ),
    )

    new_id = cursor.fetchone()[0]

    connection.commit()

    return {
        "message": "Email created successfully",
        "id": new_id,
    }
  
      
    

@router.get("/emails", response_model=list[EmailResponse])
async def fetch_email():
    cursor.execute(
        """
        Select * from emails;
        """
     )
    rows = cursor.fetchall()

    emails = []

    for row in rows:
        emails.append(
            {
                "id": row[0],
                "sender": row[1],
                "receiver": row[2],
                "subject": row[3],
                "body": row[4],
            }
        )
    
    return emails
    
    
@router.get("/emails/{id}",response_model=EmailResponse)
async def get_email_byid(id:int):
     cursor.execute(
         """
         select * from emails
         where id=%s;
         """ ,
         (id,)
    )
     row = cursor.fetchone()

     if row is None:
          return {"message": "Email not found"}

     return {
        "id": row[0],
        "sender": row[1],
        "receiver": row[2],
        "subject": row[3],
        "body": row[4],
    }
     
   
     
@router.delete("/emails/{id}")
async def delete_email(id:int):
    cursor.execute(
        """
        delete from emails
        where id=%s;
        """,
        (id,)
          
    )
    
    connection.commit()
   

    if cursor.rowcount == 0:
       return {"message": "Email not found"}

    return {"message": "Email successfully deleted"}

@router.put("/emails/{id}")
async def update_email(id: int, updated_email: UpdateEmail):

    cursor.execute(
        """
        update emails
        SET subject = %s,
          body = %s
         WHERE id = %s
         RETURNING *;
        """,
        (
    updated_email.subject,
    updated_email.body,
    id,
      )
       
    )
    row=cursor.fetchone()
    connection.commit()
    if row is None:
        return{"message":"Email not found"}
    return{
        
        
    "id": row[0],
    "sender": row[1],
    "receiver": row[2],
    "subject": row[3],
    "body": row[4],

        }