from flask import Blueprint, render_template
views = Blueprint('views', __name__)

# add URL to homepage
@views.route('/') 
def home():
    return render_template("index.html", boolean=True)