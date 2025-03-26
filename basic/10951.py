L=[]
try:
    while True:
        a,b=map(int, input().split())
        L.append(a+b)
except:
    pass
for i in range(len(L)):
    print(L[i])
    
    