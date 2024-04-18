from flask import Flask ,Blueprint
from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db

models=Blueprint('models',__name__)


class authentication(db.Model,UserMixin):
    __tablename__='authentication'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50), nullable=False)
    password=db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(),nullable=False)
    datetime =db.Column(db.DateTime(timezone=True),server_default=func.now())
