def insert_details(name:str,age:int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
    else:
        raise TypeError('invalid datatype')

insert_details("khan",23)
insert_details("usman",34)