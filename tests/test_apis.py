import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import database.models as models
import database.schemas as schemas
from api import crud

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_teacher(db):
    teacher = schemas.TeacherCreate(name="John", email="john@gmail.com",subject="Math", contact_no="0771234567")
    db_teacher = crud.create_teacher(db, teacher)
    assert db_teacher.name == "John"
    assert db_teacher.email == "john@gmail.com"

def test_get_teacher(db):
    teacher = schemas.TeacherCreate(name="Jane", email="jane@gmail.com", contact_no="0872833321", subject="Science")
    db_teacher = crud.create_teacher(db, teacher)
    fetched_teacher = crud.get_teacher(db, db_teacher.id)
    assert fetched_teacher.id == db_teacher.id

def test_delete_teacher(db):
    teacher = schemas.TeacherCreate(name="Doe", email="doe@gmail.com", contact_no="0776543210", subject="History")
    db_teacher = crud.create_teacher(db, teacher)
    deleted_teacher = crud.delete_teacher(db, db_teacher.id)
    assert deleted_teacher.id == db_teacher.id

def test_create_class(db):
    class_ = schemas.ClassCreate(name="Class A", location="Room 101")
    db_class = crud.create_class(db, class_)
    assert db_class.name == "Class A"
    assert db_class.location == "Room 101"

def test_get_class(db):
    class_ = schemas.ClassCreate(name="Class B", location="Room 102")
    db_class = crud.create_class(db, class_)
    fetched_class = crud.get_class(db, db_class.id)
    assert fetched_class.id == db_class.id

def test_delete_class(db):
    class_ = schemas.ClassCreate(name="Class C", location="Room 103")
    db_class = crud.create_class(db, class_)
    deleted_class = crud.delete_class(db, db_class.id)
    assert deleted_class.id == db_class.id

def test_create_class_schedule(db):
    teacher = schemas.TeacherCreate(name="John", email="mail@mail.com" ,subject="Math", contact_no="0771234567")
    db_teacher = crud.create_teacher(db, teacher)
    class_ = schemas.ClassCreate(name="Class A", location="Room 101")
    db_class = crud.create_class(db, class_)
    class_schedule = schemas.ClassScheduleCreate(schedule_name="Math Class", teacher_id=db_teacher.id, class_id=db_class.id, time_slot="10:00-11:00")
    db_class_schedule = crud.create_class_schedule(db, class_schedule)
    assert db_class_schedule.schedule_name == "Math Class"
    assert db_class_schedule.teacher.id == db_teacher.id
    assert db_class_schedule.class_.id == db_class.id

def test_get_class_schedule(db):
    teacher = schemas.TeacherCreate(name="Jane", email="luke@ycl.lk", contact_no="0771234567", subject="Science")
    db_teacher = crud.create_teacher(db, teacher)
    class_ = schemas.ClassCreate(name="Class B", location="Room 102")
    db_class = crud.create_class(db, class_)

    class_schedule = schemas.ClassScheduleCreate(schedule_name="Science Class", teacher_id=db_teacher.id, class_id=db_class.id, time_slot="11:00-12:00")
    db_class_schedule = crud.create_class_schedule(db, class_schedule)
    fetched_class_schedule = crud.get_class_schedule(db, db_class_schedule.id)
    assert fetched_class_schedule.id

def test_delete_class_schedule(db):
    teacher = schemas.TeacherCreate(name="Doe", email="lsla@sas.lk", contact_no="0771234567", subject="History")
    db_teacher = crud.create_teacher(db, teacher)
    class_ = schemas.ClassCreate(name="Class C", location="Room 103")
    db_class = crud.create_class(db, class_)
    class_schedule = schemas.ClassScheduleCreate(schedule_name="History Class", teacher_id=db_teacher.id, class_id=db_class.id, time_slot="12:00-13:00")
    db_class_schedule = crud.create_class_schedule(db, class_schedule)
    deleted_class_schedule = crud.delete_class_schedule(db, db_class_schedule.id)
    assert deleted_class_schedule.id


