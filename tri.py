n=5
for i in range(n):
    for j in range(i+1):
        print("@ ",end="")
    print("\r")

a="hello there how are you"

print(a)
print(a,a,a,sep="/",end=" 1",flush=True)
