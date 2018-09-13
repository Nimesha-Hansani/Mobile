# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 10:25:53 2018

@author: DaKhz
"""

from  urllib.request import urlopen
import requests
import lxml.html
from bs4 import BeautifulSoup
import csv

html =urlopen("https://www.gsmarena.com/nokia-phones-1.php")
bsObj =BeautifulSoup(html,"lxml")
filename="NokiaPhones.csv"
f=open(filename,"wt")
headers= "Model,Year,Price,Body,Storage,Display,Camera,Battery,Colours\n"

f.write(headers)


for phones in bsObj.findAll("div",{"class":"makers"}):
    for a in phones.findAll('a'):
     x="https://www.gsmarena.com/"
     y=a.get('href')
     z=(x+y)
     
     html =requests.get(z)
     doc=lxml.html.fromstring(html.content)
     
     
     Model=doc.xpath('.//h1[@class="specs-phone-name-title"]/text()')
     Year=doc.xpath('.//span[@data-spec="released-hl"]/text()')
     Price=doc.xpath('//td[@data-spec="price"]/text()')
     Body=doc.xpath('.//span[@data-spec="body-hl"]/text()')
     OS=doc.xpath('.//span[@data-spec="os-hl"]/text()')
     storage1=doc.xpath('.//span[@data-spec="storage-hl"]/text()')
     display1=doc.xpath('.//span[@data-spec="displaysize-hl"]/text()')
     display2=doc.xpath('.//span[@data-spec="displayres-hl"]/text()')
     camera=doc.xpath('.//td[@data-spec="cam1modules"]/text()')
     #storage2=doc.xpath('.//span[@data-spec="ramsize-hl"]/text()')
     Battery=doc.xpath('.//span[@data-spec="batsize-hl"]/text()')
     Colors=doc.xpath('.//td[@data-spec="colors"]/text()')
     
     n=0
     while n < len(Model):
         x1=Model[n]
         print(x1)
         x2=Year[n]
         print(x2)
         x3=Price[n]
         print(x3)
         x4=Body[n]
         print(x4)
         x5=str(storage1[n]) 
         x6=display1[n]
         print(display1[n])
         x7=camera[n]
         x8=Battery[n]
         x9=str(Colors[n]).strip(',')
         
         f.write(x1+ "," + x2.replace(","," ") +"," + x3.replace(","," ") + ","+ x4.replace(","," ") +","+ x5.replace(","," ") +"," + x6.replace(","," ") +"," + x7.replace(","," ") +","+x8.replace(","," ") +","+x9.replace(","," ")+ "\n" )
         n=n+1



f.close()