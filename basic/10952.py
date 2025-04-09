L=[]
while True:
    a,b=map(int, input().split())
    if a==0 and b==0:
        break
    L.append(a+b)
for i in range(len(L)):
    print(L[i])