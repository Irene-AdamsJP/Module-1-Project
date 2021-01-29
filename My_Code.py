#!/usr/bin/env python
# coding: utf-8

# In[395]:


from sqlalchemy import create_engine


# In[396]:


import pandas as pd


# In[397]:


#Connexion string:


# In[398]:


abs_path = '/Users/ireneadamsjdp/Desktop/ironhack_data/raw_data_project_m1.db'

conn_str = f'sqlite:///{abs_path}'

engine = create_engine(conn_str)


# In[399]:


#Database tables:


# In[400]:


data = pd.read_sql_query("SELECT * FROM sqlite_master", engine)


# In[401]:


data.head()


# In[402]:


data.dtypes


# In[403]:


data.info(memory_usage='deep')


# In[404]:


#Data personal_info exploration


# In[405]:


data_personal = pd.read_sql_query('select * from personal_info', engine)


# In[406]:


data_personal.head()


# In[407]:


data_personal.dtypes


# In[408]:


data_personal.info(memory_usage='deep')


# In[409]:


data_personal.isnull()


# In[410]:


data_personal.isnull().sum() #there are no null values


# In[411]:


##Cleaning age column (it is one of the ones I have to deliver for the Challenge)


# In[412]:


data_personal.columns = ['uuid', 'Age', 'gender', 'dem_has_children', 'age_group']


# In[413]:


a = data_personal.age.str.extract(r'(\d*)')


# In[414]:


pd.to_numeric(a[0]) + 5


# In[415]:


data_personal


# In[416]:


print(set(data_personal['Age']))


# In[417]:


data_personal['Age'] = data_personal['Age'].str.replace('years old', '')


# In[418]:


print(set(data_personal['Age']))


# In[419]:


data_personal['Age'] = data_personal['Age'].str.replace(' ', '')


# In[420]:


data_personal.sort_values(by=['Age'], inplace=True)


# In[421]:


print(set(data_personal['Age']))


# In[422]:


data_personal['Age'].iloc[0]


# In[423]:


#+5 años porque estamos en 2021 y los datos son de 2016

data_personal['Age'] = data_personal['Age'].str.replace('65', '70')
data_personal['Age'] = data_personal['Age'].str.replace('64', '69')
data_personal['Age'] = data_personal['Age'].str.replace('63', '68')
data_personal['Age'] = data_personal['Age'].str.replace('62', '67')
data_personal['Age'] = data_personal['Age'].str.replace('61', '66')
data_personal['Age'] = data_personal['Age'].str.replace('60', '65')
data_personal['Age'] = data_personal['Age'].str.replace('59', '64')
data_personal['Age'] = data_personal['Age'].str.replace('58', '63')
data_personal['Age'] = data_personal['Age'].str.replace('57', '62')
data_personal['Age'] = data_personal['Age'].str.replace('56', '61')
data_personal['Age'] = data_personal['Age'].str.replace('55', '60')
data_personal['Age'] = data_personal['Age'].str.replace('54', '59')
data_personal['Age'] = data_personal['Age'].str.replace('53', '58')
data_personal['Age'] = data_personal['Age'].str.replace('52', '57')
data_personal['Age'] = data_personal['Age'].str.replace('51', '56')
data_personal['Age'] = data_personal['Age'].str.replace('50', '55')
data_personal['Age'] = data_personal['Age'].str.replace('49', '54')
data_personal['Age'] = data_personal['Age'].str.replace('48', '53')
data_personal['Age'] = data_personal['Age'].str.replace('47', '52')
data_personal['Age'] = data_personal['Age'].str.replace('46', '51')
data_personal['Age'] = data_personal['Age'].str.replace('45', '50')
data_personal['Age'] = data_personal['Age'].str.replace('44', '49')
data_personal['Age'] = data_personal['Age'].str.replace('43', '48')
data_personal['Age'] = data_personal['Age'].str.replace('42', '47')
data_personal['Age'] = data_personal['Age'].str.replace('40', '45')
data_personal['Age'] = data_personal['Age'].str.replace('39', '44')
data_personal['Age'] = data_personal['Age'].str.replace('38', '43')
data_personal['Age'] = data_personal['Age'].str.replace('37', '42')
data_personal['Age'] = data_personal['Age'].str.replace('36', '41')
data_personal['Age'] = data_personal['Age'].str.replace('35', '40')
data_personal['Age'] = data_personal['Age'].str.replace('34', '39')
data_personal['Age'] = data_personal['Age'].str.replace('33', '38')
data_personal['Age'] = data_personal['Age'].str.replace('32', '37')
data_personal['Age'] = data_personal['Age'].str.replace('31', '36')



