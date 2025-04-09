import sys
n=int(sys.stdin.readline())
L=[]
for i in range(n):
    a,b=map(int, sys.stdin.readline().split())
    L.append(a+b)
for i in range(n):
    print(L[i])