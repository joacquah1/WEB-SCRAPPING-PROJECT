# -*- coding: utf-8 -*-
"""Copy of JEPHTAH'S WEB SCRAPPING WORK FROM GHANA-AFRICA

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kGwp5rfRNthFSVJ9Y6-v07HwUPq36mm_
"""

import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

link = 'https://sofifa.com/players?offset=0'

for i in range (0,541,60):
  print(i)
  print(f' https://sofifa.com/players?offset={i}')

"""# **PAGE 1**"""

## PAGE 1
 
url=' https://sofifa.com/players?offset=0'

resp= requests.get(url)
soup=BeautifulSoup(resp.content,'lxml')

NAME = []
for i in soup.findAll("a", {'data-tooltip':True}):
  NAME.append(str(i))

NAME

for i in NAME:
  print(re.sub('^<.*">|18</span>\xa0|</path></svg></a>|<img alt="fifaleague.it" src="https://cdn.sofifa.com/partners/fifaleague.it.png" srcset="https://cdn.sofifa.com/partners/fifaleague.it@2x.png 2x"/></a>|</div></a>','',str(i)))

AGE = []
for i in soup.findAll("td",{'data-col':'ae'}):
  AGE.append(str(i))

AGE

for i in AGE:
  print(re.sub('^<.*">|</td>','',str(i)))

TOTAL_STATS = [] 
for i in soup.findAll('span',{'class':'bp3-tag p'}):
  TOTAL_STATS.append(str(i))

TOTAL_STATS

for i in TOTAL_STATS:
  print(re.sub('^<.*">|</span>','',str(i)))

TEAM_NAME=[]
for i in soup.findAll('a',{'href':True}):
    TEAM_NAME.append(str(i))

TEAM_NAME

for i in TEAM_NAME:
  print(re.sub('^<.*">|<img.*</a>','',str(i)))

WAGE = []
for i in soup.findAll('td',{'data-col':'wg'}):
  WAGE.append(str(i))

WAGE

for i in WAGE:
  print(re.sub('^<.*">|K</td>|</td>','',str(i)))

CONTRACT = []
for i in soup.findAll('div',{'class':'sub'}):
  CONTRACT.append(str(i))

CONTRACT

for i in CONTRACT:
  print(re.sub('^<.*">|</div>|<span class="bp3-tag bp3-minimal bp3-intent-success">On Loan</span>','',str(i)))

VALUE = []
for i in soup.findAll('td',{'data-col':'vl'}):
  VALUE.append(str(i))

VALUE

for i in VALUE:
  print(re.sub('^<.*">|M</td>|K</td>','',str(i)))

import pandas as pd

df = pd.DataFrame({"Name": NAME,
                   "Age": AGE,
                   "Contract_Year": CONTRACT,
                   "Value": VALUE,
                   "Wage(K)": WAGE,
                   "Total_Stats": TOTAL_STATS})

df.head()

"""Hello Sir,please the pandas dataframe is not working when I run it,also the tags for ova and pot are same, hence upon scrapping the values for one it as well clears the value of the other, you can check and see Sir.

# **PAGE 2**
"""

## PAGE 2
 
url=' https://sofifa.com/players?offset=60'

resp= requests.get(url)
soup=BeautifulSoup(resp.content,'lxml')

NAME = []
for i in soup.findAll("a", {'data-tooltip':True}):
  NAME.append(str(i))

for i in NAME:
  print(re.sub('^<.*">|18</span>\xa0|</path></svg></a>|<img alt="fifaleague.it" src="https://cdn.sofifa.com/partners/fifaleague.it.png" srcset="https://cdn.sofifa.com/partners/fifaleague.it@2x.png 2x"/></a>|</div></a>','',str(i)))

AGE = []
for i in soup.findAll("td",{'data-col':'ae'}):
  AGE.append(str(i))

for i in AGE:
  print(re.sub('^<.*">|</td>','',str(i)))

TOTAL_STATS = [] 
for i in soup.findAll('span',{'class':'bp3-tag p'}):
  TOTAL_STATS.append(str(i))

