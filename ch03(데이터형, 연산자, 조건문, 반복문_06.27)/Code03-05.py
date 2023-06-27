money, c500, c100, c50, c10 = 0,0,0,0,0

money = int(input("교환할 돈은 얼마인가요?"))

c500 = money//500
money %= 500

c100= money //100
money %= 100

c50 = money // 50
money %= 50

c10= money // 10
money %= 10

if money>10:
    if money >=5 and money<9:
        print("b")
    elif money>5 and money>1:
        print("c")
elif money>0:
    print("b")


print("500원 짜리 %d 개" %c500)
print("100원 짜리 %d 개" %c100)
print("50원 짜리 %d 개" %c50)
print("10원 짜리 %d 개" %c10)
print("바꾸지 못한 돈 %d 원" %money)
