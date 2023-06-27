check = input("문자열을 입력하세요")

if check.isdigit() :
    print("숫자 입니다.")
elif check.isalpha() == True:
    print("한글 + 영어 입니다.")
elif(check.isalnum() == True):
    print("글자1 + 숫자 입니다.")