from pydantic import BaseModel,EmailStr

class ServiceRequestCreate(BaseModel):
    customer_name:str
    phone_no:str | None=None
    service_id:int
    description:str
    location:str | None=None
