def test():
    print("함수 실행:")
    try:
        print("try 구문 실행")
        return
    except:
        print("except 구문 실행->error 발생")
    else:
        print("else 구문 실행->error가 발생하지 않음")
    finally:
        print("finally 구문 실행")
#test() 함수 호출
test()
        