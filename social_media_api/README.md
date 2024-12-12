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

# Social Media API Deployment Guide

## Production Environment Setup

1. Configuration Files:

- settings.py: Production settings with DEBUG=False and secure configurations
- requirements.txt: All project dependencies
- Procfile: Gunicorn web server configuration
- runtime.txt: Python 3.12.0 specification
- nginx.conf: Nginx reverse proxy setup

2. Environment Variables:

```bash
DJANGO_SECRET_KEY=your_secret_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_STORAGE_BUCKET_NAME=your_bucket_name

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic

# Run migrations
python manage.py migrate

# Start Gunicorn
gunicorn social_media_api.wsgi --bind 0.0.0.0:8000

```
