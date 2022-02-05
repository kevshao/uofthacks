from dbus import Bus
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/formspage', methods=['GET', 'POST'])
def forms():
    if request.method == 'POST':
        BusinessName = request.form.get('BusinessName')

        # add business name into the database
        if len(BusinessName) >= 2:
            flash('input successful', category='success')
        elif "kevin" in BusinessName:
            flash('this business name sucks bro', category='error')
        else:
            flash('Card succesfully made', category='success')

    return render_template("form.html", boolean=True)


@auth.route('/aboutUs')
def aboutUs():
    return "<h2>Aboutus</h2>"