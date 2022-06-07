from pyhessian.client import HessianProxy


class _HessianClient:
    instance = None
    proxy = None

    def __init__(self, server):
        url = "http://localhost"
        if server == "Java":
            url = url + ":8080"
        url = url + "/Hessian" + server + "Server/books"
        if server == "Php":
            url = url + ".php"
        self.proxy = HessianProxy(url)

    def ping(self):
        return self.proxy.ping()

    def getAllAuthors(self):
        return self.proxy.getAllAuthors()

    def getAuthorsBySearch(self, keyword):
        return self.proxy.getAuthorsBySearch(keyword)

    def getAuthorById(self, id):
        return self.proxy.getAuthorById(int(id))

    def editAuthor(self, id, name, age):
        self.proxy.editAuthor(int(id), name, int(age))

    def deleteAuthor(self, id):
        self.proxy.deleteAuthor(int(id))

    def addAuthor(self,name, age):
        self.proxy.addAuthor(name, int(age))

    def getAllBooks(self):
        return self.proxy.getAllBooks()

    def getBooksBySearch(self, keyword):
        return self.proxy.getBooksBySearch(keyword)

    def getBookById(self, id):
        return self.proxy.getBookById(int(id))

    def editBook(self, id, title, description, year, authorId):
        self.proxy.editBook(int(id), title, description, int(year), int(authorId))

    def deleteBook(self, id):
        self.proxy.deleteBook(int(id))

    def addBook(self, title, description, year, authorId):
        self.proxy.addBook(title, description, int(year), int(authorId))


def service(server):
    _HessianClient.instance = _HessianClient(server)
    return _HessianClient.instance
