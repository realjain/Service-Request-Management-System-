from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,HTTPException
from db.session import getDB
from schemas.service_request import ServiceRequestCreate
from models.services import ServiceTable
from models.service_request import serviceRequest
from auth import require_admin,get_current_user
from models.users import Users


router=APIRouter(prefix='/service-request')

@router.post('/')
def create_service_request(serviceReq:ServiceRequestCreate,db:Session=Depends(getDB),current_user:Users=Depends(get_current_user)):
    service=db.query(ServiceTable).filter(ServiceTable.id==serviceReq.service_id).first()
    if not service:
        raise HTTPException(
            status_code=404,
            detail="Service not found or invalid"
        )
    new_req=serviceRequest(
        user_id=current_user.id,
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
def show_services_requests(db:Session=Depends(getDB),admin:Users=Depends(require_admin)):
    service_requests=db.query(serviceRequest).all()
    if not service_requests:
        raise HTTPException(
            status_code=404,
            details="No services is listed"
        )
    return service_requests

@router.get('/my-requests')
def my_service_request(db:Session=Depends(getDB),current_user:Users=Depends(get_current_user)):
    service_requests=db.query(serviceRequest).filter(serviceRequest.user_id==current_user.id, serviceRequest.status != "completed").all()
    return service_requests

@router.get('/my-requests/completed')
def get_completed_requests(
    db: Session = Depends(getDB),
    current_user: Users = Depends(get_current_user)
):
    requests = db.query(serviceRequest).filter(
        serviceRequest.user_id == current_user.id,
        serviceRequest.status == "completed"
    ).all()

    return requests

@router.patch('/{request_id}/status')
def update_request_status(
    request_id: int,
    status: str,
    db: Session = Depends(getDB),
    admin: Users = Depends(require_admin)
):
    allowed_status = [
        "pending",
        "assigned",
        "in progress",
        "completed",
        "cancelled"
    ]

    if status.lower() not in allowed_status:
        raise HTTPException(
            status_code=400,
            detail="Invalid request status"
        )

    request = db.query(serviceRequest).filter(
        serviceRequest.id == request_id
    ).first()

    if not request:
        raise HTTPException(
            status_code=404,
            detail="Service request not found"
        )

    request.status = status.lower()

    db.commit()
    db.refresh(request)

    return {
        "message": "Request status updated successfully",
        "status": request.status
    }