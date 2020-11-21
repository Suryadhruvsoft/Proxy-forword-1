from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/flaskdb'

db = SQLAlchemy(app)

from First import routes