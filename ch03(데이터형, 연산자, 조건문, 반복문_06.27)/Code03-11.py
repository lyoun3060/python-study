import random

numbers=[]
for num in range(0, 10) :
    #append : 배열에 삽입하는것 -> numbers라는 리스트에 하나씩 0~9까지 숫자 중 하나씩 임의로 삽입 중
    numbers.append(random.randrange(0, 10)) 

print("생성된 리스트", numbers)
	
for num in range(0, 10) :
    if num not in numbers :
        print("숫자 %d는(은) 리스트에 없네요." %num)	
