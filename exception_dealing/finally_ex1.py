try:
    #파일을 쓰기 모드로 연다.
    file=open("test.txt", "w")
    #여러 가지 처리 수행
    예외발생
    #파일 닫기
    file.close()
except:
    print("error 발생")
finally:
    file.close()
print("파일이 제대로 닫혔습니까?(True/False)", file.closed)