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

