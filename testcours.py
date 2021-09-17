person={"name":"aymen",
        "age":18,
        "job":"student",
        "natonality":"tunisian"}
print(person.keys())
print(person.values())
for i in person.keys():
        print(i)
for i in person.values():
        print(i)
print(person.items())
for i,j in person.items():
        print(i,j)

person.update(Class="4 eme")
person["hobbies"]="sports"
print(person)
del person["hobbies"]

        
        
