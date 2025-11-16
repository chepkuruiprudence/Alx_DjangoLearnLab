from django.urls import path
import relationship_app.views as views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs using class-based views
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),

    # Registration uses function-based view
    path('register/', views.register, name='register'),

     # Role-based views
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    # Secured Book actions
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
]
