
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Cardpost
from . import dataBase
import sqlite3

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
            
            # Cardpost.createMethod(BusinessName, Bio, Address, Photos, 'errorhere')
            # kevin = sqlite3.connect('database.db')
            # sql_insert = "INSERT INTO Cardpost(BusinessName, Bio, Address, Photos, BusinessType) VALUES (%s, %s, %s, %s, %s)"
            # kevin.execute(sql_insert, Cardpost)
            # flash('Card succesfully made', category='success')
            # kevin.close()
            # new_post = Cardpost(business_name=BusinessName, business_bio=Bio, business_addy=Address, business_photos=Photos, business_type=BusinessType)
            # dataBase.session.add(new_post)
            # dataBase.session.commit()
            flash('Card succesfully made', category='success')
            return redirect(url_for('views.home'))

    return render_template("form.html", boolean=True)


@auth.route('/aboutUs')
def aboutUs():
    """Function for"""
    return render_template("aboutus.html", boolean=True)

@auth.route('/gallery')
def gallery():
    """Function for"""
    return render_template("index.html", boolean=True)