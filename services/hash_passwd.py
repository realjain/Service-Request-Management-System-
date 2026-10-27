
from passlib.context import CryptContext
from db.base import setting


class HashService:
    def __init__(self):
        self.pwd_context = CryptContext(
            schemes=["bcrypt_sha256"],
            deprecated="auto"
        )
        

    def hashPasswd(self, password: str) -> str:
        password_concat = password
        return self.pwd_context.hash(password_concat)

    def verifyPasswd(
        self,
        password: str,
        hash_passwd: str
    ) -> bool:
        password_concat = password 
        return self.pwd_context.verify(
            password_concat,
            hash_passwd
        )
