# https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/
import os
import pytest

from app import create_app #,db
from db import db

from authlogin.models.user import User

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
 
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()
 
    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()
    
    yield testing_client  # this is where the testing happens!

    user1 = User(name="Mike", email="msdc@gmail.com", password="1234")
    db.session.add(user1)
 
    # Commit the changes for the users
    db.session.commit()

    ctx.pop()
    # TODO this removes the db files - is it in the right place?!  Why doesn't drop work? Because it's a file??
    # TODO it looks like the DB is deleted after each test fixture is run, not after each test - is that correct?
    os.remove("./src/data.db")


# # I don't think I need this function?  My DB is created in the app.py
# @pytest.fixture(scope='module')
# def init_database():
#     # Create the database and the database table
#     db.create_all()
 
#     # TODO this doesn't work? It needs to go above? Why?
#     # Insert user data
#     user1 = User(name="Mike", email="msdc@gmail.com", password="1234")
#     db.session.add(user1)
 
#     # Commit the changes for the users
#     db.session.commit()
 
#     yield db  # this is where the testing happens!


#     # TODO this doesn't work?!
#     # db.session.close()
#     # db.drop_all()


