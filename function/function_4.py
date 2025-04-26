'''
python은 파일과 관련된 처리를 하는 함수가 기본으로 제공된다. 
파일은 크게 text 파일과 binary 파일로 나뉜다.
파일을 처리하려면 파일 열기를 해야 한다. 파일을 열면 파일 읽기, 쓰기를 할 수 있다.
'''
#파일 열고 닫기
#파일을 열 open() 함수를 이용한다.
#기본 형식-> 파일 객체=open(문자열: 파일 경로, 문자열:읽기 모드)
#파일 쓰기 모드로 열기기
file=open("basic.txt", "w")
#파일에 텍스트 쓰기
file.write("Hello Python Programming")
#파일 닫기
file.close()

#with 키워드
#with 구문을 사용해 close() 함수 사용하지 않기
#with 구문을 사용하면 with 구문이 끝나면서 파일이 자연스럽게 종료된다.
with open("basic.txt", "a") as file:
    #파일에 텍스트 쓰기
    file.write("\nNice to meet u")
    
#텍스트 읽기-> read() 함수를 이용하여 읽는다
#파일 객체.read()
with open("basic.txt","r") as file:
    #파일의 텍스트 읽기
    contents=file.read()#파일의 텍스트를 읽고 이것을 변수 contents에 할당당
print(contents)

