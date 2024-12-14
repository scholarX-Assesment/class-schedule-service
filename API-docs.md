# Class Schedule Service API Documentation

## Endpoints

### Get Class Schedule
- **URL:** `/class-schedules/{class_schedule_id}`
- **Method:** `GET`
- **Description:** Retrieve a class schedule by its ID.
- **Parameters:**
  - `class_schedule_id` (int): The ID of the class schedule to retrieve.
- **Response:**
  - `200 OK`: Returns the class schedule object.
  - `404 Not Found`: If the class schedule does not exist.

### Get Class Schedules
- **URL:** `/class-schedules`
- **Method:** `GET`
- **Description:** Retrieve a list of class schedules.
- **Parameters:**
  - `skip` (int, optional): Number of records to skip. Default is 0.
  - `limit` (int, optional): Maximum number of records to return. Default is 10.
- **Response:**
  - `200 OK`: Returns a list of class schedules.

### Create Class Schedule
- **URL:** `/class-schedules`
- **Method:** `POST`
- **Description:** Create a new class schedule.
- **Request Body:**
  - `class_schedule` (ClassScheduleCreate): The class schedule data to create.
- **Response:**
  - `201 Created`: Returns the created class schedule object.

### Delete Class Schedule
- **URL:** `/class-schedules/{class_schedule_id}`
- **Method:** `DELETE`
- **Description:** Delete a class schedule by its ID.
- **Parameters:**
  - `class_schedule_id` (int): The ID of the class schedule to delete.
- **Response:**
  - `200 OK`: Returns the deleted class schedule object.
  - `404 Not Found`: If the class schedule does not exist.

### Get Teacher
- **URL:** `/teachers/{teacher_id}`
- **Method:** `GET`
- **Description:** Retrieve a teacher by their ID.
- **Parameters:**
  - `teacher_id` (int): The ID of the teacher to retrieve.
- **Response:**
  - `200 OK`: Returns the teacher object.
  - `404 Not Found`: If the teacher does not exist.

### Create Teacher
- **URL:** `/teachers`
- **Method:** `POST`
- **Description:** Create a new teacher.
- **Request Body:**
  - `teacher` (TeacherCreate): The teacher data to create.
- **Response:**
  - `201 Created`: Returns the created teacher object.

### Delete Teacher
- **URL:** `/teachers/{teacher_id}`
- **Method:** `DELETE`
- **Description:** Delete a teacher by their ID.
- **Parameters:**
  - `teacher_id` (int): The ID of the teacher to delete.
- **Response:**
  - `200 OK`: Returns the deleted teacher object.
  - `404 Not Found`: If the teacher does not exist.

### Get Class
- **URL:** `/classes/{class_id}`
- **Method:** `GET`
- **Description:** Retrieve a class by its ID.
- **Parameters:**
  - `class_id` (int): The ID of the class to retrieve.
- **Response:**
  - `200 OK`: Returns the class object.
  - `404 Not Found`: If the class does not exist.

### Create Class
- **URL:** `/classes`
- **Method:** `POST`
- **Description:** Create a new class.
- **Request Body:**
  - `class` (ClassCreate): The class data to create.
- **Response:**
  - `201 Created`: Returns the created class object.

### Delete Class
- **URL:** `/classes/{class_id}`
- **Method:** `DELETE`
- **Description:** Delete a class by its ID.
- **Parameters:**
  - `class_id` (int): The ID of the class to delete.
- **Response:**
  - `200 OK`: Returns the deleted class object.
  - `404 Not Found`: If the class does not exist.