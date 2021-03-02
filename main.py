import requests
from bs4 import BeautifulSoup
import time

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}

url = "https://www.amazon.in/Apple-Dual-core-10th-Generation-Intel-Core-i3-Processor/dp/B0864HXDG1/ref=sr_1_3?dchild=1&keywords=macbook&qid=1614698309&sr=8-3"

req= requests.get(url,headers=header)
soup = BeautifulSoup(req.content,'lxml')
title= soup.find("h1").text.strip()
print(title)

