from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schemas import Contact as SchemaContact
from models import Contact as ModelContact

import uuid
import os
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DB_URL'])

@app.get("/")
async def root():
    return {"message": "Hello in phone Contact app"}

@app.get("/contact/")
async def read_contact():
    db_contacts = db.session.query(ModelContact).all()
    return db_contacts

@app.post('/contact/',response_model=SchemaContact)
async def add_contact(contact:SchemaContact):
    db_contact = ModelContact(
        first_name = phone_contact.first_name,
        last_name = phone_contact.last_name,
        phone_number = phone_contact.phone_number,
        email = phone_contact.email
        )
    db.session.add(db_contact)
    db.session.commit()
    return db_contact

@app.delete("/contact/{contact_id}}")
async def remove_contact(contact_id:int):
    db_contact = db.session.query(ModelContact).filter(ModelContact.id==contact_id).first()
    if db_contact:
        db.session.delete(db_contact)
        db.session.commit()
    return db_contact

@app.patch("/contact/{contact_id}")
async def update_contact(contact_id:int,contact:SchemaContact):
    db_contact = db.session.query(ModelContact).filter(ModelContact.id==contact_id).first()
    if db_contact:
        db_contact.first_name = contact.first_name
        db_contact.last_name = contact.last_name
        db_contact.phone_number = contact.phone_number
        db_contact.email = contact.email
    db.session.commit()
    db.session.refresh(db_contact)
    return db_contact
    
