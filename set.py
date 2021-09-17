myset={1,2,3,3}
print(myset)
print(len(myset))
print(type(myset))
for x in myset:
  print(x)

print(1 in myset)
print(10 in myset)
print(1 not in myset)
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
#thisset[0]="gfdgd" # generate an error
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

a={1,2,3,4}
b={2,3,5,6,7}
print(a.difference(b))
print(b.difference(a))
print(a.union(b))
print(a.intersection(b))
print(a.remove(1))
a.discard(1)
print(a)
for x in a:
  print(x)
