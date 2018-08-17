# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 00:12:59 2018

@author: Nim
"""

from  urllib.request import urlopen
from bs4 import BeautifulSoup

html =urlopen("https://buyabans.com/item/list/mobile-phones")
bsObj =BeautifulSoup(html,"lxml")
products =bsObj.findAll("div",{"class":"product-container"})


filename="Abans1.csv"

f=open(filename,"wt")

headers= "Phone,ModelNo,Price\n"

f.write(headers)

for product in products:
        
    x=product.findAll('div')[2].text.strip()
    y=product.findAll('div')[3].text.strip()
    z=product.findAll('div')[5].text.strip().replace(","," ")
    
    print("Phone: "+x)
    print("ModelNo: "+y)
    print("Price : "+z)
    
    f.write(x + "," + y +"," + z + "\n" )
    
    
    