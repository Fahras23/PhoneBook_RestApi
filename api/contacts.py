"""Contains all methods for contacts"""
from fastapi import HTTPException, Depends, APIRouter
from fastapi_sqlalchemy import db

from schemas import Contact as SchemaContact
from models import Contact as ModelContact

from api.auth import authenticate

router = APIRouter()


@router.get("/contact/")
async def read_contacts(authenticated: bool = Depends(authenticate)):
    """Return all contacts in database"""
    db_contacts = db.session.query(ModelContact).all()
    return db_contacts


@router.get("/contact/{contact_id}")
async def read_contact(contact_id: int, authenticated: bool = Depends(authenticate)):
    """Return contact with specific id"""
    db_contact = (
        db.session.query(ModelContact).filter(ModelContact.id == contact_id).first()
    )
    # check if contact exist in database
    if db_contact:
        return db_contact
    raise HTTPException(status_code=404, detail="Item not found")


@router.post("/contact/", response_model=SchemaContact)
async def add_contact(
    contact: SchemaContact, authenticated: bool = Depends(authenticate)
):
    """
    Add contact to database
    - phone number must be int with 9 digits
    - email must be contain @
    - first_name and last_name cannot be null
    """
    # checks used to check value of specific parametrs in request
    if len(str(contact.phone_number)) != 9:
        raise HTTPException(
            status_code=400, detail="Phone number must be number with 9 digits"
        )
    if "@" not in contact.email:
        raise HTTPException(status_code=400, detail="Inserted value is not an email")
    if len(contact.first_name) < 0:
        raise HTTPException(status_code=400, detail="first_name cant be null")
    if len(contact.last_name) < 0:
        raise HTTPException(status_code=400, detail="last_name cant be null")
    try:
        db_contact = ModelContact(
            first_name=contact.first_name,
            last_name=contact.last_name,
            phone_number=contact.phone_number,
            email=contact.email,
        )
        db.session.add(db_contact)
        db.session.commit()
        return db_contact
    # raise an error is value in database already exists
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail="Phone_number or email already exists."
        )


@router.delete("/contact/{contact_id}}")
async def remove_contact(contact_id: int, authenticated: bool = Depends(authenticate)):
    """Remove contact with specific id"""
    db_contact = (
        db.session.query(ModelContact).filter(ModelContact.id == contact_id).first()
    )
    # check if contact exist in database
    if db_contact:
        db.session.delete(db_contact)
        db.session.commit()
        return db_contact
    # if contact in database not found raise an error
    raise HTTPException(status_code=404, detail="Item not found")


@router.patch("/contact/{contact_id}")
async def update_contact(
    contact_id: int, contact: SchemaContact, authenticated: bool = Depends(authenticate)
):
    """
    Update contact with specific id
    - phone number must be int with 9 digits
    - email must be contain @
    - first_name and last_name cannot be null
    """
    # checks used to check value of specific arguments in request
    if len(str(contact.phone_number)) != 9:
        raise HTTPException(
            status_code=400, detail="Phone number must be number with 9 digits"
        )
    if "@" not in contact.email:
        raise HTTPException(status_code=400, detail="Inserted value is not an email")
    if len(contact.first_name) < 0:
        raise HTTPException(status_code=400, detail="first_name cant be null")
    if len(contact.last_name) < 0:
        raise HTTPException(status_code=400, detail="last_name cant be null")
    db_contact = (
        db.session.query(ModelContact).filter(ModelContact.id == contact_id).first()
    )
    # overrite existing values in database with that from request
    if db_contact:
        db_contact.first_name = contact.first_name
        db_contact.last_name = contact.last_name
        db_contact.phone_number = contact.phone_number
        db_contact.email = contact.email
    db.session.commit()
    db.session.refresh(db_contact)
    return db_contact
