# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 18:15:06 2018

@author: Nim
"""
from  urllib.request import urlopen
import requests
import lxml.html
from bs4 import BeautifulSoup
import csv
html =urlopen("https://www.gsmarena.com/huawei-phones-58.php")
bsObj =BeautifulSoup(html,"lxml")
filename="HuwaweiM.csv"
f=open(filename,"wt")
headers= "Model,Year,Body,Storage,Display,Camera,Battery,Colours\n"

f.write(headers)


for phones in bsObj.findAll("div",{"class":"makers"}):
    for a in phones.findAll('a'):
     x="https://www.gsmarena.com/"
     y=a.get('href')
     z=(x+y)
     
     html =requests.get(z)
     doc=lxml.html.fromstring(html.content)
     #print(z)
     Model=doc.xpath('.//h1[@class="specs-phone-name-title"]/text()')
     Year=doc.xpath('.//span[@data-spec="released-hl"]/text()') 
     Body=doc.xpath('.//span[@data-spec="body-hl"]/text()')
     OS=doc.xpath('.//span[@data-spec="os-hl"]/text()')
     storage1=doc.xpath('.//span[@data-spec="storage-hl"]/text()')
     display1=doc.xpath('.//span[@data-spec="displaysize-hl"]/text()')
     display2=doc.xpath('.//span[@data-spec="displayres-hl"]/text()')
     camera=doc.xpath('.//td[@data-spec="cam1modules"]/text()')
    
     storage2=doc.xpath('.//span[@data-spec="ramsize-hl"]/text()')
     Battery=doc.xpath('.//span[@data-spec="batsize-hl"]/text()')
     Colors=doc.xpath('.//td[@data-spec="colors"]/text()')
     
     a=0
     while a < len(Model):
         x1=Model[a]
         print(x1)
         x2=Year[a]
         print(x2)
         x3=Body[a]
         
         print(x3)
         x4=str(storage1[a]) +" " +str(storage2[a])
         x5=display1[a]
         print(display1[a])
         x6=camera[a]
         x7=Battery[a]
         x8=str(Colors[a]).strip(',')
         
         f.write(x1 + "," + x2 +"," + x3 + ","+ x4 +","+ x5 +"," + x6 +"," + x7 +","+x8 + "\n" )
         a=a+1