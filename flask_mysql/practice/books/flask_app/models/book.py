from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_on = data['created_on']
        self.updated_on = data['updated_on']
        self.authors_fav = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books ( title, num_of_pages, created_on , updated_on) VALUES (%(title)s,%(num_of_pages)s, NOW(),NOW());"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        return connectToMySQL('books_schema').query_db(query)

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM books WHERE id = %(id)s";
        result = connectToMySQL('books_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_fav_books( cls , data ):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"
        result = connectToMySQL('books_schema').query_db(query,data)
        # return cls(result[0])
        book = cls( result[0] )
        for row in result:
            if row['authors.id'] == None:
                break
            author_data = {
                "id" : row["authors.id"],
                "name" : row["name"],
                "created_on" : row["authors.created_on"],
                "updated_on" : row["authors.updated_on"]
            }
            book.authors_fav.append( author.Author( author_data ) )
        return book

    @classmethod
    def unfavorited_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"
        results = connectToMySQL('books_schema').query_db(query,data)
        books = []
        for row in results:
            books.append(cls(row))
        print(books)
        return books
