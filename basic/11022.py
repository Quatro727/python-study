n=int(input())
L1=[]
L2=[]
for i in range(n):
    a,b=map(int, input().split())
    L1.append(a+b)
    L2.append([a,b])
for i in range(n):
    print(f"Case #{i+1}: {L2[i][0]} + {L2[i][1]} = {L1[i]}")