for i in TOTAL_STATS:
  print(re.sub('^<.*">|</span>','',str(i)))

TEAM_NAME=[]
for i in soup.findAll('a',{'href':True}):
    TEAM_NAME.append(str(i))

for i in TEAM_NAME:
  print(re.sub('^<.*">|<img.*</a>','',str(i)))

WAGE = []
for i in soup.findAll('td',{'data-col':'wg'}):
  WAGE.append(str(i))

for i in WAGE:
  print(re.sub('^<.*">|K</td>|</td>','',str(i)))

CONTRACT = []
for i in soup.findAll('div',{'class':'sub'}):
  CONTRACT.append(str(i))

for i in CONTRACT:
  print(re.sub('^<.*">|</div>|<span class="bp3-tag bp3-minimal bp3-intent-success">On Loan</span>','',str(i)))

VALUE = []
for i in soup.findAll('td',{'data-col':'vl'}):
  VALUE.append(str(i))

for i in VALUE:
  print(re.sub('^<.*">|M</td>|K</td>','',str(i)))

## PAGE 3
 
url=' https://sofifa.com/players?offset=120'

resp= requests.get(url)
soup=BeautifulSoup(resp.content,'lxml')

NAME = []
for i in soup.findAll("a", {'data-tooltip':True}):
  NAME.append(str(i))

for i in NAME:
  print(re.sub('^<.*">|18</span>\xa0|</path></svg></a>|<img alt="fifaleague.it" src="https://cdn.sofifa.com/partners/fifaleague.it.png" srcset="https://cdn.sofifa.com/partners/fifaleague.it@2x.png 2x"/></a>|</div></a>','',str(i)))

AGE = []
for i in soup.findAll("td",{'data-col':'ae'}):
  AGE.append(str(i))

for i in AGE:
  print(re.sub('^<.*">|</td>','',str(i)))

TOTAL_STATS = [] 
for i in soup.findAll('span',{'class':'bp3-tag p'}):
  TOTAL_STATS.append(str(i))

for i in TOTAL_STATS:
  print(re.sub('^<.*">|</span>','',str(i)))

TEAM_NAME=[]
for i in soup.findAll('a',{'href':True}):
    TEAM_NAME.append(str(i))

for i in TEAM_NAME:
  print(re.sub('^<.*">|<img.*</a>','',str(i)))

WAGE = []
for i in soup.findAll('td',{'data-col':'wg'}):
  WAGE.append(str(i))

for i in WAGE:
  print(re.sub('^<.*">|K</td>|</td>','',str(i)))

CONTRACT = []
for i in soup.findAll('div',{'class':'sub'}):
  CONTRACT.append(str(i))

for i in CONTRACT:
  print(re.sub('^<.*">|</div>|<span class="bp3-tag bp3-minimal bp3-intent-success">On Loan</span>','',str(i)))

VALUE = []
for i in soup.findAll('td',{'data-col':'vl'}):
  VALUE.append(str(i))

for i in VALUE:
  print(re.sub('^<.*">|M</td>|K</td>','',str(i)))

"""# **PAGE**"""

## PAGE 4
 
url=' https://sofifa.com/players?offset=180'

resp= requests.get(url)
soup=BeautifulSoup(resp.content,'lxml')

NAME = []
for i in soup.findAll("a", {'data-tooltip':True}):
  NAME.append(str(i))

for i in NAME:
  print(re.sub('^<.*">|18</span>\xa0|</path></svg></a>|<img alt="fifaleague.it" src="https://cdn.sofifa.com/partners/fifaleague.it.png" srcset="https://cdn.sofifa.com/partners/fifaleague.it@2x.png 2x"/></a>|</div></a>','',str(i)))

AGE = []
for i in soup.findAll("td",{'data-col':'ae'}):
  AGE.append(str(i))

for i in AGE:
  print(re.sub('^<.*">|</td>','',str(i)))

TOTAL_STATS = [] 
for i in soup.findAll('span',{'class':'bp3-tag p'}):
  TOTAL_STATS.append(str(i))

