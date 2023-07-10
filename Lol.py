import time
import bs4
import urllib.request
import ssl
import pymysql
import sys
import re
 #주의사항, 문자열 안에 특수문자 부분 체크 잘하기.
 #현재 네이트 기사는 특정 시간 예 1분마다 새로운 기사가 나옴.
 #그래서, 현재 페이지에 1페이지에서 20개 기사만 디비에 저장하기로 함. 
 # 특정 시간 time.sleep(300), 5분정도 인터벌을 두고 저장하기로 함. 
 #예스24는 한페이지의 상품이 고정,
 # 뉴스는 실시간으로 계속 생성됨. 
from tkinter import *
from tkinter import messagebox

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
title, newImg, pDate, textCheck = "", "", "", ""

null = None
def clean_text(inputString):
      text_rmv = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', ' ', inputString)
      return text_rmv

def insertData(title,bookImg,pDate,textCheck) :
    con, cur = None, None
    data = ""
    data0, data1, data2, data3, data4 = "", "", "", "", ""
    sql=""

    con = pymysql.connect(host='127.0.0.1', user='root', password='mysql', database='yes24korea', charset='utf8')
    cur = con.cursor()
#    title` VARCHAR(200) NULL,
#   `publisher` VARCHAR(45) NULL,
#   `newsDate` VARCHAR(10) NULL,
#   `newsTime` VARCHAR(6) NULL,
#   `newsDetail` VARCHAR(200) NULL,
#   `newsImgUrl` VARCHAR(200) NULL,
    # data0 = data10
    data1 = title; 
    data2 = bookImg; 
    data3 = pDate; 
    data4 = textCheck;
    #
    try :
        
        print(null)
        print(data1)
        print(data2)
        print(data3)
        print(data4)
        
        sql = "INSERT INTO yes24table (title, bookImg, pDate, textCheck)  VALUES('"+ data1 + "','" + data2 + "','" + data3 + "','" + data4 + "')"
        print("sql 실행전 ")
        cur.execute(sql)
        
    except  Exception as e:
        print("예외 발생", e)
        print("예외",  sys.exc_info())
        
        # messagebox.showerror('오류', '데이터 입력 오류가 발생함')
    else :
        print("성공")
        # messagebox.showinfo('성공', '데이터 입력 성공')
    con.commit()
    con.close()
##

pageNumber = 1
checkUrl = "https://www.yes24.com/24/Category/Display/001001046001?ParamSortTp=05&PageNumber="

while True:
    bookUrl = checkUrl +  str(pageNumber)
    pageNumber+=1
    #urllib.request 모듈을 사용하여, checkUrl로 HTTP 요청을 보내고 해당 URL에 대한 응답을 가져오는 역할
    htmlObject = urllib.request.urlopen(bookUrl,context=ssl_context)
    webPage = htmlObject.read()
    #bs4 = 가져온 데이터를 보기좋게 꾸며줌
    bsObject = bs4.BeautifulSoup(webPage, 'html.parser')    
    tag_list = bsObject.findAll('ul', {'class': 'clearfix'})

    print('###### 책 리스트 보기 #######')
    
    for tag in tag_list:

        title = tag.find('div',{'class':'goods_name'}).find('a').text
        title = clean_text(title)        
        
        bookImgcheck = tag.find('p',{'class':'goods_img'})
        #이미지 없는 경우 처리 부분. 파이썬 null 대신  None 
        if bookImgcheck != None:
            bookImg = bookImgcheck.find('img')['src']
            bookImg = 'https:' + bookImg
        else :
            bookImg = '이미지가 존재 하지 않음'
        
        pDate = tag.find('span', {'class':'goods_date'}).text

        textCheck = tag.find('div',{'class':'goods_read'}).text
        textCheck = clean_text(textCheck).lstrip()
        


        insertData(title,bookImg,pDate,textCheck)
    #time.sleep(1)
        
    