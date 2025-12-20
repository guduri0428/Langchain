from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Srinivasulu'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10,default=5,description='A decimal value representing the cgpa of the student')


new_student = {'age': '25', 'email': 'guduri660428@gmail.com'}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict)

print("--"* 30)

student_json = student.model_dump_json()

print(student_json)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/5.StructuredOutput (main)
# $ py 3_pydantic_demo.py 
# {'name': 'Srinivasulu', 'age': 25, 'email': 'guduri660428@gmail.com', 'cgpa': 5}
# ------------------------------------------------------------
# {"name":"Srinivasulu","age":25,"email":"guduri660428@gmail.com","cgpa":5.0}
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/5.StructuredOutput (main)

# It will also do implicit type conversion