for i in TOTAL_STATS:
  print(re.sub('^<.*">|</span>','',str(i)))

TEAM_NAME=[]
for i in soup.findAll('a',{'href':True}):
    TEAM_NAME.append(str(i))

for i in TEAM_NAME:
  print(re.sub('^<.*">|<img.*</a>','',str(i)))

WAGE = []
for i in soup.findAll('td',{'data-col':'wg'}):
  WAGE.append(str(i))

for i in WAGE:
  print(re.sub('^<.*">|K</td>|</td>','',str(i)))

CONTRACT = []
for i in soup.findAll('div',{'class':'sub'}):
  CONTRACT.append(str(i))

for i in CONTRACT:
  print(re.sub('^<.*">|</div>|<span class="bp3-tag bp3-minimal bp3-intent-success">On Loan</span>','',str(i)))

VALUE = []
for i in soup.findAll('td',{'data-col':'vl'}):
  VALUE.append(str(i))

for i in VALUE:
  print(re.sub('^<.*">|M</td>|K</td>','',str(i)))

"""# **PAGE 5**"""

## PAGE 5
 
url=' https://sofifa.com/players?offset=240'

resp= requests.get(url)
soup=BeautifulSoup(resp.content,'lxml')

NAME = []
for i in soup.findAll("a", {'data-tooltip':True}):
  NAME.append(str(i))

for i in NAME:
  print(re.sub('^<.*">|18</span>\xa0|</path></svg></a>|<img alt="fifaleague.it" src="https://cdn.sofifa.com/partners/fifaleague.it.png" srcset="https://cdn.sofifa.com/partners/fifaleague.it@2x.png 2x"/></a>|</div></a>','',str(i)))

AGE = []
for i in soup.findAll("td",{'data-col':'ae'}):
  AGE.append(str(i))

for i in AGE:
  print(re.sub('^<.*">|</td>','',str(i)))

TOTAL_STATS = [] 
for i in soup.findAll('span',{'class':'bp3-tag p'}):
  TOTAL_STATS.append(str(i))

for i in TOTAL_STATS:
  print(re.sub('^<.*">|</span>','',str(i)))

TEAM_NAME=[]
for i in soup.findAll('a',{'href':True}):
    TEAM_NAME.append(str(i))

for i in TEAM_NAME:
  print(re.sub('^<.*">|<img.*</a>','',str(i)))

CONTRACT = []
for i in soup.findAll('div',{'class':'sub'}):
  CONTRACT.append(str(i))

for i in CONTRACT:
  print(re.sub('^<.*">|</div>|<span class="bp3-tag bp3-minimal bp3-intent-success">On Loan</span>','',str(i)))

VALUE = []
for i in soup.findAll('td',{'data-col':'vl'}):
  VALUE.append(str(i))

for i in VALUE:
  print(re.sub('^<.*">|M</td>|K</td>','',str(i)))

## PAGE 6
 
url=' https://sofifa.com/players?offset=300'

"""# **PAGE 6**"""

resp= requests.get(url)
soup=BeautifulSoup(resp.content,'lxml')

NAME = []
for i in soup.findAll("a", {'data-tooltip':True}):
  NAME.append(str(i))

for i in NAME:
  print(re.sub('^<.*">|18</span>\xa0|</path></svg></a>|<img alt="fifaleague.it" src="https://cdn.sofifa.com/partners/fifaleague.it.png" srcset="https://cdn.sofifa.com/partners/fifaleague.it@2x.png 2x"/></a>|</div></a>','',str(i)))

AGE = []
for i in soup.findAll("td",{'data-col':'ae'}):
  AGE.append(str(i))

for i in AGE:
  print(re.sub('^<.*">|</td>','',str(i)))

TOTAL_STATS = [] 
for i in soup.findAll('span',{'class':'bp3-tag p'}):
  TOTAL_STATS.append(str(i))

for i in TOTAL_STATS:
  print(re.sub('^<.*">|</span>','',str(i)))

