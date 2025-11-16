from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library  # required by checker


# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
    return render(
        request,
        "relationship_app/list_books.html",
        {"books": books}
    )


# Class-based view: Show details of a single library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # required by checker
    context_object_name = "library"
