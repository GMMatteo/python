from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.friendships =[]
# Now we use class methods to query our database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name, last_name, created_at , updated_at ) VALUES (%(first_name)s, %(last_name)s, NOW(),NOW());"
        results = connectToMySQL('friendships_schema').query_db(query, data)
        return  results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('friendships_schema').query_db(query)
        users = []
        for x in results:
            users.append( cls(x))
        return users

    @classmethod
    def get_friendships(cls):
        query = """
                SELECT users2.id, users2.first_name, users2.last_name, users2.created_at, users2.updated_at, users.id, users.first_name, users.last_name, users.created_at, users.updated_at
                FROM users JOIN friendships ON users.id = friendships.user_id
                LEFT JOIN users as users2 ON users2.id = friendships.friend_id
                ORDER BY users2.first_name;"""
        results = connectToMySQL('friendships_schema').query_db(query)
        friends = []
        for row in results:
            friend = {
                "id" : row["id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "created_at" : row["created_at"],
                "updated_at" : row["updated_at"]
            }
            if len(friends) > 0:
                if friends[len(friends)-1].id !=friend['id']:
                    friends.append(cls(friend))
            else:
                friends.append(cls(friend))
            buddy = {
                "id" : row["users.id"],
                "first_name" : row["users.first_name"],
                "last_name" : row["users.last_name"],
                "created_at" : row["users.created_at"],
                "updated_at" : row["users.updated_at"]
            }
            if buddy['id'] != None:
                friends[len(friends)-1].friendships.append(cls(buddy))
        return friends

    @classmethod
    def make_friends(cls, data):
        query = "INSERT INTO friendships (user_id, friend_id, created_at, updated_at) VALUES (%(user_id)s, %(friend_id)s, NOW(), NOW());"
        results = connectToMySQL('friendships_schema').query_db(query, data)
        print(results)
        return  results

    @classmethod
    def destroy(cls, data):
        query = "DELETE from friendships WHERE id = %(id)s"
        results = connectToMySQL('friendships_schema').query_db(query, data)
        print(results)
        return  results