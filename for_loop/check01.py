#list 생성
L=[0,'저녁 운동', 4, 99, 76, '아침밥']
   
#확인 문제
for item in L:
    #접근한 요소의 type이 string일 때때
    if type(item)==str:
        print(type(item), item[1])#1번째 요소 출력
    
 
    