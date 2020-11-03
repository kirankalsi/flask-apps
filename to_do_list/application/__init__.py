from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1234@35.197.224.61/flask_db"

db = SQLAlchemy(app)

from application import routes
