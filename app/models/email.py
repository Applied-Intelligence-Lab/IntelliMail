from sqlalchemy import Column, Integer, String
from .base import Base
class Email(Base):
    __tablename__ = "emails"
    id=Column(Integer,primary_key=True)
    sender=Column(String,nullable=False)
    receiver=Column(String,nullable=False)
    body=Column(String,nullable=False)
    subject=Column(String)