"""print("Entrer un numero")
a=int(input("a: "))
b=int(input("b: "))
if b<a:
    print(b,"is < than", a)
elif b>a:
    print(b,"is > than", a)
else:
    print(b,"is equal to",a)
"""
"""
a=15
b=15
if b>a: print(b,"is greater than",a)

print(b,"is lower than ",a)if b<a else print(a,"is lower than ",b) if a<b else print (a,"=",b)
"""
"""
namebase="alex"
lastnamebase="smith"

name=str(input("Enter your name: "))
lastname=str(input("Enter your lastname: "))
if name!=namebase or lastname!=lastnamebase:
    print("you are not aloud to connect")
else:
    print("connected successfully")
"""

namebase="alex"
lastnamebase="smith"
emailbase="alexsmith123@gmail.com"
telbase="20214215"

name=str(input("Enter your name: "))
lastname=str(input("Enter your lastname: "))

if name!=namebase or lastname!=lastnamebase:
    print("you are not aloud to connect")
else:
    print("to continue to the web site ")
    print("please enter your email or telphone: ")
    id = str(input("email/phone: "))
    if(id==emailbase or id==telbase):
        print("you are connected ")

a=10
b=9
if a>b:
    pass
