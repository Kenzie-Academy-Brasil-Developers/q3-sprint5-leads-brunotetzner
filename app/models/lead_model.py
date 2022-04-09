from ctypes import BigEndianStructure
from email.policy import default
from sqlalchemy import DateTime, String, Column, Integer
from app.configs.database import db
from dataclasses import dataclass
from  datetime import datetime, timedelta

@dataclass
class Lead(db.Model):
    id :            int
    name :          str
    email :         str
    phone :         str
    creation_date : DateTime
    last_visit :    DateTime
    visit :         int
 
    __tablename__ = "leads"
   
    id =             Column(Integer, primary_key=True)
    name =           Column(String,  nullable=False)
    email =          Column(String, unique=True, nullable=False)
    phone =          Column(String, unique=True, nullable=False)
    creation_date =  Column(DateTime, default = datetime.now())
    last_visit =     Column(DateTime, default =  datetime.now())
    visit =          Column(Integer, default=1)