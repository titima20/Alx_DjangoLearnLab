# Advanced API Project

## API Endpoints

### Books API

- GET /api/books/ - List all books (Public access)
- GET /api/books/<id>/ - Get book details (Public access)
- POST /api/books/create/ - Create new book (Authentication required)
- PUT /api/books/<id>/update/ - Update book (Authentication required)
- DELETE /api/books/<id>/delete/ - Delete book (Authentication required)

## Authentication

This API uses token authentication. To access protected endpoints:

1. Obtain a token through the login endpoint
2. Include the token in the Authorization header:
   `Authorization: Token <your-token>`

## Permissions

- List and Detail views are public
- Create, Update, and Delete operations require authentication
