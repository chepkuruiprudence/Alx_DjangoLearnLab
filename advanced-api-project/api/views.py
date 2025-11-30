from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ListView: Retrieve all books
# Uses ListAPIView for read-only listing
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]   # Public access


# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]   # Public access


# CreateView: Add a new book
# Uses CreateAPIView and enforces authentication
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

    # Optional customization: attach logged-in user as "creator"
    def perform_create(self, serializer):
        # Additional custom logic can go here
        serializer.save()


# UpdateView: Modify an existing book
# Uses UpdateAPIView
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

    # Additional validation/custom behavior can be added here
    def perform_update(self, serializer):
        serializer.save()


# DeleteView: Remove a book
# Uses DestroyAPIView
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated]  # Auth required

    # Optional: add custom deletion logic
    def perform_destroy(self, instance):
        instance.delete()
