# Update a book record
```bash
python manage.py shell
>>> from library.models import Book
>>> b = Book.objects.get(id=1)
>>> b.title = "Updated Title"
>>> b.save()
