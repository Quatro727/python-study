'''
파이썬에는 크게 2가지의 자료형이 있다.
1)기본 자료형: 숫자, 문자열, bool
2)객체 자료형: 기본 자료형을 제외한 모든 자료형들(리스트, 튜플, 딕셔너리...)

각 자료형들은 선언될 때 저장되는 방식이 다르다.
기본 자료형->stack이라는 창고에 저장된다.
객체 자료형->heap이라는 거대한 창고에 저장 후 이들의 위치를 stack에 저장
이때 창고의 위치에 대한 정보를 address 또는 reference라고 한다.

python은 함수 호출 시, 함수 내부 코드 실행을 위해 함수 내부의 변수를 저장할 stack을
추가로 만들고 함수의 실행이 끝나면 그 함수의 스택을 삭제한다.
'''
#기본 자료형 복사
def primitive_change(b):
    b=20
a=10
print(a)#10
primitive_change(a)
print(a)#10->a의 값이 그대로 b로 가는 것이 아닌 복사되어 b에 할당되는 방식
'''
리스트->객체 자료형->선언 시 heap에 저장된고 그 위치가 stack에 저장
아래 예시에서 object_change()가 호출되면 변수 b는 결국 stack의 a의 위치를 가리키고
b.append(4)가 실행되면서 stack의 주소를 따라 heap의 리스트가 [1,2,3,4]로 변경된다.
이후에 함수 object_change()의 호출이 끝나면서 함수 스택이 사라지면서 변수 b도 사라진다.
이때 변수 a는 여전히 스택의 리스트 주소를 가리키고 있고 heap에는 [1,2,3,4]로 변경된 상태이다.
따라서 함수 호출 시에는 단순히 자료형이 객체인지, 기본인지를 넘어서 선언될 때 stack방식인지, heap방식인지도 같이 고려해야 한다.

'''
#객체 자료형 복사
def object_change(b):
    b.append(4)
a=[1,2,3]
print(a)#[1,2,3]
object_change(a)#
print(a)#[1,2,3,4]

