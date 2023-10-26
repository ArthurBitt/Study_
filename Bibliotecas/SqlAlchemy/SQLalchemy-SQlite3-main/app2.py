from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

with app.app_context():

    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///C:\\Users\\arthu\\OneDrive\\Documentos\\Projetos\\SQLalchemy-SQlite3\\space_api.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)


    class users(db.Model)