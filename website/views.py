from flask import Blueprint

views = Blueprint('views', __name__)

# add URL to homepage
@views.route('/') 
def home():
    return "<h1>HomeGallery</h1>"