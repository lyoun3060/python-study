# aa = [0, 0, 0, 0]
# hap = 0

# aa[0] = int(input("1번째 숫자 : "))
# aa[1] = int(input("2번째 숫자 : "))
# aa[2] = int(input("3번째 숫자 : "))
# aa[3] = int(input("4번째 숫자 : "))

# hap = aa[0] + aa[1] + aa[2] + aa[3]

# print("합계 ==> %d" % hap)

bb= [0, 0, 0, 0, 0]
i = 0

for i in range (0,5,1) :
    bb[i]=i #<- 이렇게 쓰려면 0이라는 값이 들어가 있어야 바꿀수 있음 
    #bb=[]라고 선언되있는 경우에는 append를 사용해야 순차적으로 들어감
    

print(bb)