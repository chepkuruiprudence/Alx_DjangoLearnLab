from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm, ExampleForm  # <-- add ExampleForm here
from django.http import HttpResponse


def my_view(request):
    response = HttpResponse("Hello secure world")
    response['Content-Security-Policy'] = "default-src 'self'"
    return response


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):  # renamed from list_books
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            return redirect('book_list')  # update redirect
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # update redirect
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # update redirect
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

def search_books(request):
    query = request.GET.get('q', '')
    # Use ORM filter with parameterized query, not string concatenation
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books, 'query': query})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():  # validates and sanitizes input
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})
