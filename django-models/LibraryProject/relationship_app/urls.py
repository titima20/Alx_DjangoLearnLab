from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('booklist/', views.booklist, name="booklist"),
    path('librarylist/<int:pk>/', views.LibraryListView.as_view(), name="librarylist"),
    path('adminsonly/', views.AdminOnlyView, name="adminsonly"),
    path('librarian/', views.LibrarianView, name="librarian"),
    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('members/', views.MemberView.as_view(), name="members"),

    path('book_add/', views.AddBookView.as_view(), name='addbook'),
    path('book_edit/', views.EditBookView.as_view(), name='editbook'),
    path('book_delete', views.DeleteBookView.as_view(), name='deletebook')
        path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]
