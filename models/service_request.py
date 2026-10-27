from sqlalchemy import Column,Text,Integer,String,ForeignKey
from db.session import Base
from models.users import Users


class serviceRequest(Base):
    __tablename__="service_request_table"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("Users.id"),nullable=False)
    service_id=Column(Integer,ForeignKey("Services_table.id"),nullable=False)
    customer_name=Column(String(100),nullable=False)
    phone_no=Column(String(20),nullable=False)
    location=Column(String(500))
    status=Column(String(30),default="pending",nullable=False)
    description=Column(Text,nullable=False)

