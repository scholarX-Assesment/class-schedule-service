# Class Schedule Service

## Overview
The Class Schedule Service is a RESTful API that allows users to manage class schedules, teachers, and classes. It provides endpoints to create, retrieve, and delete class schedules, teachers, and classes.

## Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL
- SQLAlchemy
- FastAPI
- Pydantic

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/class-schedule-service.git
   cd class-schedule-service
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   - Create a PostgreSQL database.
   - Update the `DATABASE_URL` in the `config.py` file with your database credentials.

5. **Run the database migrations:**
   ```bash
   alembic upgrade head
   ```

6. **Start the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```

7. **Access the API documentation:**
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation.

### Running Tests
To run the tests, use the following command:
```bash
pytest
```