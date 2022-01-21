from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

db = 'email_valid'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$')

class User:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        query = "INSERT INTO users (name,email,password) VALUES (%(name)s,%(email)s,%(password)s)"
        user_id = connectToMySQL(db).query_db(query,data)
        return user_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        users_in_db =  connectToMySQL(db).query_db(query)
        users =[]
        for u in users_in_db:
            users.append(cls(u))
        return users

    @classmethod
    def delete(cls, data ):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query,data)

    @staticmethod
    def valid_email(email):
        valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query,email)
        if len(results) >= 1:
            flash("Email already taken. Please Try Again.")
            valid=False
        return valid

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['name']) < 3:
            flash("Name must be at least 3 characters")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address! Must have @ symbol")
            is_valid = False
        if not PW_REGEX.match(user['password']):
            flash("Invalid password - Must be more then 8 Characters with At Least 1 Number & 1 Special Character")
            is_valid = False
        return is_valid

