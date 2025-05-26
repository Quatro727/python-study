#예제1
a=[1,2,3]
b=[*a,4,5]
print(b)

#예제2
def func(x,y,z):
    print(x,y,z)
args=[10,20,30]
func(*args)

#예제3:딕셔너리 전개 연산자 **
dict1={'a':1, 'b':2}
dict2={'b':3, 'c':4}
merged={**dict1, **dict2}
print(merged)
#딕셔너리에 전개 연산자를 적용할 때는 **를 적용을 한다. 
# **를 적용을 할 경우 키-값 쌍의 형태로 펼쳐진다.
#주의할 점은 딕셔너리에 전개 연산자를 적용할 때는 함수를 호출할 때 아니면 딕셔너리로 다시 감쌀 경우이다.

#예제4: tuple에 전개 연산자를 적용한 경우
a=[1,2]
b=(3,4)
c=[*a, *b]
print(c)
#tuple도 list와 마찬가지로 전개 연산자를 적용할 경우 그대로 펼쳐진 형태로 나온다.(값이 list 형태가 되는 것은 아니다.)

#예제5: * 연산을 2번 적용시키는 예제
def print_info(*args, **kwargs):
    print("ARGS:",args)
    print("KWARGS:", kwargs)
positional=(1,2,3)
keyworded={'name':'Alice', 'age':30}
print_info(*positional, **keyworded) 
#함수 호출 시 * 연산을 적용 시키면 전개해서 인수로 전달하는 것이고
#함수 정의에서 매개변수에 *연산을 적용 시키면 다시 묶어서 받는 다고 생각하면 된다.
#이때 함수 정의에서 * 연산은 항상 tuple 형태로 묶어서 받는다.(참고로 **연산은 always 딕셔너리로 묶어서 받는다. 왜냐하면 **연산을 적용시키는 자료향은 딕셔너리 밖에 없다)