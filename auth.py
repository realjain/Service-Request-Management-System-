from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from db.session import getDB
from models.users import Users
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from jose import JWTError,jwt
from db.base import setting

bearer_schema=HTTPBearer()

def get_current_user(
        credentials:HTTPAuthorizationCredentials=Depends(bearer_schema),
        db:Session=Depends(getDB)
):
        token=credentials.credentials
        try:
                payload=jwt.decode(
                        token,
                        setting.SECRET_KEY,
                        algorithms="HS256"
                )
                user_id=payload.get("sub")
                if not user_id:
                        raise HTTPException(
                                status_code=401,
                                detail="Invalid token "
                        )
                user_id=int(user_id)

        except:
                raise HTTPException(
                        status_code=401,
                        detail="invalid user"
                )
        current_user=db.query(Users).filter(Users.id==user_id).first()

        if not current_user:
                raise HTTPException(
                        status_code=401,
                        detail="No user found or invalid user"
                )
        return current_user

def require_admin(current_user:Users=Depends(get_current_user)):
        if current_user.role!="admin":
                raise HTTPException(
                        status_code=403,
                        detail="admin permisson are not there"
                )
        return current_user
