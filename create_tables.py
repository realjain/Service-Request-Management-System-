from db.session import Base, engine

from models.users import Users
from models.services import ServiceTable
from models.service_request import serviceRequest
Base.metadata.create_all(bind=engine)