from flask import Blueprint

auth = Blueprint('auth', __name__)

# add URL to homepage
@auth.route('/') 
def home():
    pass # add homepage stuff here 