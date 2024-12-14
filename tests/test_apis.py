from fastapi.testclient import TestClient
from main import app
from database import models, schemas
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_class_schedule():
    response = client.post(
        "/class-schedules",
        json={"name": "Math 101", "teacher_id": 1, "start_time": "09:00", "end_time": "10:00"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Math 101"

def test_get_class_schedule():
    response = client.get("/class-schedules/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Math 101"

def test_get_class_schedules():
    response = client.get("/class-schedules")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_delete_class_schedule():
    response = client.delete("/class-schedules/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Math 101"

def test_create_teacher():
    response = client.post(
        "/teachers",
        json={"name": "John Doe", "subject": "Mathematics"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"

def test_get_teacher():
    response = client.get("/teachers/1")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_delete_teacher():
    response = client.delete("/teachers/1")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_create_class():
    response = client.post(
        "/classes",
        json={"name": "Math Class", "description": "Basic Math Class"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Math Class"

def test_get_class():
    response = client.get("/classes/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Math Class"

def test_delete_class():
    response = client.delete("/classes/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Math Class"
