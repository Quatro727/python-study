#두 수를 비교하는 문제
a,b=map(int, input().split(' '))
if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('==')