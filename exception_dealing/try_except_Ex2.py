#문자열 리스트를 숫자 리스트로 바꾸기
L=["52", "456", "908", "998", "1000"]

L_num=[]
for item in L:
    try:
        float(item)
        L_num.append(item)
    except:
        pass
#출력
print(f"L 내부에 있는 숫자는 {L_num} 입니다.")