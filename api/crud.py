from sqlalchemy.orm import Session
from ..database import models, schemas

def get_class_schedule(db: Session, class_schedule_id: int):
    return db.query(models.ClassSchedule).filter(models.ClassSchedule.id == class_schedule_id).first()

def get_class_schedules(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ClassSchedule).offset(skip).limit(limit).all()

def create_class_schedule(db: Session, class_schedule: schemas.ClassScheduleCreate):
    db_class_schedule = models.ClassSchedule(**class_schedule.dict())
    db.add(db_class_schedule)
    db.commit()
    db.refresh(db_class_schedule)
    return db_class_schedule

def delete_class_schedule(db: Session, class_schedule_id: int):
    db_class_schedule = db.query(models.ClassSchedule).filter(models.ClassSchedule.id == class_schedule_id).first()
    if db_class_schedule:
        db.delete(db_class_schedule)
        db.commit()
    return db_class_schedule

def get_teacher(db: Session, teacher_id: int):
    return db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()

def create_teacher(db: Session, teacher: schemas.TeacherCreate):
    db_teacher = models.Teacher(**teacher.dict())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def delete_teacher(db: Session, teacher_id: int):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if db_teacher:
        db.delete(db_teacher)
        db.commit()
    return db_teacher

def get_class(db: Session, class_id: int):
    return db.query(models.Class).filter(models.Class.id == class_id).first()

def create_class(db: Session, class_: schemas.ClassCreate):
    db_class = models.Class(**class_.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

def delete_class(db: Session, class_id: int):
    db_class = db.query(models.Class).filter(models.Class.id == class_id).first()
    if db_class:
        db.delete(db_class)
        db.commit()
    return db_class