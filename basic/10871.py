a,b=map(int, input().split())
L1=list(map(int, input().split()))
L2=[]
for i in range(len(L1)):
    if L1[i]<b:
        L2.append(L1[i])
for i in range(len(L2)):
    print(L2[i], end=' ')