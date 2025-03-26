print("----프로그램 시작----")

while True:
    try:
        print("try 구문 실행")
        break#예외가 발생하지 않음->while문 빠져나감
        print("try 구문의 break 키워드 뒤 실행")
    except:
        print("except 구문 실행->error 발생")
    finally:
        print("finally 구문 실행")
    print("while문의 마지막 문장")
print("프로그램 종료")