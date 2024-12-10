from pydantic import BaseModel

class TeacherBase(BaseModel):
    name: str
    email: str
    subject: str
    contact_no: str

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):
    id: int

    class Config:
        orm_mode = True

class ClassBase(BaseModel):
    name: str
    location: str

class ClassCreate(ClassBase):
    pass

class Class_(ClassBase):
    id: int

    class Config:
        orm_mode = True

class ClassScheduleBase(BaseModel):
    schedule_name: str
    teacher_id: int
    class_id: int 
    time_slot: str

class ClassScheduleCreate(ClassScheduleBase):
    pass

class ClassSchedule(ClassScheduleBase):
    id: int
    teacher: Teacher
    class_: Class_

    class Config:
        orm_mode = True