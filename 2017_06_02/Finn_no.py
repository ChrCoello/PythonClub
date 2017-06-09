# -*- coding: utf-8 -*-
"""
Created on Sat May  6 10:25:01 2017

@author: kande
"""

import requests as re
from bs4 import BeautifulSoup as bs

Url = "https://www.finn.no/realestate/homes/search.html?location=0.20061"
r=re.get(Url)
c=r.content

soup=bs(c,"html.parser")

################# Mult site
soup_first=bs(c,"html.parser")

base_url = "https://www.finn.no/realestate/homes/search.html?location=0.20061&page="
l=[] 


for page in range(1,43):
    r=re.get(base_url+str(page))
    c=r.content
    soup=bs(c,"html.parser")
 
    all=soup.find_all("div", {"class":"unoverflowify"})




    for item in all:
        d={}
        d["Adress"]=item.find("span", {"class":"licorice valign-middle"}).text #road
        d["Area"]=item.find_all("span", {"class":"prm"})[0].text #kvm
        d['Area'] = d['Area'].replace(' m²', '')
        d['Area'] = d['Area'].split('-')
        d['Area'] = d['Area'][-1]
        

        d["Price"]=item.find_all("span", {"class":"prm"})[-1].text #prize
        d['Price'] = d['Price'].replace(',-', '')
        d["Price"]= d['Price'].replace('\xa0', '')
        d["Price"]= d['Price'].split('-')
        d["Price"]= d['Price'][-1]
        d["Price"]= d['Price'].replace('Solgt', '0')

        a=item.find_all("li", {"class":"truncate"})[1].text#soverom
        if "soverom" in a:
            word =a.split(" ")
            string = word[-2]
            string2 = ' '.join(string)
            d["bedroom"]=string2
        else:
            d["bedroom"]="NaN" 
            #soverom
        l.append(d)
    
import pandas as pd
df=pd.DataFrame(l)


#output CSV
df.to_csv("finn4.csv", encoding='utf-8')