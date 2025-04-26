#try except 구문으로 예외를 처리
try:
    #숫자로 변환
    korean, math, english=map(int, input("국어 수학 영어 순으로 점수를 입력하세요\n").split(' '))
    #출력
    total=korean+math+english
    avg=total/3
    print(f"국어:{korean}, 수학:{math}, 영어:{english}")
    print("총점:{}, 평균:{}".format(total, avg))
#예외가 발생하면 다 아래 구문으로 처리
#예외의 종류를 처리하기 위해 어떤 타입의 에러가 났는지 파악
except Exception as exception:
    #예외 객체 출력
    print("type(exception):", type(exception))
    print("exception:", exception)

    