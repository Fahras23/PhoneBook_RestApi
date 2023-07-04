# PhoneBook App

## Setup App
1. Clone repository
```
git clone
```
2. Add .env file to home directory that contains database url
```
DB_URL = *****
```
3. Install requirements
```
pip install -r requirements.txt
```
4. Start uvicorn server
```
uvicorn main:app --reload
```
5. All method available in api are in URL after starting server
[API DOCS SITE](http://127.0.0.1:8000/docs#/)


## App features
### Main Page
listed all methods available in api

### Contact Item
methods:
- read (for single contact and all contacts)
- add
- update
- delete
- check (used in all methods to validate arguments)

### Authentication features
methods:
- register (new user)
features:
- authenticate existing user
- hashing and unhashing password for safty

Code formated with black and validated with pylint and flake8