data_personal['Age'] = data_personal['Age'].str.replace('1986', '35')
data_personal['Age'] = data_personal['Age'].str.replace('1987', '34')
data_personal['Age'] = data_personal['Age'].str.replace('1988', '33')
data_personal['Age'] = data_personal['Age'].str.replace('1989', '32')
data_personal['Age'] = data_personal['Age'].str.replace('1990', '31')
data_personal['Age'] = data_personal['Age'].str.replace('1991', '30')
data_personal['Age'] = data_personal['Age'].str.replace('1992', '29')
data_personal['Age'] = data_personal['Age'].str.replace('1993', '28')
data_personal['Age'] = data_personal['Age'].str.replace('1994', '27')
data_personal['Age'] = data_personal['Age'].str.replace('1995', '26')
data_personal['Age'] = data_personal['Age'].str.replace('1996', '25')
data_personal['Age'] = data_personal['Age'].str.replace('1997', '24')
data_personal['Age'] = data_personal['Age'].str.replace('1998', '23')
data_personal['Age'] = data_personal['Age'].str.replace('1999', '22')
data_personal['Age'] = data_personal['Age'].str.replace('2000', '21')
data_personal['Age'] = data_personal['Age'].str.replace('2001', '20')
data_personal['Age'] = data_personal['Age'].str.replace('2002', '19')


# In[424]:


print(set(data_personal['Age']))


# In[ ]:





# In[425]:


#Data country_info exploration


# In[426]:


data_country = pd.read_sql_query('select * from country_info', engine)


# In[427]:


data_country.head()


# In[428]:


##Cleaning Country column (it is one of the ones I have to deliver for the Challenge)


# In[429]:


data_country.columns = ['uuid', 'Country', 'rural']


# In[430]:


data_country.head()


# In[431]:


print(set(data_country['Country']))


# In[ ]:


## From Countries abbreviations to full name countries using https://abbreviations.yourdictionary.com/articles/country-abbreviations.html

data_country['Country'] = data_country['Country'].str.replace('BG', 'Bulgaria')
data_country['Country'] = data_country['Country'].str.replace('NL', 'Netherlands')
data_country['Country'] = data_country['Country'].str.replace('CY', 'Cyprus')
data_country['Country'] = data_country['Country'].str.replace('HU', 'Hungary')
data_country['Country'] = data_country['Country'].str.replace('BE', 'Belgium')
data_country['Country'] = data_country['Country'].str.replace('SI', 'Hungary')
data_country['Country'] = data_country['Country'].str.replace('IT', 'Italy')
data_country['Country'] = data_country['Country'].str.replace('PT', 'Portugal')
data_country['Country'] = data_country['Country'].str.replace('EE', 'Estonia')
data_country['Country'] = data_country['Country'].str.replace('SE', 'Sweden')
data_country['Country'] = data_country['Country'].str.replace('ES', 'Spain')
data_country['Country'] = data_country['Country'].str.replace('SK', 'Slovakia')
data_country['Country'] = data_country['Country'].str.replace('FI', 'Finland')
data_country['Country'] = data_country['Country'].str.replace('CZ', 'Czech Republic')
data_country['Country'] = data_country['Country'].str.replace('LV', 'Latvia')
data_country['Country'] = data_country['Country'].str.replace('MT', 'Malta')
data_country['Country'] = data_country['Country'].str.replace('AT', 'Austria')
data_country['Country'] = data_country['Country'].str.replace('DE', 'Germany')
data_country['Country'] = data_country['Country'].str.replace('FR', 'France')
data_country['Country'] = data_country['Country'].str.replace('GB', 'United Kingdom')
data_country['Country'] = data_country['Country'].str.replace('LT', 'Lithuania')
data_country['Country'] = data_country['Country'].str.replace('HR', 'Croatia')
data_country['Country'] = data_country['Country'].str.replace('IE', 'Ireland')
data_country['Country'] = data_country['Country'].str.replace('PL', 'Poland')
data_country['Country'] = data_country['Country'].str.replace('LU', 'Luxembourg')
data_country['Country'] = data_country['Country'].str.replace('GR', 'Greece')
data_country['Country'] = data_country['Country'].str.replace('DK', 'Denmark')
data_country['Country'] = data_country['Country'].str.replace('RO', 'Romania')


