from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass123')
        
        # Create test author
        self.author = Author.objects.create(name='Test Author')
        
        # Create test book
        self.book = Book.objects.create(
            title='Test Book',
            publication_year=2023,
            author=self.author
        )


    def test_list_books(self):
        """Test retrieving a list of books"""
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book(self):
        """Test creating a new book"""
        self.client.force_authenticate(user=self.user)
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_retrieve_book(self):
        """Test retrieving a single book"""
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_update_book(self):
        """Test updating a book"""
        self.client.force_authenticate(user=self.user)
        url = reverse('book-update')
        data = {
            'title': 'Updated Book',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        """Test deleting a book"""
        self.client.force_authenticate(user=self.user)
        url = reverse('book-delete')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_search_books(self):
        """Test searching books"""
        url = reverse('book-list') + '?search=Test'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books(self):
        """Test filtering books"""
        url = reverse('book-list') + '?publication_year=2023'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        """Test ordering books"""
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

