#3차원 중첩 리스트 생성clea
list_3_dimensional=[[[1,2],[3,4]],[[5,6],[7]],[[8,9],[10]]]

#반복문 한 번만 적용
for element in list_3_dimensional:
    print(element)
print()

#반복문 2개를 중첩하여 적용
for element1 in list_3_dimensional:
    for element2 in element1:
        print(element2)
print()

#반복문 3개를 중첩하여 적용
for element1 in list_3_dimensional:
    for element2 in element1:
        for element3 in element2:
            print(element3)
print()