from sqlalchemy import Column,Integer,String,Boolean,TEXT
from db.session import Base

class ServiceTable(Base):
    __tablename__="Services_table"
    id=Column(Integer,primary_key=True)
    service_name=Column(String(50),nullable=False)
    description=Column(TEXT)
    status=Column(Boolean,default=True)