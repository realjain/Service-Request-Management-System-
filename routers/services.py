from fastapi import APIRouter,Depends,HTTPException
from schemas.services import ServiceCreate
from sqlalchemy.orm import Session
from db.session import getDB
from models.services import ServiceTable


router=APIRouter(prefix="/services")

@router.post('/')
def add_service(service:ServiceCreate,db:Session=Depends(getDB)):
    existing_service=db.query(ServiceTable).filter(ServiceTable.service_name==service.service_name).first()
    if existing_service:
        raise HTTPException(
            status_code=409,
            detail="This service is already exists"
        )
    new_service=ServiceTable(
        service_name=service.service_name,
        description=service.description
    )
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return {
        "message": "Service added successfully",
        "service": {
            "id": new_service.id,
            "service_name": new_service.service_name,
            "description": new_service.description,
            "status": new_service.status
        }
    }

@router.get('/')
def get_services(db:Session=Depends(getDB)):
    services=db.query(ServiceTable).filter(ServiceTable.status==True).all()
    return services

@router.delete('/{service_id}')
def delete_services(service_id:int,db:Session=Depends(getDB)):
    service=db.query(ServiceTable).filter(ServiceTable.id==service_id).first()

    if not service:
        raise HTTPException(
            status_code=404,
            detail="service not exist or not found"
        )
    db.delete(service)
    db.commit()
    return {
        "message": "Service deleted successfully"
    }