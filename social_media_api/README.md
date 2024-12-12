# Social Media API

A Django REST Framework-based Social Media API with user authentication.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start server: `python manage.py runserver`

## API Endpoints

- POST /api/accounts/register/ - Register new user
- POST /api/accounts/login/ - Login and get token

## Authentication

Use Token Authentication header:
`Authorization: Token <your-token>`
