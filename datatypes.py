import random
name='aymen'

def function():

    name="alex"
    print(name)

function()
print(name)  # we have to variables with the same name and different content
"""Second example """
name1='aymen'

def function():
    global name1
    name1="alex"
    print(name1)

function()
print(name1)


""" Data types """
varible="aymen"
print(varible,type(varible))
varible=5
print(varible,type(varible))
varible=5.0
print(varible,type(varible))
varible=5j
print(varible,type(varible))

for i in range(10):print("hi")
# retrun n times 10
print("aymen"*10)
#List Ordered changeable
array=[1,2,3,4,5,1,1,2,2]
print(array)
array[0]=10
print(array[0],array[1])
print(array)
#Tuple Ordered Unchangeable
array=(1,2,3,4,5,1,1,2,2)
print(array)
#array[0]=10
print(array)
#Set Unordered Unchangeable
array={1,2,3,4,1,1,1,1,5}
print(array)
#dictionary
car={
    "name":"lamberguini",
    "color":"red",
    "year":1970
}
print(car["year"],type(car["year"]))

# string
#name="aymen"
name=str("aymen")
print(name)
#int
#number=20
number=int(20)
print(number)
x = dict(name="John", age=36)
print(x)

x=bool(5)
print(x)
x=bool("ghfgjughk")
print(x)
x=bool(0)
print(x)
x=bool("")
print(x)
