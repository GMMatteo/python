from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'dojo_survey'

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_all(cls,data):
        query = "INSERT INTO dojos (name,location,language,comment,created_at,updated_at) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s, NOW(), NOW())"
        dojo_id = connectToMySQL(db).query_db(query,data)
        return dojo_id

    @classmethod
    def get_one(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        results = connectToMySQL(db).query_db(query)
        return Dojo(results[0])

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters")
            is_valid = False
        if len(dojo['location']) < 3:
            flash("Location must be at least 3 characters")
            is_valid = False
        if len(dojo['language']) < 2:
            flash("Must choose a favorite language")
            is_valid = False
        if 0 < len(dojo['comment']) < 3:
            is_valid = False
            flash("Comments must be empty or at least 3 characters.")
        return is_valid

    # @classmethod
    # def save_dojo(cls,data):
    #     query = "INSERT INTO dojos (location,created_at,updated_at) VALUES (%(location)s, NOW(), NOW())"
    #     dojo_id = connectToMySQL(db).query_db(query,data)
    #     return dojo_id

    # @classmethod
    # def save_lang(cls,data):
    #     query = "INSERT INTO dojos (language,created_at,updated_at) VALUES (%(language)s, NOW(), NOW())"
    #     lang_id = connectToMySQL(db).query_db(query,data)
    #     return lang_id

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM dojos;"
    #     dojos_from_db =  connectToMySQL(db).query_db(query)
    #     dojos =[]
    #     for d in dojos_from_db:
    #         dojos.append(cls(d))
    #     return dojos

    # @classmethod
    # def get_langs(cls):
    #     query = "SELECT language FROM dojos;"
    #     languages_from_db =  connectToMySQL(db).query_db(query)
    #     languages =[]
    #     for l in languages_from_db:
    #         languages.append(cls(l))
    #     return languages

    # @classmethod
    # def get_dojos(cls):
    #     query = "SELECT location FROM dojos;"
    #     locations_from_db =  connectToMySQL(db).query_db(query)
    #     locations =[]
    #     for l in locations_from_db:
    #         locations.append(cls(l))
    #     return locations

    # @staticmethod
    # def validate_location(dojo):
    #     is_valid = True
    #     if len(dojo['location']) < 3:
    #         flash("Location must be at least 3 characters")
    #         is_valid = False
    #     return is_valid

    # @staticmethod
    # def validate_language(dojo):
    #     is_valid = True
    #     if len(dojo['language']) < 3:
    #         flash("Language must be at least 3 characters")
    #         is_valid = False
    #     return is_valid