# PhoneBook App

## Setup App
1. Clone repository
```
git clone https://github.com/Fahras23/PhoneBook_RestApi.git
cd PhoneBook_RestApi
```
2. Create virtual enviroment
```
pip install virtualenv
virtualenv venv
```
3. Activate virtual enviroment
For linux:
```
source venv/bin/activate
```
For windows:
```
venv/Scripts/activate
```
4. Add .env file to home directory that contains database url
```
DB_URL = *****
```
5. Install requirements
```
pip install -r requirements.txt
```
6. Start uvicorn server
```
uvicorn main:app --reload
```
7. All method available in api are in URL after starting server
[API](http://127.0.0.1:8000/)
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

