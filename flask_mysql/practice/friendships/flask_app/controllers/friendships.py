from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.friendship import User

@app.route('/')
def index():
    return redirect ("/friendships")

@app.route('/friendships')
def users():
    users = User.get_all()
    friend = User.get_all()
    friendships = User.get_friendships()
    return render_template("index.html", user=users, friends=friendships, friend=friend)

@app.route('/addUser', methods=["POST"])
def add_user():
    User.save(request.form)
    return redirect("/friendships")

@app.route('/newFriendship', methods=["POST"])
def create_friendship():
    User.make_friends(request.form)
    return redirect("/friendships")