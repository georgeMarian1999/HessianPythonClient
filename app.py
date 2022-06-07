from flask import Flask, render_template, request, redirect, url_for
from client.HessianPythonClient import service

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    serverName = request.args.get("server")
    client = service(serverName)
    ping = client.ping()

    return render_template("home.html", server=serverName, ping=ping)


@app.route("/authors")
def authors():
    serverName = request.args.get("server")
    client = service(serverName)
    keyword = request.args.get("search-parameter")
    if keyword:
        authors = client.getAuthorsBySearch(keyword)
    else:
        authors = client.getAllAuthors()

    if authors is None:
        authors = []

    return render_template("authors.html", server=serverName, authors=authors)

@app.route("/author-detail")
def authorDetail():
    serverName = request.args.get("server")
    client = service(serverName)
    id = request.args.get("authorId")
    author = client.getAuthorById(id)
    return render_template("author-detail.html", author=author, server=serverName)


@app.route("/edit-author")
def editAuthor():
    serverName = request.args.get("server")
    client = service(serverName)
    id = request.args.get("authorId")
    name = request.args.get("name")
    age = request.args.get("age")
    client.editAuthor(id, name, age)
    return redirect(url_for("authors", server=serverName))


@app.route("/delete-author")
def deleteAuthor():
    serverName = request.args.get("server")
    client = service(serverName)
    id = request.args.get("authorId")
    client.deleteAuthor(id)
    return redirect(url_for("authors", server=serverName))

@app.route("/author-add")
def authorAdd():
    serverName = request.args.get("server")

    return render_template("author-add.html", server=serverName)


@app.route("/add-author")
def addAuthor():
    serverName = request.args.get("server")
    client = service(serverName)
    name = request.args.get("name")
    age = request.args.get("age")
    client.addAuthor(name, age)
    return redirect(url_for("authors", server=serverName))

@app.route("/books")
def books():
    serverName = request.args.get("server")
    client = service(serverName)
    keyword = request.args.get("search-parameter")

    if keyword:
        books = client.getBooksBySearch(keyword)
    else:
        books = client.getAllBooks()

    if books is None:
        books = []
    return render_template("books.html", server=serverName, books=books)

@app.route("/book-detail")
def bookDetail():
    serverName = request.args.get("server")
    client = service(serverName)
    bookId = request.args.get("bookId")
    book = client.getBookById(bookId)
    authors = client.getAllAuthors()

    return render_template("book-detail.html",book=book, authors=authors, server=serverName)


@app.route("/book-add")
def bookAdd():
    serverName = request.args.get("server")
    client = service(serverName)
    authors = client.getAllAuthors()

    return render_template("book-add.html", server=serverName, authors=authors)

@app.route("/edit-book")
def editBook():
    serverName = request.args.get("server")
    client = service(serverName)
    bookId = request.args.get("bookId")
    title = request.args.get("title")
    description = request.args.get("description")
    year = request.args.get("year")
    authorId = request.args.get("authorId")
    client.editBook(bookId, title, description,year, authorId)
    return redirect(url_for("books", server=serverName))

@app.route("/delete-book")
def deleteBook():
    serverName = request.args.get("server")
    client = service(serverName)
    bookId = request.args.get("bookId")
    client.deleteBook(bookId)
    return redirect(url_for("books", server=serverName))


@app.route("/add-book")
def addBook():
    serverName = request.args.get("server")
    client = service(serverName)
    title = request.args.get("title")
    description = request.args.get("description")
    year = request.args.get("year")
    authorId = request.args.get("authorId")

    client.addBook(title, description, year, authorId)
    return redirect(url_for("books", server=serverName))

if __name__ == '__main__':
    app.run()
