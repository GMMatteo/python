from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_on = data['created_on']
        self.updated_on = data['updated_on']
# Now we use class methods to query our database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas ( first_name, last_name, age , created_on , updated_on, dojo_id ) VALUES (%(first_name)s,%(last_name)s, %(age)s,NOW(),NOW(),%(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query)
