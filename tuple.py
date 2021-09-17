a=("orange",1,"banana",2,"mango")
print(a,len(a))
print(a[0])
print(type(a))
print(a[:2])
print(a[1:])
for i in a:
   if type(i) == str:
        print(i)

y=list(a)
print(y)
y.append(10)
a=tuple(y)
print(a)

a=("gdfg","fgdfg","fdg","fdgd","fd","g","fd")
y=("ddgz","zdedfde")
y+=a
print(y)
g=("banana","banana","banana","apple","cherry")
a,*_=g
print(*_)
print(g.count("banana"))
print(g.index("banana"))