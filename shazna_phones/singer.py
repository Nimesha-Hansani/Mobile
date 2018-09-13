# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 14:21:00 2018

@author: shazna
"""

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url='https://www.91mobiles.com/top-10-mobiles-in-india'
#open connection and grabbing page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")


containers=page_soup.findAll("div",{"class":"filter filer_finder"})
#print(len(containers))
#print(containers[0])

#container=containers[0]
filename="91mobiles.csv"
f=open(filename,"w")
headers= "brand,price,performance\n"
f.write(headers)


for container in containers:
        container_name=container.find("span",{"class":"a2 star star_width"})
        brand=container_name.h3.a.text
        prices=container.find("span",{"class":"price price_padding"})
        price=prices.text
        #os=container_name.div.text
        container_performance=container.find("div",{"class":"a filter-list-text"})
        performance=container_performance.label.text
        print(brand)
        print(price)
        #print(os)
        print(performance)
       
         
        f.write(brand.replace(","," ")+","+price.replace(","," ")+","+performance.replace(","," ")+"\n")
f.close()   
    

    
    
    
  
    
    
   