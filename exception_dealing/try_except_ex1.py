try:
    #숫자 입력
    data_input=input("숫자 입력:")
    #출력
    num_input=int(data_input)
    print(f"원의 반지름:{num_input}")
    print(f"원의 둘레:{2*3.141592*num_input}")
    print(f"원의 넓이:{num_input**2*3.141592}")
except:
    print("숫자를 입력하세요")#원의 둘레를 계산할 때 문자열은 숫자 자료형이 아니어서 오류가 발생