
from . import dataBase
from flask_login import UserMixin

# Database model for posts/cards that exist

class Cardpost(dataBase.Model, UserMixin):
    __tablename__ = 'cardpost'

    def __init__(self, business_name, business_bio, business_addy, business_photos, business_type):
        self.business_name = business_name
        self.business_bio = business_bio
        self.business_addy = business_addy
        self.business_photos = business_photos
        self.business_type = business_type

    business_id = dataBase.Column(dataBase.Integer, primary_key=True)
    business_name = dataBase.Column(dataBase.String(50), unique=True, nullable=False)
    business_bio = dataBase.Column(dataBase.String(150), nullable=False)
    business_addy = dataBase.Column(dataBase.String(50), nullable=False)
    business_photos = dataBase.Column(dataBase.String(50))
    business_type = dataBase.Column(dataBase.String(50), nullable=False)

    @classmethod
    def createMethod(self, business_name, business_bio, business_addy, business_photos, business_type):
        myCard = Cardpost()
        myCard.business_name = business_name
        myCard.business_bio = business_bio
        myCard.business_addy = business_addy
        myCard.business_photos = business_photos
        myCard.business_type = business_type

        dataBase.session.add(myCard)
        dataBase.session.commit()
        return myCard