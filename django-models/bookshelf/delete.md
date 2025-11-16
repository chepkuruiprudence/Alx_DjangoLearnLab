# Delete the book
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
Book.objects.all()
# Expected output: <QuerySet []>
