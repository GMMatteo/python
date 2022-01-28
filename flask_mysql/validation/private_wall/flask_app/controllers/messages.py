from flask import render_template, session,flash,redirect, request
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User
from flask_app.models.message import Message


@app.route('/create_message', methods=["POST"] )
def create_msg():
    if 'user_id' not in session:
        return redirect('/')
    if not Message.valid_msg(request.form):
        return redirect('/wall')
    data = {
        "message" : request.form['message'],
        "send_id" : request.form['send_id'],
        "receive_id" : request.form['receive_id'],
    }
    Message.create_message(data)
    if 'count' in session:
        session['count']+=1
    else:
        session['count']=0
    return redirect('/wall')

@app.route('/delete/<int:id>')
def delete(id):
    data ={
        'id': id
    }
    Message.delete_message(data)
    return redirect('/wall')