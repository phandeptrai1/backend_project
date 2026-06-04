# Data Extraction Service

## Setup

```bash
git clone <repo>

cd project

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Database

```bash
python manage.py migrate
```

## Run

```bash
python manage.py runserver
```

## Swagger

http://localhost:8000/api/docs/

## Run Tests

```bash
pytest
```

## Health Endpoint

GET

/api/v1/health
