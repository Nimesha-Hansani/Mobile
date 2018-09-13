# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 10:45:38 2018

@author: DaKhz
"""

from  urllib.request import urlopen
import requests
import lxml.html
from bs4 import BeautifulSoup
import csv

html =urlopen("https://www.gsmarena.com/microsoft-phones-64.php")
bsObj =BeautifulSoup(html,"lxml")
filename="MicrosoftPhones1.csv"
f=open(filename,"wt")
headers= "Model,Year,Price,Body,Storage,Display,Camera,Colours\n"

f.write(headers)


for phones in bsObj.findAll("div",{"class":"makers"}):
    for a in phones.findAll('a'):
     url="https://www.gsmarena.com/"
     y=a.get('href')
     z=(url+y)
     
     html =requests.get(z)
     doc=lxml.html.fromstring(html.content)
     
     
     Model=doc.xpath('.//h1[@class="specs-phone-name-title"]/text()')
     Year=doc.xpath('.//span[@data-spec="released-hl"]/text()')
     Price=doc.xpath('//td[@data-spec="price"]/text()')
     Body=doc.xpath('.//span[@data-spec="body-hl"]/text()')
     OS=doc.xpath('.//span[@data-spec="os-hl"]/text()')
     Storage1=doc.xpath('.//span[@data-spec="storage-hl"]/text()')
     Display1=doc.xpath('.//span[@data-spec="displaysize-hl"]/text()')
     Display2=doc.xpath('.//span[@data-spec="displayres-hl"]/text()')
     Camera=doc.xpath('.//td[@data-spec="cam1modules"]/text()')
     #Storage2=doc.xpath('.//span[@data-spec="ramsize-hl"]/text()')
     #Battery=doc.xpath('.//span[@data-spec="batsize-hl"]/text()')
     Colors=doc.xpath('.//td[@data-spec="colors"]/text()')
     
     m=0
     while m < len(Model):
         x1=Model[m]
         print(x1)
         x2=Year[m]
         print(x2)
         x3=Price[m]
         print(x3)
         x4=Body[m]
         print(x4)
         x5=str(Storage1[m]) 
         x6=Display1[m]
         print(Display1[m])
         x7=Camera[m]
         #x8=Battery[m]
         x9=str(Colors[m]).strip(',')
         
         f.write(x1 + "," + x2 +"," + x3 + ","+ x4 +","+ x5 +"," + x6 +"," + x7 +","+x9+ "\n" )
         m=m+1



f.close()