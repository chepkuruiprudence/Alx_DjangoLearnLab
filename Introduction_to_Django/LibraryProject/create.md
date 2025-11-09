# Create a new book record
```bash
python manage.py shell
>>> from library.models import Book
>>> Book.objects.create(title="New Book", author="Author Name")