# In[432]:


print(set(data_country['Country']))


# In[433]:


data_country.isnull().sum() #there are no null values


# In[434]:


data_country['uuid'][0]


# In[435]:


data_career = pd.read_sql_query('select * from career_info', engine)


# In[436]:


data_career.head()


# In[437]:


data_career.groupby(['dem_education_level', 'dem_full_time_job']).size().reset_index()


# In[438]:


jobs_code_unique = set(data_career['normalized_job_code'])


# In[439]:


data_poll = pd.read_sql_query('select * from poll_info', engine)


# In[440]:


data_poll.head()


# In[441]:


get_ipython().system('python -m pip install requests')

import requests
import json

response = requests.get('http://api.dataatwork.org/v1/jobs/26bc4486dfd0f60b3bb0d8d64e001800')

json_data = response.json()


# In[442]:


job_code_unique2 = (data_career['normalized_job_code']).unique()
len(job_code_unique2)


# In[ ]:





# In[443]:


c = []
code = data_career.normalized_job_code[3]
link = f'http://api.dataatwork.org/v1/jobs/{code}'
b = requests.get(link)
c.append(b.json())


# In[444]:


code = data_career.normalized_job_code[1]


# In[445]:


link = f'http://api.dataatwork.org/v1/jobs/{code}'
b = requests.get(link)
c.append(b.json())


# In[446]:


c


# In[447]:


pd.json_normalize(c)


# In[448]:


link = f'http://api.dataatwork.org/v1/jobs/{code}'

b = requests.get(link)

c = pd.json_normalize(b.json())


# In[455]:


c = []
for code in data_career.normalized_job_code:
    try:
        link = f'http://api.dataatwork.org/v1/jobs/{code}'

        b = requests.get(link)

        c.append(b.json())
    except KeyError:
        print('No ID for this subject')


# In[483]:


titles = pd.json_normalize(c)


# In[491]:


titles.head()


# In[492]:


print(set(titles['title']))


# In[515]:


titles.columns = ['error.code', 'error.message', 'uuid', 'Job_Title', 'normalized_job_title', 'parent_uuid', 'Quantity']


# In[519]:


titles['count'] = titles.groupby('Job_Title')['Job_Title'].transform('count')


# In[626]:


titles.head()


# In[627]:


titles_and_quant = titles.Job_Title.value_counts().rename_axis('Job_Title').reset_index(name='Quantity')


# In[628]:


print(titles_and_quant)


# In[629]:


titles_and_quant2 = pd.merge(titles_and_quant, titles, left_on='Job_Title', right_on='Job_Title')


# In[630]:


titles_and_quant2.head()


# In[631]:


del titles_and_quant2['error.code']


# In[632]:


del titles_and_quant2['error.message']


# In[633]:


del titles_and_quant2['Quantity_y']


# In[634]:


del titles_and_quant2['count']


# In[635]:


titles_and_quant2.head()


# In[636]:


titles["Quantity"] = titles.Job_Title.value_counts()


# In[637]:


titles.head()


# In[638]:


titles_and_percent = titles_and_quant2.Job_Title.value_counts(normalize=True).rename_axis('Job_Title').reset_index(name='Percentage')


# In[639]:


titles_and_percent.head()


# In[640]:


titles_quant_and_percent = pd.merge(titles_and_quant2, titles_and_percent, left_on='Job_Title', right_on='Job_Title')


# In[641]:


titles_quant_and_percent.head()


# In[642]:


titles_quant_and_percent.head()


