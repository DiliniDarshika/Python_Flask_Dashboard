from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expensesDB.db'
app.config['SECRET_KEY'] = 'hhfghfhijgxhsgtydhxsggjkjibyjibuwokiixa'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

app.app_context().push()

from application import routes

#dd
#pip install flask-sqlalchemy

#python
#from application import app
#from application import db
#db.create_all()
