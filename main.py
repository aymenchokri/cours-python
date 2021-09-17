"""x=2+3j
print(type(x))
print(x.imag)
print(x.conjugate())"""
array=[1,2,3,'hello','aymen',3.2]
"""print(type(array))
print(len(array))
print(type("hello"))"""
for index in array:
    if type(index)==str:
        print(index)

"""a,b,c,d,e,f=array
_,b,*_=array
print(b)
string="hello there"
for index in string:
    print(index)
# create function in python
 create funtion in in python 
def myFunction():
    print('hello there')

myFunction()

function for adding to numbers"""

def addinumber(*args):
    res=1
    for i in args:
        res=res*i
    print(res)
addinumber(21,545)