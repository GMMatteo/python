from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/books')
def books():
    book = Book.get_all()
    return render_template("books.html", books = book)

@app.route('/newBook', methods=["POST"])
def add_book():
    Book.save(request.form)
    return redirect('/books')

@app.route('/books/<int:id>')
def show_book(id):
    data ={
        "id":id
    }
    print(Book.get_fav_books(data))
    print('it worked')
    return render_template("book_show.html", book=Book.get_one(data), unfavorited_authors=Author.unfavorited_authors(data), favs=Book.get_fav_books(data))

@app.route('/addFavAuthor',methods=['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/books/{request.form['book_id']}")