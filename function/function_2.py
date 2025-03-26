#재귀함수
'''
재귀(recursion)이란 자기 자신을 호출한다는 의미이다.
즉, 함수가 호출되어 함수 내부의 구문들을 실행하는 과정에서 자기 자신을 호출하는 함수를
재귀함수라고 한다. 재귀함수는 잘 쓰면 매우 유용하지만 잘못 쓰면 쓸데없는 호출로
중복 연산이 일어나 코드의 실행을 매우 느리게 한다. 이를 방지하기 위한 것 중 하나가
메모제이션 기술이다. 즉 중복 호출이 안 일어나도록 미리 메모한다는 의미이다.
'''
#재귀함수 예시: 피보나치 수열, 아마 20부터 슬슬 결과 나오기까지 오래 걸릴 것이다.
def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        result=fibo(n-2)+fibo(n-1)
        return result
#향상된 재귀함수: 메모제이션
def fibo_better(n):
    dic={
        1:1,
        2:1
    }
    if n in dic:
        return dic[n]
    else:
        result=fibo(n-2)+fibo(n-1)
        dic[n]=result
        return result

#2차원 리스트 1차원 리스트로 만들기
def flatten(L):
    output=[]
    for element in L:
        if type(element)==list:
            output.extend(element)
    return output
#고차원 리스트 1차원 리스트로 만들기->재귀의 개념 이용하기
def advanced_flatten(L):
    output=[]
    for element in L:
        if type(element)==list:
            output.extend(advanced_flatten(element))
        else:
            output.append(element)
    return output
L=[[1,2,3],[4,[5,6],7],[8,9,10]]
print(advanced_flatten(L))