from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app= FastAPI()

class Student(BaseModel):
    name: str
    age: int
    class_name: str
    
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    class_name: Optional[str] = None

students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "year 12"
    },
    2: {
        "name": "Alice",
        "age": 16,
        "class": "year 11"
    },
    3: {
        "name": "Bob",
        "age": 18,
        "class": "year 12"
    },
    4: {
        "name": "Emma",
        "age": 17,
        "class": "year 12"
    },
    5: {
        "name": "Michael",
        "age": 16,
        "class": "year 11"
    },
    6: {
        "name": "Sarah",
        "age": 18,
        "class": "year 12"
    },
    7: {
        "name": "David",
        "age": 17,
        "class": "year 12"
    },
    8: {
        "name": "Sophia",
        "age": 16,
        "class": "year 11"
    },
    9: {
        "name": "James",
        "age": 18,
        "class": "year 12"
    },
    10: {
        "name": "Olivia",
        "age": 17,
        "class": "year 12"
    }
}


@app.get("/")
def home():
    return{"page": "Homepage"}



# path parameter
@app.get("/home/{variable}")
def mystudents(variable:int=Path(description="Student ID",gt=0)):
    return students[variable]

# combination of both path and query parameter 
@app.get("/get-by-name/{student_id}")
def student__by_name(*,student_id:int,name:Optional[str]=None,test:int=0):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"Data":"Not found"}


# post method //put the values in the body
@app.post("/create/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student already exists"}
    students[student_id] = student.dict()
    return students[student_id]

# put method //update the values in the body
@app.put("/update/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    if student.name:
        students[student_id]["name"] = student.name
        
    if student.age:
        students[student_id]["age"] = student.age
    
    if student.class_name:
        students[student_id]["class"] = student.class_name
        
    return students[student_id]



# delete method // deletes the student object
@app.delete("/delete/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    del students[student_id]
    return {"Message": "Student deleted successfully"}