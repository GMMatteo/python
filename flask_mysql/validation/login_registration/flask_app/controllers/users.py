from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register/user',methods=['POST'])
def register():
    if not User.valid_email(request.form):
        return redirect ('/')
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = User.create(data)
    session['user_id'] = user_id
    return redirect('/profile')

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
    return redirect('/profile')

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("profile.html", user=User.get_by_id(data))

@app.route('/users')
def results():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("users.html", results=User.get_all())

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/delete/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.delete(data)
    return redirect('/profile')