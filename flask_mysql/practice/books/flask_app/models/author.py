from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_on = data['created_on']
        self.updated_on = data['updated_on']
        self.fav_books = []
# Now we use class methods to query our database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors ( name, created_on , updated_on ) VALUES (%(name)s,NOW(),NOW());"
        results = connectToMySQL('books_schema').query_db(query, data)
        return  results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for x in results:
            authors.append( cls(x))
        return authors

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM authors WHERE id = %(id)s";
        result = connectToMySQL('books_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def unfavorited_authors(cls,data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        authors = []
        results = connectToMySQL('books_schema').query_db(query,data)
        for row in results:
            authors.append(cls(row))
        return authors

    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id,book_id, created_on, updated_on) VALUES (%(author_id)s, %(book_id)s, NOW(), NOW());"
        return connectToMySQL('books_schema').query_db(query,data);

    @classmethod
    def get_books( cls , data ):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db( query , data )
        favs = cls( results[0] )
        for row in results:
            if row['books.id'] == None:
                break
            book_data = {
                "id" : row["books.id"],
                "title" : row["title"],
                "num_of_pages" : row["num_of_pages"],
                "created_on" : row["books.created_on"],
                "updated_on" : row["books.updated_on"]
            }
            favs.fav_books.append( book.Book( book_data ) )
        return favs
