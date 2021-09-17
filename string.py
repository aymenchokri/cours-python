"""chaine="hi how are you"
if "hi" in chaine:
    print("yes")
else :
    print("you cant found the letter")"""
from math import *

"""
def testexist(chaine,value):
    if value in chaine:
        print("yes")
    else:
        print("you cant found the letter")

testexist("hi hello ","yu")
"""
"""
#fuctoriel 
def fuctoriel(n):
    facotriel=1
    for i in range(n+1):
        if i !=0:
          facotriel=facotriel*i
    print(facotriel)
fuctoriel(4)
"""
""" function deriver"""
"""
lim x->a f(x)-f(a)/x-a
on pose h=x-a

lim h->0 f(a+h)-f(a)/h
"""

"""def slope(f,a,h):
    print((f(a+h)-f(a))/h)

slope(lambda x:x**2,2,0.00000000001)"""


# slice in string
"""string="ayMen"
print(string[::-1])
print(string.upper())
print(string.lower())
separateteur="/"
print(separateteur.join(['03','09','2021']))
chaine="hi how are you {name}"
print(chaine.split('h'))
print(chaine.format(name="hamza"))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

print('hello "aymen"')
print("hello\b\b\"aymen\"")
print([i for i in range(100) if i%2!=0])"""
y=[2,5,10,20,15,420]
print(list(map(lambda x:x**2,y)))
def map(f,list):
    r=[i for i in list]
    j=0
    for i in list:
        r[j]=f(i)
        j=j+1

    print(r)

map(lambda x:x**2,y)

