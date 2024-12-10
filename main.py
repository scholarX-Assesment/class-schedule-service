from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import models, schemas, database
from api import crud

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Class Schedule API"}

@app.post("/class_schedules/", response_model=schemas.ClassSchedule)
def create_class_schedule(class_schedule: schemas.ClassScheduleCreate, db: Session = Depends(database.get_db)):
    return crud.create_class_schedule(db=db, class_schedule=class_schedule)

@app.get("/class_schedules/{class_schedule_id}", response_model=schemas.ClassSchedule)
def read_class_schedule(class_schedule_id: int, db: Session = Depends(database.get_db)):
    db_class_schedule = crud.get_class_schedule(db, class_schedule_id=class_schedule_id)
    if db_class_schedule is None:
        raise HTTPException(status_code=404, detail="Class schedule not found")
    return db_class_schedule

@app.get("/class_schedules/", response_model=list[schemas.ClassSchedule])
def read_class_schedules(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    class_schedules = crud.get_class_schedules(db, skip=skip, limit=limit)
    return class_schedules

@app.delete("/class_schedules/{class_schedule_id}", response_model=schemas.ClassSchedule)
def delete_class_schedule(class_schedule_id: int, db: Session = Depends(database.get_db)):
    db_class_schedule = crud.delete_class_schedule(db, class_schedule_id=class_schedule_id)
    if db_class_schedule is None:
        raise HTTPException(status_code=404, detail="Class schedule not found")
    return db_class_schedule

@app.post("/teachers/", response_model=schemas.Teacher)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(database.get_db)):
    return crud.create_teacher(db=db, teacher=teacher)

@app.get("/teachers/{teacher_id}", response_model=schemas.Teacher)
def read_teacher(teacher_id: int, db: Session = Depends(database.get_db)):
    db_teacher = crud.get_teacher(db, teacher_id=teacher_id)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher

@app.delete("/teachers/{teacher_id}", response_model=schemas.Teacher)
def delete_teacher(teacher_id: int, db: Session = Depends(database.get_db)):
    db_teacher = crud.delete_teacher(db, teacher_id=teacher_id)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher

@app.post("/classes/", response_model=schemas.Class_)
def create_class(class_: schemas.ClassCreate, db: Session = Depends(database.get_db)):
    return crud.create_class(db=db, class_=class_)

@app.get("/classes/{class_id}", response_model=schemas.Class_)
def read_class(class_id: int, db: Session = Depends(database.get_db)):
    db_class = crud.get_class(db, class_id=class_id)
    if db_class is None:
        raise HTTPException(status_code=404, detail="Class not found")
    return db_class

@app.delete("/classes/{class_id}", response_model=schemas.Class_)
def delete_class(class_id: int, db: Session = Depends(database.get_db)):
    db_class = crud.delete_class(db, class_id=class_id)
    if db_class is None:
        raise HTTPException(status_code=404, detail="Class not found")
    return db_class