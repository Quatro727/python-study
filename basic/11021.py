n=int(input())
L=[]
for i in range(n):
    a,b=map(int, input().split())
    L.append(a+b)
for i in range(n):
    print(f"Case #{i+1}: {L[i]}")