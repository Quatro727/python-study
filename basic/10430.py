#(A+B)%C는 왜 ((A%C)+(B%C))%C와 같을까?
#(AxB)%C는 왜 ((A%C)x(B%C))%C와 같을까?
a,b,c=map(int, input().split(' '))
print((a+b)%c)
print(((a%c)+(b%c))%c)
print(a*b%c)
print(((a%c)*(b%c))%c)