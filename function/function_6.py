'''
<제너레이터>
이터레이터를 직접 만들 때 사용하는 python의 특수한 문법 구조
함수 내부에 yield 키워드를 사용해 해당 함수를 제너레이터 함수로 만들 수 있다.
또한 제너레이터 함수는 일반 함수와 다르게 함수를 호출해도 함수 내부의 코드가 실행되지
않는다.

generator 함수는 호출하면 generator를 호출한다. generator 객체는 next() 함수를 사용해 
함수 내부의 코드를 실행한다. 이때 yield 이쿼드 부분까지만 실행한다. 
그리고 next() 함수의 return 값으로 yield 키워드 뒤에 입력한 값이 출력된다.
generator 객체는 함수를 조금씩 실행할 때 사용하는 개념이다.
'''
#제너레이터
def gene_test():
    print("A지점")
    yield 1
    print("B지점")
    yield 2
    print("C지점")
    yield 3
    print("D지점")
    yield 4
#함수 호출
ouput=gene_test()
print("<제너레이터 4회 수행>")
a=next(ouput)
print(a)
b=next(ouput)
print(b)
c=next(ouput)
print(c)
d=next(ouput)
print(d)
'''
<리스트 함수의 키워드 매개변수>
예를 들어 딕셔너리를 활용해서 책을 표현할 경우 '가격이 가장 저렴한 책'과
'가격이 가장 비싼 책'을 찾고 싶다고 하자. 이럴 때는 딕셔너리의 key를 활용하면 된다.
min(), max()에는 '어떤 값으로 비교할 것인지'를 나타내는 key라는 키워드 매개변수를 지정할 수 있다.
이를 이용해 딕셔너리에 있는 가격속성으로 최댓값과 최솟값을 비교할 수 있다.
'''
#딕셔너리에 저장된 책 중에서 MAX값과 min값 찾기
books=[{
    "제목":"전쟁론",
    "가격":18000
},{
    "제목":"군주론",
    "가격":20000
},{
    "제목":"손자병법",
    "가격":30000
}]
#가격함수
def price(book):
    return book["가격"]
#가장 비싼 책과 가장 저렴한 책을 골라서 출력
#books 리스트에서 원소 하나씩 꺼내서 key로 지정된 함수를 적용한 결과값을 기준으로 비교
#key로 지정된 함수는 딕셔너리에서 "가격"이라는 key에 배정된 값을 return한다. 
#이떼 key에 지정되는 함수를 lambda식으로 작성할 수도 있다.
print("가장 비싼 책:", max(books, key=price))#lambda book:book["가격"]
print("가장 저렴한 책:", min(books, key=price))