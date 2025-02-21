# ORDER MANAGEMENT

A Django REST Framework-based backend service for vehicle procurement, inspection, and management system.

## Project Overview

ProcX is a comprehensive vehicle management platform that handles:
- Vehicle procurement and leads management
- Multi-level inspection workflows
- Pricing engine for vehicle valuation
- Mobile app integration
- Integration with CRM and ERP systems

### Technology Stack

- **Framework**: Django REST Framework
- **Database**: PostgreSQL
- **Caching**: Redis
- **Task Queue**: Celery
- **API Documentation**: drf-spectacular (OpenAPI/Swagger)


### System Components

1. **API Layer (Django REST Framework)**
   - RESTful API endpoints
   - Request/Response handling
   - Serialization/Deserialization
   - Validation using Pydantic

2. **Apps Structure**
   - `order_management/`: Main app for setting/server files 
   - `orders/`: custom app for api endpoints 

4. **Background Processing**
   - Celery for async task processing
   - Redis as message broker

5. **Data Storage**
   - PostgreSQL for primary data storage
   - Redis for caching and session storage

### Key Features

- Modular app architecture
- Strong type checking with Pydantic
- Robust error handling
- Efficient database querying
- Scalable background task processing



## Development Setup

### Prerequisites

1. Install required system packages:
   - Python 3.x
   - PostgreSQL
   - Redis
   - Docker (optional)

2. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Environment Configuration

1. Copy sample environment file:
```bash
cp .env.sample .env
```

2. Update the following variables in `.env`:
```env
# Database
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Redis
REDIS_URL=redis://localhost:6379



### Docker Setup


2. Run Redis container:
```bash
docker run --name redis -d -p 6379:6379 redis
```

3. Build and run the application:
```bash
docker build -t order_management .
docker run -p 8000:8000 order_management
```

### Running Locally

1. Apply database migrations:
```bash
python manage.py migrate
```

2. Start development server:
```bash
python manage.py runserver
```

3. Start Celery worker:
```bash
celery -A order_management worker -l info
```

```

## Testing

Run tests with:
```bash
python manage.py test
```

For coverage report:
```bash
coverage run manage.py test
coverage report
```

## Deployment

1. Update environment variables for production
2. Configure proper security settings
3. Set up proper process management (gunicorn, supervisor)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

### Code Style

- Follow PEP 8 guidelines
- Use type hints
- Write docstrings for functions/classes
- Keep functions/methods focused and small
- Write tests for new features

