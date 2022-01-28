from flask import render_template, session,redirect, request,flash
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User
from flask_app.models.message import Message
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register/user',methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = User.create_user(data)
    session['user_id'] = user_id
    return redirect('/wall')

@app.route('/login',methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    if 'count' in session:
        session['count']+=1
    else:
        session['count']=0
    return redirect('/wall')

@app.route('/wall')
def wall():
    if 'user_id' not in session:
        return redirect('/')
    data ={
        'id': session['user_id']
    }
    user=User.get_by_id(data)
    messages = Message.get_messages(data)
    users = User.get_all()
    return render_template("wall.html", user=user, users=users, messages=messages)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')