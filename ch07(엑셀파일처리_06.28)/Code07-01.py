import xlrd

workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')
sheetCount = workbook.nsheets #시트의 갯수 number sheet ->nsheet
print('워크시트는 %d개 입니다' % (sheetCount))

wsheetList = workbook.sheets() #시트들을 꺼내서 리스트에 담음
for worksheet in wsheetList :
    print('** 워크시트의 이름 : %s' % (worksheet.name) )
    print(" 행 수는 %d, 열 개수는 %d 입니다." % (worksheet.nrows, worksheet.ncols))
