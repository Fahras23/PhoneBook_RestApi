"""Phone Book API"""
import os
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware


from dotenv import load_dotenv

from api import contacts, auth

# import enviromental variables from .env
load_dotenv(".env")

app = FastAPI()
# connect FastApi app to database
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DB_URL"])
# add routing specific api routes containg endpoints
app.include_router(auth.router)
app.include_router(contacts.router)


# main site of phonebook app
@app.get("/")
async def root():
    """
    Welcome site that prints all endpoints in phonebook API
    Contains info about all endpoints
    """
    return {
        "message": "Welcome in phone contact app",
        "get /contact/": "list of contacts",
        "get /contact/[id]": "list specific contact",
        "post /contact/": "add contact to database",
        "delete /contact/[id]": "remove contact from database",
        "patch /contact/[id]": "update contact in database",
        "post /register/": "add user credintials to database",
    }
