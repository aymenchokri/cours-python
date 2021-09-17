"""
i=int(input("enter your number: "))
while i<10:
    print(i)
    i+=1
"""
employee=["alex","jhon","stive","sandra","morgen","doe","juan"]
i=0
while (employee[i]):
    print(employee[i])
    i+=1
    if i==len(employee)-2:
        break

while 0:
    print("gfhfg")

k = 0
while k < 6:
  k += 1
  if k == 3:
    continue
  print(k)

nationality=["tunisia"," ","Syria","lebon"," "," ","UK"]

l=0
while (nationality[l]):

    if nationality[l] == " ":
        l += 1
        continue
    print(nationality[l])
    l += 1
    if l==len(nationality):
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)


for x in fruits:
  print(x)
  if x == "banana":
    break

for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x)

for x in range(2, 30, 3):
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

row = [1,2,2,4]
col = [10,15,20]

for x in row:
  for y in col:
    print(x,y)

matrix=[[1,2,3],[10,12,40],[14,52,21]]
for x in matrix:
    for y in x:
        print(y)


"""
[1,  2, 3]
[10,12,40]
[14,52,21]
"""
