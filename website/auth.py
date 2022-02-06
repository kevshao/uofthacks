
from flask import Blueprint, render_template, request, flash, request, url_for
from .models import Post
from . import dataBase


auth = Blueprint('auth', __name__)

@auth.route('/formspage', methods=['GET', 'POST'])
def forms():
    """ Function for our form, checks for proper input"""
    if request.method == 'POST':
        BusinessName = request.form.get('BusinessName')
        Bio = request.form.get('Bio')
        Address = request.form.get('Address')
        Photos = request.form.get('Photos')
        BusinessType = request.form.get('BusinessType')


        # add business name into the database
        if len(BusinessName) <= 0:
            flash('enter a business name', category='noData')
        elif len(Bio) <= 0:
            flash('say something to you clients!', category='noData')
        elif len(Address) <= 0:
            flash('enter the location of your business', category='noData')
        elif BusinessType == "Choose":
            flash('choose one of the business types', category = 'noData' )
        else:
            new_post = Post(BusinessName=BusinessName, Bio=Bio, Addy=Address, Photos=Photos, BusinessType=BusinessType)
            flash('Card succesfully made', category='success') 
            #return redirect(url_for('views.home'))


    return render_template("form.html", boolean=True)


@auth.route('/aboutUs')
def aboutUs():
    """Function for"""
    return render_template("aboutus.html", boolean=True)

@auth.route('/gallery')
def gallery():
    """Function for"""
    return render_template("index.html", boolean=True)