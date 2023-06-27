num = 0
sum = 0

for i in range(0, 100, 1):
    if num%7==0 :
        sum+=num
    num += 1    

    
    
print("0부터 100까지 7의 배수 합계는 %d 입니다" %sum)



#정답지
i, hap = 0, 0

for i in range(0, 101, 7) :
    hap = hap + i
    
print("0과 100 사이에 있는 7의 배수 합계 : %d" % hap)