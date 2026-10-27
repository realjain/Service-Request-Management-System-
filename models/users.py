from db.session import Base
from sqlalchemy import Column,INTEGER,String,Boolean

class Users(Base):
    __tablename__="Users"
    id=Column(INTEGER,primary_key=True,nullable=False)
    name=Column(String(40),nullable=False)
    email=Column(String(60),nullable=False)
    password=Column(String(255),nullable=False)
    phone_no=Column(String(20))
    role=Column(String(20),default="customer",nullable=False)
    is_active=Column(Boolean,default=True,nullable=False)

