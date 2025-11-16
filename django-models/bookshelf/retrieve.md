# Retrieve all Book instances
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book 
# Expected output: <QuerySet [<Book: Book object (1)>]>

# Retrieve attributes of the first book
book = books.first()
book.title  # "1984"
book.author  # "George Orwell"
book.publication_year  # 1949
