from django.urls import path
from . import views

urlpatterns = [
    path('booklist/', views.booklist, name="booklist"),
    path('librarylist/<int:pk>/', views.LibraryListView.as_view(), name="librarylist"),
    path('adminsonly/', views.AdminOnlyView, name="adminsonly"),
    path('librarian/', views.LibrarianView, name="librarian"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('members/', views.MemberView.as_view(), name="members"),

    path('book_add/', views.AddBookView.as_view(), name='addbook'),
    path('book_edit/', views.EditBookView.as_view(), name='editbook'),
    path('book_delete', views.DeleteBookView.as_view(), name='deletebook')
]

