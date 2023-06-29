import time
import bs4
import urllib.request
import ssl
import pymysql
from tkinter import *
from tkinter import messagebox

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
# outcome, charImg, pDate, kda = "", "", "", ""
#주소 : https://www.op.gg/summoners/kr/WannabeNuguri
# 가지고올 클래스명
# sc-1ulxjc4-0 cPjXWn sc-cTAqQK hYTavo = 전적리스트(부모태그)  - div - li같은형태
# sc-1xwhuw1-0 afFmu sc-1hmh1k6-4 dIKnaT<div밑에>
#       ㄴ> 이미지 초상화 - img src로 쓰자
# buiiz7-0 d490eh-4 ikoBOt dSQenp = win/lose - span
# buiiz7-0 sc-1p49g2y-1 hNWwrq gLFnks = kda k/d/a형식으로 - span
# buiiz7-0 d490eh-3 hNWwqN cfnrzw = 몇시간전, ?, 기준을 모르겠다(하루지나면 날짜로 나옴) - span

# null = None
def insertData(outcome,charImg,pDate,kda) :
    con, cur = None, None
    data = ""
    data0, data1, data2, data3, data4 = "", "", "", "", ""
    sql=""

    con = pymysql.connect(host='127.0.0.1', user='root', password='mysql', database='lol', charset='utf8')
    cur = con.cursor()
#    title` VARCHAR(200) NULL,
#   `publisher` VARCHAR(45) NULL,
#   `newsDate` VARCHAR(10) NULL,
#   `newsTime` VARCHAR(6) NULL,
#   `newsDetail` VARCHAR(200) NULL,
#   `newsImgUrl` VARCHAR(200) NULL,
    # data0 = data10
    data1 = outcome; 
    data2 = charImg; 
    data3 = pDate; 
    data4 = kda;
    #
    try :
        
        print(null)
        print(data1)
        print(data2)
        print(data3)
        print(data4)
        
        sql = "INSERT INTO newsTable (outcome,charImg,pDate,kda)  VALUES('"+ data1 + "','" + data2 + "','" + data3 + "','" + data4 + "')"
        print("sql 실행전 ")
        cur.execute(sql)
        
    except :
        print("예외 발생")
        
        # messagebox.showerror('오류', '데이터 입력 오류가 발생함')
    else :
        print("성공")
        # messagebox.showinfo('성공', '데이터 입력 성공')
    con.commit()
    con.close()
##

checkUrl = "https://www.op.gg/summoners/kr/WannabeNuguri"
while True:
    #urllib.request 모듈을 사용하여, checkUrl로 HTTP 요청을 보내고 해당 URL에 대한 응답을 가져오는 역할
    htmlObject = urllib.request.urlopen(checkUrl,context=ssl_context)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
    tag_list = bsObject.find('div', {'class': 'content-header'})
    print(tag_list)
    print('###### 롤 내 전적보기 #######')

    for tag in tag_list:
        #승패 알려주기
        outcome = tag.find('div', {'class':'result'}).text
        print(tag)        
        # #이미지 없는 경우 처리 부분. (파이썬방식으로 작성 / null 대신  None )
        # imgLink = tag.find('div',{'class':'icon'})
        # if imgLink != None:
        #     imgLinkUrl = imgLink.find('img')['src']
        #     imgLinkUrl = 'https:' + imgLinkUrl
        # else :
        #     imgLinkUrl = '이미지가 존재 하지 않음'

        # #플레이한 날짜
        # playDate = tag.find('div', {'class':'time-stamp'}).text

        # #kda
        # kda = tag.find('div', {'class','k-d-a'}).text

        # print("데이터 추가 전")
        # print(outcome,'',imgLink,'',playDate,'',kda)

        time.sleep(60)