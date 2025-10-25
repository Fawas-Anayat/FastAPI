""" by looking at the following function we can easily understand whats the issues with the data validation 
in the python as not feasible in case of the production grade high level applications

def insert_details(name:str,age:int):
    if age <0:
        raise ValueError("age cant be negative")
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
    else:
        raise TypeError('invalid datatype')

insert_details("khan",25)
insert_details("usman",34)

"""

from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
# from typing import List,Dict

class patient(BaseModel):  #this is the model means we can say that its the standard and we can use it    
    name:str               # these are te simpler datatypes and we can use the complex ones also like lists,dictionaries etc
    mail:EmailStr           # we can also make some data as optional
    url:AnyUrl
    age:int=Field(gt=0)             # here we can define the range of the field in which this data is placed       

def insert_details(patientt:patient):
    print(patientt.name)
    print(patientt.age)
    print(patientt.mail)
    print(patientt.url)
@field_validator('mail')
@classmethod
def mail_validator(cls,value):
    valid_domains=['gmail.com','gpgc.com']
    domain_name=value.split('@')[-1]
    
    if domain_name not in valid_domains:
        raise ValueError(f'not a valid domain name .choose from{valid_domains}')
    
    return value
        
personal_info={'name':'usman','mail':'abc@hu.com','age':34,'url':'http://linked.com/234'}
patient1=patient(**personal_info)
insert_details(patient1)