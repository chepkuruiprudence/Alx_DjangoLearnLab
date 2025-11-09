# Retrieve all Book instances
from bookshelf.models import Book

books = Book.objects.all()
books
# Expected output: <QuerySet [<Book: Book object (1)>]>

# Retrieve attributes of the first book
book = books.first()
book.title  # "1984"
book.author  # "George Orwell"
book.publication_year  # 1949
