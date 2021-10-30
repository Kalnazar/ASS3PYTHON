# ASS3Python

## Installation
 You jusst need to pip installing in terminal
 
* Flask==2.0.2
* Flask_SQLAlchemy==2.5.1
* PyJWT==1.7.0

## Usage

* Import libraries
* Generate and set SECRET_KEY
* Set SQLALCHEMY_DATABASE_URI as postgreSQL or sqlite

```
>>> from flaskblog import db
>>> from flaskblog.models import Users
>>> db.create_all()
```

## Example 

http://127.0.0.1:5000/protected?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImJpYmEiLCJleHAiOjE2MzU1ODAxMDd9.empDxiz7bgDQmY_L13_PoE6LURkmgc1gb-AJG8su708
