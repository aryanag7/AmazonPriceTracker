import smtplib as s
from bs4 import BeautifulSoup
import requests
import time

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}

url = "https://www.amazon.in/Apple-Dual-core-10th-Generation-Intel-Core-i3-Processor/dp/B0864HXDG1/ref=sr_1_1?dchild=1&keywords=macbook&qid=1614747676&sr=8-1ds=boss+bassheads&qid=1562494135&s=gateway&sr=8-2-fkmr0=sr_1_3?dchild=1&keywords=macbook&qid=1614698309&sr=8-3"

def check_price():

    req = requests.get(url, headers=header)
    soup = BeautifulSoup(req.content, 'lxml')
    # title= soup.find("h1").text.strip()
#    print(title)
    price = soup.find(id="priceblock_ourprice").text
    price=float(price[2:8].replace(",",""))
    print(price)
    if price < 80000.0:
        send_mail()

def send_mail():
    ob = s.SMTP("smtp.gmail.com",587)
    ob.starttls()
    # look for app passwords

    ob.login("your email","your password")

    subject = "The Price fell down!!!"
    body = "GO Grab them!!:https://www.amazon.in/Apple-Dual-core-10th-Generation-Intel-Core-i3-Processor/dp/B0864HXDG1/ref "

    message = "Subject:{}\n\n{}".format(subject,body)
    listofadd = ["to whom u want to send mail"]
    ob.sendmail("from which mail",listofadd,message)
    print("Send Successfully!!!")
    ob.quit()
while(True):
    check_price()
    time.sleep(3600)
#   can keep running ,executes once in an hour







