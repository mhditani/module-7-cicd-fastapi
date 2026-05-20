# Module 7 – FastAPI CI/CD Project

A production-ready FastAPI backend application built for Software Engineering Module 7.

This project demonstrates backend API development, PostgreSQL integration, Docker containerization, automated testing, CI/CD pipelines, and cloud deployment using Render and Supabase.

## Features

- FastAPI REST API
- PostgreSQL database integration
- SQLAlchemy ORM
- Alembic database migrations
- CRUD operations
- Machine Learning prediction endpoint
- Sentiment analysis API
- Pytest automated testing
- Docker containerization
- GitHub Actions CI/CD pipeline
- Render cloud deployment
- Supabase PostgreSQL hosting

## Project Structure

```bash
Module 7/
├── .github/workflows/
│   └── workflow.yaml
├── alembic/
├── app/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   └── utils/
├── tests/
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
├── main.py
└── README.md

Technologies Used
FastAPI
Python 3.12
PostgreSQL
Supabase
SQLAlchemy
Alembic
Pytest
Docker
GitHub Actions
Render
Scikit-learn
Hugging Face Transformers

Installation
git clone https://github.com/mhditani/module-7-cicd-fastapi.git
cd module-7-cicd-fastapi
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Environment Variables

Create a .env file:

DATABASE_URL=your_database_url

Example:

DATABASE_URL=postgresql://username:password@localhost:5432/mydatabase
Run the Application
uvicorn main:app --reload

Open:

http://127.0.0.1:8000/docs
Run Tests
pytest
Docker

Build the Docker image:

docker build -t fastapi-app .

Run the container:

docker run -p 8000:8000 fastapi-app
CI/CD Pipeline

This project uses GitHub Actions.

The workflow performs:

dependency installation
PostgreSQL service setup
automated testing with pytest
Docker image build

Workflow file:

.github/workflows/workflow.yaml
Deployment

The application is deployed using:

Render for hosting
Supabase for PostgreSQL database
API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc
Author

Mohammad Itani

GitHub: https://github.com/mhditani

Repository: https://github.com/mhditani/module-7-cicd-fastapi

License

This project is for educational purposes.
