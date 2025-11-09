# Retrieve book records
```bash
python manage.py shell
>>> from library.models import Book
>>> Book.objects.all()
