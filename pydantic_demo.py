from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class student(BaseModel):
    name:str
    age:Optional[int]=None
    email:EmailStr
    marks: float =Field(gt=0,lt=100,default=0,description='marks student got')

new_student={
    'name':'pranav','age':'22', 'email':'shh@gmail.com','marks':10
}
st=student(**new_student)
print(st)

# Can convert it into json or python dictionary
st_dict=dict(st)
print('pythin dictionary:',st_dict)

st_json=st.model_dump_json()
print('json:',st_json)