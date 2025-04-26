##아직 구현되지 않은 부분에서 강제로 예외 발생시키기
#입력
num=input("정수 입력:")
num=int(num)

if num%2==1:
	#입력값이 홀수인 경우
	raise NotImplementedError
else:
	#입력값이 짝수인 경우
	raise NotImplementedError