# passage par valeur
x=10
def function(x):
    x = 20
    return x

y=function(x)

print(y)
print(x)
# passage par reference
list=["aymen","ali","saber","sami"]
def function1(l):
    l[0]="hamza"
    print(l)

function1(list)