#가변 매개변수수
'''
가변 매개변수
매개변수를 원하는 만큼 받을 수 있는 함수를 의미한다.
가변 매개변수 뒤에는 일반 매개변수가 올 수 없다
가변 매개변수 only 1개만 사용가능
'''
def print_n_times(times, *L):
    print(L)
    for i in range(times):
        for element in L:
            print(element)

#함수 호출
print_n_times(3, [1,2,3], [4,5,6,7,8])

#기본 매개변수
'''
가변 매개변수 뒤에 올 수 있는 변수. 
함수를 정의할 때 매개변수에 default 값을 set한 것
즉, 우리가 인수 없이 함수 호출 시 이 기본값이 매개변수에 전달되어 함수가 실행된다.
기본 매개변수 뒤에는 일반 매개변수가 올 수 없다.
'''
def print_n_times(value, n=2):
    #n번 반복합니다.
    for i in range(n):
        print(value)
#함수 호출->매개변수에 아무런 인수도 전달하지 않음(기본값 실행)
print_n_times("Hello Nice 2 meet u")
print()

#키워드 매개변수
'''
매개변수를 직접 지정하고 값을 할당하는 방식이다.
이럴 경우 함수를 호출할 때 따로 매개변수의 위치를 고민할 필요가 없다.
'''
def print_Hello_n(*values, n):
    for i in range(n):
        for element in values:
            print(element)
        print()
#함수 호출: 함수에 쓰인 매개변수 n을 직접 지명하여 값 3을 할당함
print_Hello_n("Hello", "nice 2 meet u", n=4)
'''
이를 통해 우리가 앞으로 함수를 호출할 때 아예 매개변수를 직접 지정하고 값을
할당하는 방식으로 호출하면 매개변수의 세세한 위치를 신경 쓸 필요가 없음을 알 수 있다.
참고로 기본 매개변수는 인수로 전달되는 값이 없을 경우에만 default값이 할당된다.
'''
def test(a, b=10, c=200):
    print(a+b+c)
test(10, 20, 30)
test(a=10, b=200, c=500)
test(b=100, c=100, a=10)
test(10)

#return
'''
함수가 실행되고 나서 최종적으로 내놓은 결과물을 반환하기 위한 구문이라고 생각하면 된다.
그리고 함수의 결괏깂을 우리는 return 값이라고 한다.
그리고 return 구문은 함수 실행을 여기서 끝내라는 의미로 받아들여도 된다.
'''
def return_example(a,b,c):
    result=a+b+c
    return result#함수의 실행은 여기까지. 그리고 return값을 호출된 위치로 되돌려줌줌
    result+=100
#함수 호출
data=return_example(10,34,8)
#함수의 return값이 변수 data에 할당됨
print(data)
    