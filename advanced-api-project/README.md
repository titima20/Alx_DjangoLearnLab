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

## Advanced Query Parameters

### Filtering

Filter books using query parameters:

- `title`: Filter by book title
- `author`: Filter by author
- `publication_year`: Filter by publication year

Example: `/api/books/?publication_year=2023`

### Searching

Search across books using the `search` parameter:

- Searches in book title and author name

Example: `/api/books/?search=python`

### Ordering

Order results using the `ordering` parameter:

- `title`: Order by title
- `publication_year`: Order by publication year
- Use `-` prefix for descending order

Example: `/api/books/?ordering=-publication_year`
