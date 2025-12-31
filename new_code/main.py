from fastapi import FastAPI ,HTTPException
from typing import Optional
from pydantic import BaseModel

# Dummy student data for practice
students = [
    {
        "id": 1,
        "name": "Fawas Anayat",
        "age": 22,
        "grade": "A",
        "city": "Mansehra"
    },
    {
        "id": 2,
        "name": "Ali Khan",
        "age": 21,
        "grade": "B",
        "city": "Islamabad"
    },
    {
        "id": 3,
        "name": "Sara Ahmed",
        "age": 23,
        "grade": "A",
        "city": "Lahore"
    },
    {
        "id": 4,
        "name": "Hassan Ali",
        "age": 20,
        "grade": "C",
        "city": "Karachi"
    },
    {
        "id": 5,
        "name": "Ayesha Iqbal",
        "age": 22,
        "grade": "B",
        "city": "Peshawar"
    }
]



app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

@app.get('/about')
def about():
    return {
        'name':'Fawas Anayat',
        'Grade':12,
        'city':'Mansehra'
    }

@app.get('/studentData/{student_id}')
def student_data_by_id(student_id:int):
    for id in students:
        if student_id == id['id']:
            return id
    raise HTTPException(status_code=404,detail='student not found')

@app.get('/students')
def students_filtering(name:Optional[str]=None,city:Optional[str]=None,grade:Optional[str]=None):
    results=students
    if name:
        results=[s for s in results if name.lower() in s['name'].lower()]
    
    if grade:
        filtered_students=[]
        for std in results:
            if grade.upper() == std['grade'].upper():
                filtered_students.append(std)
        results=filtered_students

    if city:
        results=[ct for ct in results if city.lower() in ct['city'].lower()]
    return results

class std(BaseModel):
    id:int
    name:str
    age:int=18
    city:str
    grade:Optional[str]=None


@app.put('/updateStudents/{student_id}')
def update_student(student_id:int , student:std):
    for i,j in enumerate(students):
        if student_id == j['id']:
            student[i]=student.dic()
            return {'message':'student updated','student':student}
        return HTTPException(status_code=404,detail='student not found')

@app.post('/addStudents')
def addStd(student:std):
    for i in students:
        if student.id == i['id']:
            raise HTTPException(status_code=400,detail='student alreay present')
    students.append(student.dict())
    return {'message':'student added','student':student}