TEAM_NAME=[]
for i in soup.findAll('a',{'href':True}):
    TEAM_NAME.append(str(i))

for i in TEAM_NAME:
  print(re.sub('^<.*">|<img.*</a>','',str(i)))

CONTRACT = []
for i in soup.findAll('div',{'class':'sub'}):
  CONTRACT.append(str(i))

for i in CONTRACT:
  print(re.sub('^<.*">|</div>|<span class="bp3-tag bp3-minimal bp3-intent-success">On Loan</span>','',str(i)))

VALUE = []
for i in soup.findAll('td',{'data-col':'vl'}):
  VALUE.append(str(i))

for i in VALUE:
  print(re.sub('^<.*">|M</td>|K</td>','',str(i)))

"""# **PAGE 7**"""

## PAGE 7
 
url=' https://sofifa.com/players?offset=360'

resp= requests.get(url)
soup=BeautifulSoup(resp.content,'lxml')

NAME = []
for i in soup.findAll("a", {'data-tooltip':True}):
  NAME.append(str(i))

for i in NAME:
  print(re.sub('^<.*">|18</span>\xa0|</path></svg></a>|<img alt="fifaleague.it" src="https://cdn.sofifa.com/partners/fifaleague.it.png" srcset="https://cdn.sofifa.com/partners/fifaleague.it@2x.png 2x"/></a>|</div></a>','',str(i)))

AGE = []
for i in soup.findAll("td",{'data-col':'ae'}):
  AGE.append(str(i))

for i in AGE:
  print(re.sub('^<.*">|</td>','',str(i)))

TOTAL_STATS = [] 
for i in soup.findAll('span',{'class':'bp3-tag p'}):
  TOTAL_STATS.append(str(i))

for i in TOTAL_STATS:
  print(re.sub('^<.*">|</span>','',str(i)))

TEAM_NAME=[]
for i in soup.findAll('a',{'href':True}):
    TEAM_NAME.append(str(i))

for i in TEAM_NAME:
  print(re.sub('^<.*">|<img.*</a>','',str(i)))

CONTRACT = []
for i in soup.findAll('div',{'class':'sub'}):
  CONTRACT.append(str(i))

for i in CONTRACT:
  print(re.sub('^<.*">|</div><span class="bp3-tag bp3-minimal bp3-intent-success">On Loan</span>','',str(i)))

VALUE = []
for i in soup.findAll('td',{'data-col':'vl'}):
  VALUE.append(str(i))

for i in VALUE:
  print(re.sub('^<.*">|M</td>|K</td>','',str(i)))

"""**PAGE 8**"""

## PAGE 8
 
url=' https://sofifa.com/players?offset=420'

resp= requests.get(url)
soup=BeautifulSoup(resp.content,'lxml')

NAME = []
for i in soup.findAll("a", {'data-tooltip':True}):
  NAME.append(str(i))

for i in NAME:
  print(re.sub('^<.*">|18</span>\xa0|</path></svg></a>|<img alt="fifaleague.it" src="https://cdn.sofifa.com/partners/fifaleague.it.png" srcset="https://cdn.sofifa.com/partners/fifaleague.it@2x.png 2x"/></a>|</div></a>','',str(i)))

AGE = []
for i in soup.findAll("td",{'data-col':'ae'}):
  AGE.append(str(i))

for i in AGE:
  print(re.sub('^<.*">|</td>','',str(i)))

TOTAL_STATS = [] 
for i in soup.findAll('span',{'class':'bp3-tag p'}):
  TOTAL_STATS.append(str(i))

for i in TOTAL_STATS:
  print(re.sub('^<.*">|</span>','',str(i)))

TEAM_NAME=[]
for i in soup.findAll('a',{'href':True}):
    TEAM_NAME.append(str(i))

for i in TEAM_NAME:
  print(re.sub('^<.*">|<img.*</a>','',str(i)))

CONTRACT = []
for i in soup.findAll('div',{'class':'sub'}):
  CONTRACT.append(str(i))

