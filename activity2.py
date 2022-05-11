from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(url)
soup=bs(page.text,"html.parser")
star_table=soup.find_all("table")
temp_list=[]
table_rows=star_table[5].find_all("tr")
for tr in table_rows:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td] 
    temp_list.append(row)
star_name=[]
dist=[]
mass=[]
radius=[]

for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][0])
    dist.append(temp_list[i][5])  
    mass.append(temp_list[i][7]) 
    radius.append(temp_list[i][8]) 
df=pd.DataFrame(list(zip(star_name,dist,mass,radius)),columns=["Star_name","distance","mass","radius"])    
df.to_csv("dwarf_stars.csv")
