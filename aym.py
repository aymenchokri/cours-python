a=["a","b","c"," ","d"]
l=0
while a[l]:
    if a[l]==" ":
        l=l+1
        continue
    print(a[l])
    l+=1
    if l==len(a):
        break