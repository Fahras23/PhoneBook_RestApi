"""
Auth contains all function connected to authentication
- function for password hashing
- authentication function
- register method
"""
from fastapi import HTTPException, Depends, APIRouter
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi_sqlalchemy import db
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext

from schemas import Credintials as SchemaCredintials
from models import Credintials as ModelCredintials

router = APIRouter()
# create basic http authentication
security = HTTPBasic()
# create password hasher
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    """Return hashed password"""
    return pwd_context.hash(password)


def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    """Check if user is in database comparing firstly username and password next"""
    user = (
        db.session.query(ModelCredintials)
        .filter(ModelCredintials.username == credentials.username)
        .first()
    )
    # if user with similar object exist in database return value diffrent from None
    if user is not None:
        # compare hashed password from login and database
        if pwd_context.verify(credentials.password, user.password):
            return True
    raise HTTPException(status_code=401, detail="Invalid username or password")


@router.post("/register/")
async def register_user(user: SchemaCredintials):
    """Add user to database"""
    # checks for variables in credintials
    if len(user.password) < 8:
        HTTPException(
            status_code=400,
            detail="Password is too short. Should has at least 8 characters",
        )
    if len(user.username) < 4:
        HTTPException(
            status_code=400,
            detail="Username is too short. Should has at least 4 characters",
        )

    try:
        db_user = ModelCredintials(
            username=user.username, password=get_password_hash(user.password)
        )
        db.session.add(db_user)
        db.session.commit()
        return db_user
    except IntegrityError:
        # if username is already in database raise error
        raise HTTPException(status_code=400, detail="Username already exists.")