# In[643]:


titles_quant_and_percent['Percentage'] = titles_quant_and_percent['Percentage']*100


# In[644]:


titles_quant_and_percent.head()


# In[645]:


titles_quant_and_percent['Percentage'] = titles_quant_and_percent['Percentage'].astype(int)


# In[646]:


titles_quant_and_percent.head()


# In[647]:


titles_quant_and_percent['Percentage'] = titles_quant_and_percent['Percentage'].astype(str) + '%'


# In[648]:


titles_quant_and_percent.head()


# In[487]:


quantity_titles = pd.json_normalize(c)


# In[488]:


quantity_titles.head()


# In[489]:


titles_df = pd.DataFrame(quantity_titles) 


# In[459]:


Quantity_percent = quantity_titles.title.value_counts(normalize=True)


# In[460]:


percentage = d.title.value_counts(normalize=True) * 100


# In[461]:


percentage.head()


# In[462]:


percentage2 = percentage.astype(int)


# In[463]:


percentage2.head()


# In[464]:


percentage3 = percentage2.astype(str) + '%'


# In[465]:


percentage3.head()


# In[466]:


import requests
import re
link1 = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'

res = requests.get(url = link1)

from bs4 import BeautifulSoup

soup = BeautifulSoup(res.content)

tablas = soup.find_all('table')

def scrap(tabla):
    pais = []
    codigo = []

    for j in tabla.find_all('td'):
    #     print(i)
        i = str(j)
        if '<td>' in i:
            if '(' in i:
                a = re.match(r'.*\((\w*)', i).group(1)
                codigo.append(a)
            else:
                a = re.match(r'.*\>(\w*)', i).group(1)
                pais.append(a)

    return {'codigo':codigo, 'pais':pais}

dic = scrap(tablas[0])


# In[ ]:





# In[468]:


df_eu = pd.DataFrame(dic)


# In[469]:


df_eu.head()


# In[676]:


data_country.head()


# In[677]:


data_country_name = pd.merge(df_eu, data_country, left_on='codigo', right_on='Country')


# In[678]:


data_country_name.head()


# In[679]:


age_and_country = pd.merge(data_personal, data_country_name, left_on='uuid', right_on='uuid')


# In[680]:


age_and_country.head()


# In[681]:


jobs_careers = pd.merge(titles_quant_and_percent, data_career, left_on='uuid', right_on='normalized_job_code')


# In[682]:


jobs_careers.head()


# In[715]:


age_country_and_jobs = pd.merge(age_and_country, jobs_careers, left_on='uuid', right_on='uuid_y')


# In[716]:


age_country_and_jobs.head()


# In[717]:


del age_country_and_jobs['uuid']


# In[718]:


del age_country_and_jobs['gender']


# In[719]:


del age_country_and_jobs['dem_has_children']


# In[720]:


del age_country_and_jobs['age_group']


# In[721]:


del age_country_and_jobs['codigo']


# In[722]:


age_country_and_jobs.head()


# In[723]:


del age_country_and_jobs['Country']


# In[724]:


del age_country_and_jobs['rural']


# In[725]:


del age_country_and_jobs['uuid_x']


# In[726]:


age_country_and_jobs.head()


# In[727]:


del age_country_and_jobs['normalized_job_title']


# In[728]:


del age_country_and_jobs['parent_uuid']


# In[729]:


del age_country_and_jobs['uuid_y']


# In[730]:


del age_country_and_jobs['dem_education_level']


# In[731]:


del age_country_and_jobs['dem_full_time_job']


# In[732]:


del age_country_and_jobs['normalized_job_code']


# In[733]:


age_country_and_jobs.head()


# In[734]:


age_country_and_jobs.columns = ['Age', 'Country', 'Job Title', 'Quantity', 'Percentage']


# In[735]:


age_country_and_jobs.head()


# In[736]:


age_country_and_jobs = age_country_and_jobs[['Country', 'Job Title', 'Age', 'Quantity', 'Percentage']]


# In[737]:


age_country_and_jobs.head()


# In[747]:


age_country_and_jobs.to_csv('challenge1.csv', index=False)


# In[ ]:




