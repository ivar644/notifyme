from django.shortcuts import render
from django.http import HttpResponse
import requests,time,smtplib
from bs4 import  BeautifulSoup
from notify_run import Notify
from datetime import datetime
url=""
email=""
dp=0
product=""
def home(request):
    return render(request,'home.html')
def productdetail(request):
    return render(request,'product.html')
def checkprice(request):
    global url,email,dp,product
    u=request.GET['url']
    url=u+url
    e=request.GET['email']
    email=e+email
    p=request.GET['price']
    dp=int(p)
    pr=request.GET['product']
    product=pr
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    def check_price():
        URL=url
        page = requests.get(URL, headers=headers)
        soup= BeautifulSoup(page.content,'html.parser')
        '''
        m=open('soupw.txt',"wb")
        m.write(soup.prettify().encode("utf-8"))
        m.close
        '''
        
        title = soup.find(id="productTitle").get_text()
        pric = soup.find(id="priceblock_dealprice")
        if pric:
            xy=0
        else:
            pric = soup.find(id="priceblock_ourprice")
        price=pric.get_text()
        main_price = price[2:]
        
        l = len(main_price)
        if l<=6 :
            main_price = price[2:5]
        else:
            p1 =  price[2]
            p2 =  price[4:7]
            pf = str(p1)+str(p2)
            main_price = int(pf)
            
        price_now = int(main_price)
        title1=str(title.strip())
        main_price1 = main_price
        ''''print("NAME : "+ title1)
        print("CURRENT PRICE : "+ str(main_price1))
        print("DESIRED PRICE : "+ str(dp))
        '''
        
        #count = 0
        if(price_now <= dp):
            send_mail()
            #push_notification()
        '''else:
            count = count+1
            print("Rechecking... Last checked at "+str(datetime.now()))'''
        
    
    def send_mail():
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('ravipatidar644@gmail.com','7221019969')
        subject = "Price of "+product+" has fallen down below Rs. "+str(dp)
        body = "Hey Manku! \n The price of "+product+" on AMAZON has fallen down below Rs."+str(dp)+".\n So, hurry up & check the amazon link right now : "+url
        msg = f"Subject: {subject} \n\n {body} "
        server.sendmail(
        'ravipatidar644@gmail.com',
        email,
        msg
        )
        #print("HEY AMLAN, EMAIL HAS BEEN SENT SUCCESSFULLY.")
        
        server.quit()
    '''
    def push_notification():
        notify = Notify()
        notify.send(pnmsg)
        print("HEY RAVI, PUSH NOTIFICATION HAS BEEN SENT SUCCESSFULLY.")
    '''    
        #print("Check again after an hour.")
    
    #count = 0
    check_price()
    return render(request,'home.html')
# Create your views here.