for i in CONTRACT:
  print(re.sub('^<.*">|</div>|<span class="bp3-tag bp3-minimal bp3-intent-success">On Loan</span>','',str(i)))

VALUE = []
for i in soup.findAll('td',{'data-col':'vl'}):
  VALUE.append(str(i))

for i in VALUE:
  print(re.sub('^<.*">|M</td>|K</td>','',str(i)))

"""# **PAGE 9**"""

## PAGE 9
 
url=' https://sofifa.com/players?offset=480'

resp= requests.get(url)
soup=BeautifulSoup(resp.content,'lxml')

NAME = []
for i in soup.findAll("a", {'data-tooltip':True}):
  NAME.append(str(i))

for i in NAME:
  print(re.sub('^<.*">|18</span>\xa0|</path></svg></a>|<img alt="fifaleague.it" src="https://cdn.sofifa.com/partners/fifaleague.it.png" srcset="https://cdn.sofifa.com/partners/fifaleague.it@2x.png 2x"/></a>|</div></a>','',str(i)))

AGE = []
for i in soup.findAll("td",{'data-col':'ae'}):
  AGE.append(str(i))

for i in AGE:
  print(re.sub('^<.*">|</td>','',str(i)))

TOTAL_STATS = [] 
for i in soup.findAll('span',{'class':'bp3-tag p'}):
  TOTAL_STATS.append(str(i))

for i in TOTAL_STATS:
  print(re.sub('^<.*">|</span>','',str(i)))

TEAM_NAME=[]
for i in soup.findAll('a',{'href':True}):
    TEAM_NAME.append(str(i))

for i in TEAM_NAME:
  print(re.sub('^<.*">|<img.*</a>','',str(i)))

CONTRACT = []
for i in soup.findAll('div',{'class':'sub'}):
  CONTRACT.append(str(i))

for i in CONTRACT:
  print(re.sub('^<.*">|</div>|<span class="bp3-tag bp3-minimal bp3-intent-success">On Loan</span>','',str(i)))

VALUE = []
for i in soup.findAll('td',{'data-col':'vl'}):
  VALUE.append(str(i))

for i in VALUE:
  print(re.sub('^<.*">|M</td>|K</td>','',str(i)))

"""# **PAGE 10**"""

## PAGE 10
 
url=' https://sofifa.com/players?offset=540'

resp= requests.get(url)
soup=BeautifulSoup(resp.content,'lxml')

NAME = []
for i in soup.findAll("a", {'data-tooltip':True}):
  NAME.append(str(i))

for i in NAME:
  print(re.sub('^<.*">|18</span>\xa0|</path></svg></a>|<img alt="fifaleague.it" src="https://cdn.sofifa.com/partners/fifaleague.it.png" srcset="https://cdn.sofifa.com/partners/fifaleague.it@2x.png 2x"/></a>|</div></a>','',str(i)))

AGE = []
for i in soup.findAll("td",{'data-col':'ae'}):
  AGE.append(str(i))

for i in AGE:
  print(re.sub('^<.*">|</td>','',str(i)))

TOTAL_STATS = [] 
for i in soup.findAll('span',{'class':'bp3-tag p'}):
  TOTAL_STATS.append(str(i))

for i in TOTAL_STATS:
  print(re.sub('^<.*">|</span>','',str(i)))

TEAM_NAME=[]
for i in soup.findAll('a',{'href':True}):
    TEAM_NAME.append(str(i))

for i in TEAM_NAME:
  print(re.sub('^<.*">|<img.*</a>','',str(i)))

CONTRACT = []
for i in soup.findAll('div',{'class':'sub'}):
  CONTRACT.append(str(i))

for i in CONTRACT:
  print(re.sub('^<.*">|</div>|<span class="bp3-tag bp3-minimal bp3-intent-success">On Loan</span>','',str(i)))

VALUE = []
for i in soup.findAll('td',{'data-col':'vl'}):
  VALUE.append(str(i))

for i in VALUE:
  print(re.sub('^<.*">|M</td>|K</td>','',str(i)))