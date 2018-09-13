# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 06:22:10 2018

@author: DaKhz
"""

import csv 
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.91mobiles.com/phonefinder.php')
bsObj=BeautifulSoup(html,"lxml")
products = bsObj.findAll("div",{"class":"a filter-list-text"})

filename="phones6.csv"
f=open(filename,"wt")

headers= "performance, display, camera,battery\n"

f.write(headers)

for product in products:
    
        x=product.findAll('label')[0].text.strip() 
        y=product.findAll('label')[1].text.strip()
        z=product.findAll('label')[1].text.strip()
        
        print(x+y+z)
          
f.write(x+y+z + "," + x+y+z + "," + x+y+z + ","  + "\n")
f.close()