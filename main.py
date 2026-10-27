from fastapi import FastAPI
from routers import users,services,service_requests


app=FastAPI()
app.include_router(users.router)
app.include_router(services.router)
app.include_router(service_requests.router)


@app.get('/')
def home():
    return {"Service Request Management System"}


