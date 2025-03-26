'''
tuple: 리스트와 유사한 자료형. 리스트와는 다르게 1번 결정된 요소는 변경이 불가
lambda: 함수를 간단하고 쉽게 선언하는 방법. 1회용 함수를 만들어야 할 때 보통 사용
'''
#tuple의 특이한 할당 구문
tuple=10, 20, 30, 40, 50
print("괄호가 없는 튜플의 값과 자료형 출력")
print("tuple:",tuple)
print("type(tuple):",type(tuple))
print()
#괄호가 없는 튜플 활용
a,b,c=10, 20, 30#튜플은 괄호를 생략해도 tuple로 인식할 수 있는 경우 괄호 생략이 가능하다.
print("괄호가 없는 튜플을 이용한 할당")
print("a/b/c", a,b,c,sep='/')
#이러한 튜플의 특징을 이용하여 변수의 값을 교환할 수 있다.
print(f"교환 전 값:a={a}, b={b}")
a,b=b,a
print(f"교환 후 값:a={a}, b={b}")
#또한 괄호 생략의 특징을 이용하여 여러 개의 값을 반환하여 받을 수 있다.
def test():
    return (10, 20)
a,b=test()
print(f"a:{a}, b:{b}")
#즉, tuple은 괄호 없이 여러 개의 값을 할당할 수 있다는 점이다.

'''
함수라는 기능을 매개변수로 전달하는 코드를 사용하는 경우가 많다. 이때 함수의 매개변수에 사용하는 
함수를 callback 함수라고 한다.
'''
#콜백함수
def call_10_times(func):
    for i in range(10):
        func()
def print_hello():
    print("Hello!")
call_10_times(print_hello)
#filter() 함수: 
# 리스트의 요소를 함수에 넣고 return된 값이 True인 것으로만 새로운 리스트를 구성
#형식(함수, 리스트)
#이때 주의해야 할 점이 filter() 함수의 return값은 iterator 객체이므로 일반 리스트처럼 indexing이 불가능하다
def power(item):
    return item*item
def under_3(item):
    return item<3
list_input=[1,2,3,4,5]
output_a=filter(under_3, list_input)
print(output_a)
print(list(output_a))
#map(함수, 리스트)
#리스트의 요소를 함수에 넣고 return된 값으로 새로운 리스트를 구성하는 함수
output_b=map(power, list_input)
print(output_b)
print(list(output_b))
#lambda 함수의 개념-> 가장 간단학 함수를 선언하는 방법
#기본 형태-> lambda 매개변수: return 값
power_3=lambda x: x*x*x
under_5=lambda y:y<5

output_a=filter(under_5, list_input)
print(output_a)
print(list(output_a))
output_b=map(power_3, list_input)
print(output_b)
print(list(output_b))
#위의 코드를 더 간략하게 하여 설정이 가능하다.
output_a=filter(lambda y:y<4, list_input)
print(output_a)
print(list(output_a))
output_b=map(lambda x:x**4, list_input)
print(output_b)
print(list(output_b))