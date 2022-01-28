from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from datetime import datetime
import math

db = 'private_wall'

class Message:
    def __init__(self,data):
        self.id = data['id']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.send_id = data['send_id']
        self.sender = data['sender']
        self.receive_id = data['receive_id']
        self.receiver = data['receiver']

    def time_stamp(self):
        now = datetime.now()
        delta = now - self.created_at
        print(delta.days)
        print(delta.total_seconds())
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} hours ago"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
        else:
            return f"{math.floor(delta.total_seconds())} seconds ago"

    @classmethod
    def create_message(cls,data):
        query = "INSERT INTO messages (message, send_id, receive_id) VALUES (%(message)s, %(send_id)s,%(receive_id)s);"
        message = connectToMySQL(db).query_db(query,data)
        return message

    @classmethod
    def get_messages(cls,data):
        query = """SELECT users.first_name as sender, users2.first_name as receiver, messages.*
                    FROM users LEFT JOIN messages ON users.id = messages.send_id
                    LEFT JOIN users as users2 ON users2.id = messages.receive_id
                    WHERE users2.id =  %(id)s;"""
        messages = connectToMySQL(db).query_db(query,data)
        message =[]
        for m in messages:
            message.append(cls(m))
        return message

    @staticmethod
    def valid_msg(msg):
        is_valid=True
        if len(msg['message']) < 5:
            flash("Please Add In More Content To Message")
            is_valid = False
        return is_valid

    @classmethod
    def delete_message(cls,data):
        query = "DELETE FROM messages WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query,data)