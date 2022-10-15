import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notifyme.settings')
django.setup()
from productdetail.models import productdetails
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from bs4 import  BeautifulSoup
import requests,time,smtplib
from datetime import datetime
def check_price(url,dp,email,id):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    if url.count("amazon"):
        driver=webdriver.Chrome(executable_path='C:/Users/Ravi Patidar/Downloads/chromedriver.exe')
        driver.get(url)
        timeout=30
        try:
            WebDriverWait(driver,timeout).until(ec.visibility_of_element_located((By.ID,"productTitle")))
        except TimeoutException:
            driver.quit()
        title = driver.find_element(By.ID,"productTitle").text
        try:
            pric = driver.find_element(By.ID,"priceblock_ourprice")
        except:
            pric = driver.find_element(By.ID,"priceblock_dealprice")
        price1=pric.text
        s=price1[2:]
        st=""
        l=list(s.split(','))
        price=float(st.join(l))
        title1=str(title.strip())
    if url.count("flipkart"):
        page = requests.get(url, headers=headers)
        soup= BeautifulSoup(page.content,'html.parser')
        pric = soup.find("div", {"class": "_1vC4OE _3qQ9m1"})
        title = soup.find("span", {"class": "_35KyD6"})
        title1=title.contents[0]
        st=pric.contents[0]
        s=st[1:]
        l=list(s.split(','))
        p=""
        price=float(p.join(l))
    if url.count("snapdeal"):
        page = requests.get(url, headers=headers)
        soup= BeautifulSoup(page.content,'html.parser')
        pric = soup.find("span", {"class": "payBlkBig"})
        title = soup.find("h1", {"class": "pdp-e-i-head"})
        title1=title.contents[0]
        price=float(pric.contents[0])

    if(price <= dp):
        send_mail(title1,dp,email,id,url)
        #push_notification()

def send_mail(title,dp,email,id,url):
    user=User.objects.get(id=id)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    fname=user.first_name
    server.login('ravipatidar644@gmail.com','7221019969')
    subject = "Price of "+title+" has fallen down below Rs. "+str(dp)
    body = "Hey "+fname.capitalize()+" \n The price of "+title+" on AMAZON has fallen down below Rs."+str(dp)+".\n So, hurry up & check the amazon link right now : "+url
    msg = f"Subject: {subject} \n\n {body} "
    server.sendmail(
    'ravipatidar644@gmail.com',
    email,
    msg
    )
    #print("HEY AMLAN, EMAIL HAS BEEN SENT SUCCESSFULLY.")
    
    server.quit()
def fun(name):
    print(name)

while(True):
    l=productdetails.objects.all()
    for i in l:
        fun(i.name)
        check_price(i.url,i.price,i.email,i.userid)
    time.sleep(60)