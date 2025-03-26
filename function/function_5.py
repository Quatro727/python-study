'''
텍스트를 사용하여 데이터를 구조적으로 표현할 수 있는 방법으로 CSV, XML, JSON 등이 있다.
이 중에서 CSV 파일의 텍스트를 한 줄씩 읽어보자
CSV는 쉼표로 구분된 값들을 의미한다. 한 줄에 하나의 데이터를 나타내며 각각의 줄은 쉼표를 통해 
데이터를 구분한다. 이때 첫 줄은 Header를 넣어 각 데이터가 무엇을 의미하는지 나타낼 수 있다.
'''
#랜덤한 숫자를 만들기 위한 random 모듈
import random
#간단한 리스트 생성
eng=list('abcdefghijklmnopqrstuvwxyz')
#파일을 쓰기 모드로 열고 텍스트 작성하기
with open("info.txt", "w") as file:
    for i in range(100):
        #random한 값으로 변수 생성
        name=random.choice(eng)+random.choice(eng)+random.choice(eng)
        height=random.randrange(140, 200)
        weight=random.randrange(30, 100)
        file.write(f"{name}, {weight}, {height}\n")
#파일을 한 줄씩 읽어 bmi를 계산하고 해당 인물이 과체중인지, 저체중인지 아니면 정상체중인지
#판단해보자
with open("info.txt", "r") as file:
    for line in file:
        #변수 선언하고 각 변수에 unpacking 하기기
        name, weight, height=line.strip().split(',')
        #header값인 부분은 다음 반복으로 넘어가기기
        if not weight.isdigit() or not height.isdigit():
            continue
        else:
            bmi=int(weight)/((int(height)/100)**2)
            result=""
            if 25<=bmi:
                result="overweight"
            elif 18.5<=bmi:
                result="normal weight"
            else:
                result="less weight"

        #한 줄씩 bmi 결과를 출력하기
        print(f"이름:{name}, 몸무게:{weight}, 키:{height}, 결과:{result}")