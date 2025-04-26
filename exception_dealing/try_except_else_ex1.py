#try except else 구문으로 예외 처리

try:
    a,b=map(int, input().split())
except:
    print("숫자를 입력해주세요!!")
else:
    print(f"밑변:{a}")
    print(f"높이:{b}")
    print(f"넓이:{a*b}")