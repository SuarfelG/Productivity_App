from flask import Flask, request, render_template, redirect, url_for, Blueprint, flash
from flask_login import login_user, logout_user, login_required, current_user
import random
import string
from .models import authentication
import bcrypt
from sqlalchemy import orm 
import smtplib
from . import db

auth = Blueprint('auth', __name__)



@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        print(username)
        email = request.form.get('Email')
        password = request.form.get('password')
        confirmPassword = request.form.get('Confirm_password')

        if len(username) < 4:
            flash("Username Too Short", category='error')
            return render_template('signup.html')
        elif len(password) < 4:
            flash("Password Too Short", category='error')
            return render_template('signup.html')
        elif password != confirmPassword:
            flash("Passwords Don't Match", category='error')
            return render_template('signup.html')

        existing_user = authentication.query.filter_by(email=email).first()
        existing_p = authentication.query.filter_by(password=password).first()


        if existing_user or existing_p:
            flash("Email already exists", category='error')
            return render_template('signup.html')

        try:
            newuser = authentication(email=email, password=password, username=username)
            db.session.add(newuser)
            db.session.commit()
            flash("Account Created Successfully", category='success')
            return redirect(url_for('task.home'))
        except:
            flash("An error occurred during account creation. Please try again.", category='error')
            return render_template('signup.html')

    return render_template('signup.html')




@auth.route('/login', methods=['POST', 'GET' ])
def login():
        
        if request.method == "POST":

            username = request.form.get('username')
            password = request.form.get('password')


            userNameExist = authentication.query.filter_by(username=username).first() 
            passExist= authentication.query.filter_by(password=password).first()

            if userNameExist :
                if passExist:
                    login_user(userNameExist)
                    flash('Logged in successfully', category='success')
                    return redirect(url_for('task.home'))
                
                flash('Invalid  password', category='error')
                return render_template('login.html')
            
            else:
                flash('Invalid username', category='error')
                return render_template('login.html')

        return render_template('login.html')

@auth.route('/resetpassword', methods=['POST', 'GET' ])
def reset():
    if request.method=='POST':

        username=request.form.get('username')
        email=request.form.get('Email')

        userNameExist = authentication.query.filter_by(username=username).first() 
        emailExist= authentication.query.filter_by(email=email).first()


        chars=string.ascii_letters
        length=10
        message = ''.join(random.choice(chars) for _ in range(length))


        if userNameExist:
            if emailExist:
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login("surafelgmehin7@gmail.com",'31282526')
                server.sendmail("surafelgmehin7@gmail.com",email,message)
            else:
                flash("User Doesnot Exist" ,category='error')
                return render_template('resetpassword.html')
            
        flash("User Doesnot Exist" ,category='error')
        return render_template('resetpassword.html')

    return render_template ('resetpassword.html')


