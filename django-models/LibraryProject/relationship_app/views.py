from typing import Any

# Django imports
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, DeleteView, UpdateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin

# App-specific imports
from .models import Author, Book, Librarian, Library, UserProfile
from .forms import BookForm


# Views for listing and displaying models
def booklist(request):
    """View to display list of all books."""
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context=context)

class LibraryListView(DetailView):
    """View to display details of a specific library and its books."""
    model = Library
    template_name = 'relationship_app/librarylist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()
        return context


# Helper functions for access control
def has_role(user, role):
    """Checks if the user has the specified role."""
    return UserProfile.objects.filter(user=user.id, role=role).exists()

def is_admin(user):
    """Checks if the user is an Admin."""
    return has_role(user, "Admin")

def is_librarian(user):
    """Checks if the user is a Librarian."""
    return has_role(user, "Librarian")


# Views restricted by user roles
@user_passes_test(is_admin)
def AdminOnlyView(request):
    """View accessible only to Admins."""
    user = request.user
    return render(request, 'relationship_app/admin_view.html', {"user": user})

@user_passes_test(is_librarian)
def LibrarianView(request):
    """View accessible only to Librarians."""
    user = request.user
    return render(request, 'relationship_app/librarian_view.html', {"user": user})


# User registration and profile views
class RegisterView(CreateView):
    """View for user registration."""
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

class ProfileView(TemplateView):
    """User profile view."""
    template_name = 'relationship_app/profile.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


# Authentication views
class LoginView(LoginView):
    """User login view."""
    template_name = 'relationship_app/login.html'

class LogoutView(LogoutView):
    """User logout view."""
    template_name = 'relationship_app/logout.html'


# Member view restricted by role
class MemberView(UserPassesTestMixin, TemplateView):
    """View accessible only to Members."""
    template_name = 'relationship_app/member_view.html'

    def test_func(self) -> bool:
        return hasattr(self.request.user, "Member")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context

#views to pages that can add, edit, delete and browse books

class AddBookView(PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'relationship_app/addbook.html'
    permission_required = ["relationship_app.add_book"]
    success_url = reverse_lazy('booklist')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["authors"] = Author.objects.all()
        return context

# 2. EditBookView
class EditBookView(PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'relationship_app/editbookview.html'
    permission_required = ["relationship_app.change_book"]
    success_url = reverse_lazy('booklist')  # Redirect to book list or relevant page after editing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()  # Add authors for the dropdown
        return context


# 3. DeleteBookView
class DeleteBookView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'relationship_app/deletebookview.html'
    permission_required = ["relationship_app.delete_book"]
    success_url = reverse_lazy('booklist')  # Redirect to book list or relevant page after deleting
    