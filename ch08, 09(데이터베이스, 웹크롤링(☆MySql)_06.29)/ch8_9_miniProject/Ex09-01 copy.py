import time
import bs4
import urllib.request
import ssl
import pymysql
from tkinter import *
from tkinter import messagebox

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
imgLinkUrl,subject,link ,press,pDate,pTime= "","","","","",""

null = None
## 함수 선언 부분
def insertData(subject,press,pDate,pTime,link,imgLinkUrl) :
    con, cur = None, None
    data = ""
    data0, data1, data2, data3, data4, data5, data6 = "", "", "", "", "", "",""
    sql=""

    con = pymysql.connect(host='127.0.0.1', user='root', password='mysql', database='nateNewsLive', charset='utf8')
    cur = con.cursor()
#    title` VARCHAR(200) NULL,
#   `publisher` VARCHAR(45) NULL,
#   `newsDate` VARCHAR(10) NULL,
#   `newsTime` VARCHAR(6) NULL,
#   `newsDetail` VARCHAR(200) NULL,
#   `newsImgUrl` VARCHAR(200) NULL,
    # data0 = data10
    data1 = subject; 
    data2 = press; 
    data3 = pDate; 
    data4 = pTime;
    data5 = link;
    data6 = imgLinkUrl;
    #
    try :
        
        print(null)
        print(data1)
        print(data2)
        print(data3)
        print(data4)
        print(data5)
        print(data6)
        sql = "INSERT INTO newsTable (title,publisher,newsDate,newsTime,newsDetail,newsImgUrl)  VALUES('"+ data1 + "','" + data2 + "','" + data3 + "','" + data4 + "','"+ data5 +"','"+data6+ "')"
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
page = 1
nateUrl = "https://news.nate.com/recent?mid=n0100&page="
while True :
    newsUrl = nateUrl + str(page)
    page += 1
    htmlObject = urllib.request.urlopen(newsUrl,context=ssl_context)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
    
    tag_list = bsObject.findAll('div', {'class': 'mlt01'})

    print('###### 실시간 뉴스 속보 #######')
    
    for tag in tag_list :

#strong -> h2 변경 230629 (확인 날짜)
        subject = tag.find('h2', {'class': 'tit'}).text
        
        link = tag.find('a', {'class': 'lt1'})['href']
        link = 'https:' + link

        imgLink = tag.find('em',{'class':'mediatype'})
        #이미지 없는 경우 처리 부분. 파이썬 null 대신  None 
        if imgLink != None:
            imgLinkUrl = imgLink.find('img')['src']
            imgLinkUrl = 'https:' + imgLinkUrl
        else :
            imgLinkUrl = '이미지가 존재 하지 않음'
            
        pressAndDate = tag.find('span', {'class': 'medium'}).text
        pressAndDate.replace('\t',' ')
        pressAndDate.replace('\n', '')

        if len(pressAndDate.split()) == 3 :
            press, pDate, pTime = pressAndDate.split()
        elif len(pressAndDate.split()) == 4 :
            press1,press2, pDate, pTime = pressAndDate.split()
            press = press1+press2
        else :
            continue
        print("데이터 추가 전")
        insertData(subject,press,pDate,pTime,link,imgLinkUrl)
        print('(' , page, ')', subject)
        print('\t https:'+link, press, pDate, pTime)
        print('\t imgLink : '+ imgLinkUrl)
        

    time.sleep(60)