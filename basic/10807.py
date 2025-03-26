a=int(input())
L=[]
L=list(map(int,input().split()))
b=int(input())
cnt=0
for i in range(len(L)):
    if L[i]==b:
        cnt+=1
print(cnt)