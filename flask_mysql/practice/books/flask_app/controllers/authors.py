from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def index():
    return redirect ("/author")

@app.route('/author')
def authors():
    author = Author.get_all()
    return render_template("index.html", authors = author)

@app.route('/newAuthor', methods=["POST"])
def add_author():
    Author.save(request.form)
    return redirect('/author')

@app.route('/authors/<int:id>')
def show_authors(id):
    data ={
        "id":id
    }
    return render_template("author_show.html", author=Author.get_one(data), unfavorited_books=Book.unfavorited_books(data), favs=Author.get_books(data))

@app.route('/addFavBook',methods=['POST'])
def join_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/authors/{request.form['author_id']}")