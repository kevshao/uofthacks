from flask import Blueprint

views = Blueprint('views', __name__)

# add URL to homepage
@views.route('/') 
def home():
    pass # add homepage stuff here 