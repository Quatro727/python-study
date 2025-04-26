L=[1,2,3,4,5,6]

#try except구문으로 예외를 처리
try:
	#숫자 입력
	num_input=int(input("정수 입력: "))
	#리스트의 요소를 출력
	print(f"{num_input}번째 요소:{L[num_input]}")
	예외.발생()
except ValueError as exception:
	#ValueError 발생
	print("정수를 입력해주세요!")
	print(type(exception), exception)
except IndexError as exception:
	#IndexError 발생
	print("리스트의 인덱스의 범위를 벗어났습니다!")
	print(type(exception), exception)