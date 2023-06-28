#기본인코딩 ANSI로 되어있어서 해당 csv파일 확인할때는 메모장으로 확인
inFp = open("C:/CookAnalysis/CSV/singer1.csv", "r")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()