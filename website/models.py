
from . import dataBase


# Database model for posts/cards that exist

class Post(dataBase.Model):
    Businessid = dataBase.Column(dataBase.Integer, primary_key=True)
    BusinessName = dataBase.Column(dataBase.String(50), unique=True, nullable=False)
    Bio = dataBase.Column(dataBase.String(150), nullable=False)
    Addy = dataBase.Column(dataBase.String(50), nullable=False)
    Photos = dataBase.Column(dataBase.String(50))
    BusinessType = dataBase.Column(dataBase.String(50), nullable=False)