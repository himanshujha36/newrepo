# from bs4 import BeautifulSoup
# import requests
# #import lxml

# with open(r"/Users/mac/Desktop/EU Sanctions Map.html",encoding='utf8') as file:
#     contents = file.read()
# soup = BeautifulSoup(contents,'html.parser')

# name = soup.find_all(name='div',class_ = 'filter-block hidden-print members')
# for n in name:
#     ls = n.find_all(name='li')

# for i in range(4,len(ls)):
#     print(ls[i].text)
    

from bs4 import BeautifulSoup
import requests

import pandas as pd

with open(r"/Users/mac/Desktop/EU Sanctions Map.html",encoding='utf8') as file:
    contents = file.read()
soup = BeautifulSoup(contents,'html.parser')



data = soup.find(name='div',class_ ='filter-block hidden-print members').find_all(name='ul',class_='filter-list')

size = len(data)
table = []
for i in range(size):
    row =[]
    for j in range(4):
        name = data[i].find_all(name='li')[j].getText().split('\n')
        N=''
        for k in name:
            if k!='':
                N=k
                break
        row.append(N)
    table.append(row)
for i in table:
    print(i)

df = pd.DataFrame(table,columns=['Type','FSD_Id','Name','Date of designation (if available on FSD)'])
df.to_csv('data.csv', sep='\t', encoding='utf-8')    