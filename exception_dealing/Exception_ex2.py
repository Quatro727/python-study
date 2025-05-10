L=[1,2,3,4,5,6,7,8,9]
#try except구문으로 예외 처리
try:
	#정수 입력
	num_input=int(input("정수 입력: "))
	#처리
	print(f"L의 {num_input}번째 요소={L[num_input]}")
#ValueError 발생하는 경우	
except ValueError as exception:
	print("값을 잘못 입력하셨습니다. 정수를 입력해주세요!")
	print("exception:", exception)
#IndexError 발생하는 경우
except IndexError as exception:
	print("리스트의 범위를 벗어났습니다. 다시 입력해주세요")
	print("exception:", exception)