#!/usr/bin/env python
# coding: utf-8

# In[16]:


from bs4 import BeautifulSoup
import requests
import datetime



# In[17]:


#connecting to website and getting the data
URL ='https://www.amazon.in/LEOTUDE-Regular-Sleeve-T-Shirt-Color/dp/B09CV399D5/ref=sr_1_5?crid=18NA5PMLU5UNG&dib=eyJ2IjoiMSJ9.8kjp9RYjMqxuSiSMj6zZpkKSJOiwzZKzDZehiG13lCXNcF1j6aoAf1GfXubORZgtApBuTQ2Tsy4azDR60FC3dst1_R5balIFdxxmJjtqtCI5D-k6EexPCfj_SGkxAO25NPvU2pI6Y6l69XGF1QltlHjdASZ2IcwR4yOjjklgc0fK-fZNehS2OOTYABtHUu8Ocrfnshvc_wr7TAZkHFGZOPrwL_GdW5XN1P6BE6Nn0_sgx6_zjthTZfO0uTfdnbskEGJfB2LkiEUIqS6Q71IndGlEIZ8WTABxUrQW_6CcCZs.U14cYYnosec2adL2p59-A3ru-C0rnVXBLuHQTH0K5x0&dib_tag=se&keywords=tshirt+for+man&qid=1732120050&sprefix=tsh%2Caps%2C344&sr=8-5'
headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-673e0e9d-293e616b6c48a95e17f5d091"}
page=requests.get(URL,headers=headers)
soup1=BeautifulSoup(page.content,"html.parser")
soup2=BeautifulSoup(soup1.prettify(),"html.parser")
title=soup2.find(id='productTitle').text.strip()
price=soup2.find('span',class_='a-price-whole').text.strip()
print("t-shirt name-")
print(title)
print(f'price: Rs.{price}')


# In[18]:


#create a Timestamp for your output to track when data was collected
import datetime
today = datetime.date.today()
print(today)


# In[19]:


#csv creation
import csv

header =['Title','Price','Date']
data=[title,price,today]


with open('AmazonWebScraperDatasetk.csv', 'w',newline='',encoding='UTF8') as f:
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[20]:


import pandas as pd
df=pd.read_csv(r'C:\Users\Administrator\Downloads\AmazonWebScraperDatasetk.csv')
print(df)


# In[21]:


#combining all the code into the function

def check_price():
    URL ='https://www.amazon.in/LEOTUDE-Regular-Sleeve-T-Shirt-Color/dp/B09CV399D5/ref=sr_1_5?crid=18NA5PMLU5UNG&dib=eyJ2IjoiMSJ9.8kjp9RYjMqxuSiSMj6zZpkKSJOiwzZKzDZehiG13lCXNcF1j6aoAf1GfXubORZgtApBuTQ2Tsy4azDR60FC3dst1_R5balIFdxxmJjtqtCI5D-k6EexPCfj_SGkxAO25NPvU2pI6Y6l69XGF1QltlHjdASZ2IcwR4yOjjklgc0fK-fZNehS2OOTYABtHUu8Ocrfnshvc_wr7TAZkHFGZOPrwL_GdW5XN1P6BE6Nn0_sgx6_zjthTZfO0uTfdnbskEGJfB2LkiEUIqS6Q71IndGlEIZ8WTABxUrQW_6CcCZs.U14cYYnosec2adL2p59-A3ru-C0rnVXBLuHQTH0K5x0&dib_tag=se&keywords=tshirt+for+man&qid=1732120050&sprefix=tsh%2Caps%2C344&sr=8-5'
    headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36", 
        "X-Amzn-Trace-Id": "Root=1-673e0e9d-293e616b6c48a95e17f5d091"}
    page=requests.get(URL,headers=headers)
    soup1=BeautifulSoup(page.content,"html.parser")
    soup2=BeautifulSoup(soup1.prettify(),"html.parser")
    title=soup2.find(id='productTitle').text.strip()
    price=soup2.find('span',class_='a-price-whole').text.strip()
    import datetime
    today = datetime.date.today()
    import csv

    header =['Title','Price','Date']
    data=[title,price,today]

    #appending data to the csv
    with open('AmazonWebScraperDataset1k.csv', 'w',newline='',encoding='UTF8') as f:
        writer=csv.writer(f)
        writer.writerow(data)


# In[22]:


import pandas as pd
df=pd.read_csv(r'C:\Users\Administrator\Downloads\AmazonWebScraperDatasetk.csv')
print(df)


# In[15]:





# In[ ]:




