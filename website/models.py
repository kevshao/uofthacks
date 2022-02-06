from ast import BinOp
from email.headerregistry import Address
from . import dataBase
from flask_login import UserMixin

# Database model for posts/cards that exist

class Post(dataBase.Model, UserMixin):
    Businessid = dataBase.Column(dataBase.Integer, primary_key=True)
    BusinessName = dataBase.Column(dataBase.String(50), unique=True)
    Bio = dataBase.Column(dataBase.String(150))
    Addy = dataBase.Column(dataBase.String(50))
    # Photos = 
    BusinessType = dataBase.Column(dataBase.String(50))