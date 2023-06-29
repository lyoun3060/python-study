from tkinter import *
import xlsxwriter
window = Tk()
photo = PhotoImage(file = 'C:/CookAnalysis/GIF/pic7.gif')
h = photo.height()
w = photo.width()


#이중for문을 다르게 적는법임
# photoR = []
# for _ in range(w):
#     row = []
#     for _ in range(h):
#         row.append(0)
#     photoR.append(row)
photoR=[ [0 for _ in range(h)] for _ in range(w)]
photoG=[ [0 for _ in range(h)] for _ in range(w)]
photoB=[ [0 for _ in range(h)] for _ in range(w)]

for i in range(w) :
    for k in range(h) :
        r, g, b = photo.get(i,k)
        photoR[i][k] = r
        photoG[i][k] = g
        photoB[i][k] = b
#이미지의 각 픽셀의 RGB 색상 코드를 가져오는 작업 
#이미지 -> 메모리        =  입력

#여기 밑의 절대 경로에 엑셀 파일 형식으로 쓰기작업
#메모리-> 파일          = 출력
workbook = xlsxwriter.Workbook('C:/CookAnalysis/Excel/pic7_0629.xlsx')
worksheetR = workbook.add_worksheet('photoR')
worksheetG = workbook.add_worksheet('photoG')
worksheetB = workbook.add_worksheet('photoB')

for i in range(w) :
    for k in range(h) :
        worksheetR.write(i, k, photoR[i][k])
        worksheetG.write(i, k, photoG[i][k])
        worksheetB.write(i, k, photoB[i][k])

workbook.close()
print('Save. OK~')