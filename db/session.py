from db.base import setting
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

Base=declarative_base()

engine=create_engine(url=setting.DATABASE_URL)

localsession=sessionmaker(bind=engine)

def getDB():
    session=localsession()
    try:
        yield session
    finally:
        session.close()