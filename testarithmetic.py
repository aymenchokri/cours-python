from arithmetic import *
somme(10,200,20,54)
multiplication(1021,54,85588)
soustraction(65948,2587,5425847)
division(587,441458747)

l=list({1,2,3,4,4})
print(l)

list=[1,2,3,4,5,6]

copylist=[i for i in list]
print(copylist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
import math
from random import *

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
n=[]
for i in fruits:

    if i!="banana":
        n.append(i)
    elif i=="banana":
        n.append("orange")
print(n)

p=[(x,x,x,x) for x in range(math.ceil(random()*10))]

print(p)
print(len(p))





