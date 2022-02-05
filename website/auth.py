from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/formspage')
def forms():
    return "<h2>Form here</h2>"


@auth.route('/aboutUs')
def aboutUs():
    return "<h2>Aboutus</h2>"