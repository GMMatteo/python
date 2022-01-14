from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_on = data['created_on']
        self.updated_on = data['updated_on']
        self.ninjas = []
# Now we use class methods to query our database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name, created_on , updated_on ) VALUES (%(name)s,NOW(),NOW());"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return  results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for x in results:
            dojos.append( cls(x))
        return dojos

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM dojos WHERE id = %(id)s";
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_ninjas_in_dojo(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(result)
        dojo = cls(result[0])
        for row in result:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_on': row['ninjas.created_on'],
                'updated_on': row['ninjas.updated_on']
            }
            dojo.ninjas.append( ninja.Ninja(n) )
        return dojo