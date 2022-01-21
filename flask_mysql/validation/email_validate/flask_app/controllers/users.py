from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_user',methods=['POST'])
def create():
    if not User.valid_email(request.form):
        return redirect ('/')
    if not User.validate_user(request.form):
        return redirect('/')
    User.create(request.form)
    email = request.form["email"]
    flash(f"The {email} email has successfully been created and is Valid. Thank You!")
    print(request.form["name"])
    return redirect('/success')

@app.route('/success')
def results():
    return render_template("success.html", results=User.get_all())

@app.route('/delete/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.delete(data)
    return redirect('/')