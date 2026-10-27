from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,HTTPException
from db.session import getDB
from schemas.service_request import ServiceRequestCreate
from models.services import ServiceTable
from models.service_request import serviceRequest


router=APIRouter(prefix='/service-request')

@router.post('/')
def create_service_request(serviceReq:ServiceRequestCreate,db:Session=Depends(getDB)):
    service=db.query(ServiceTable).filter(ServiceTable.id==serviceReq.service_id).first()
    if not service:
        raise HTTPException(
            status_code=404,
            detail="Service not found or invalid"
        )
    new_req=serviceRequest(
        user_id=1,
        service_id=serviceReq.service_id,
        customer_name=serviceReq.customer_name,
        phone_no=serviceReq.phone_no,
        location=serviceReq.location,
        description=serviceReq.description

    )
    db.add(new_req)
    db.commit()
    db.refresh(new_req)
    return {
        "Service Request is successfully submitted"
    }
@router.get('/')
def show_services_requests(db:Session=Depends(getDB)):
    service_requests=db.query(serviceRequest).all()
    if not service_requests:
        raise HTTPException(
            status_code=404,
            details="No services is listed"
        )
    return service_requests