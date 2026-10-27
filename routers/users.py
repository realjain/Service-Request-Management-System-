from fastapi import APIRouter,Depends,HTTPException
from schemas.users import UserCreate,UserLogin
from db.session import getDB
from sqlalchemy.orm import Session
from models.users import Users
from services.hash_passwd import HashService

router=APIRouter(prefix='/users')
hash_service=HashService()

@router.post('/register')
def register(user:UserCreate,db:Session=Depends(getDB)):
    existing_user=db.query(Users).filter(Users.email==user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="User's email is already exist create new one.."
        )
    hash_passwd=hash_service.hashPasswd(user.password)
    
    new_user=Users(
        name=user.name,
        email=user.email,
        phone_no=user.phone_no,
        password=hash_passwd,
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message":"Successfully Registered..."
    }
@router.post('/login')
def login(user:UserLogin,db:Session=Depends(getDB)):
    check_user=db.query(Users).filter(Users.email==user.email).first()
    if not check_user:
        raise HTTPException(
            status_code=401 ,
            detail="Invalid email or password"
        )
    verify_passwd=hash_service.verifyPasswd(user.password,check_user.password)
    if not verify_passwd:
        raise HTTPException(
            status_code=401,
            detail="Invalid password "
        )
    return {
        "message":"Successfully logged in..."
    }


    
    

    



