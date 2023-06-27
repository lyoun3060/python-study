num1=int(input("첫 번째 수를 입력하세요"))
num2=int(input("두 번째 수를 입력하세요"))
calc=input("계산하고 싶은 기호를 입력하세요")


def calcurator(num1, calc, num2) :
    result = 0
    if calc == '+':
        result =num1 + num2

    elif calc =='-':
        result =num1 - num2

    elif calc =='*':
        result =num1 * num2

    elif calc =='/':
        if(num2==0):
            return
        else:
            result =num1 / num2

    elif calc =='**':
        result =num1 ** num2

    return result

if calc=='/' and num2 ==0:
    print("0으로는 나눌 수 없습니다.")
else:
    print("%d %c %d =" %(num1, calc, num2), end=" "),

    print("정답은 %d입니다" %calcurator(num1, calc, num2))
