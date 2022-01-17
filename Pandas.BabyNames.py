#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


names = pd.read_table('yob1880.txt', sep=',', names=['name', 'sex', 'number'])
names


# In[4]:


names.groupby('sex').size()


# In[5]:


years = range(1880, 2011)
pieces = []
for i in years:
    df = pd.read_table('yob%d.txt'%i, sep = ',', engine = 'python' , names=['name', 'sex', 'number'])
    df['year'] = i
    pieces.append(df)
    data = pd.concat(pieces, ignore_index = True)
data


# In[6]:


YearsSexCount = data.groupby(['year', 'sex']).size()
YearsSexCount


# In[7]:


abscissa = []
ordinada_F = []
ordinada_M = []

for i in range(1880, 2011):
    abscissa.append(i)

for i in range(0, 262):
    if i % 2 == 0:
        ordinada_F.append(YearsSexCount.iloc[i])
    else:
        ordinada_M.append(YearsSexCount.iloc[i])
        
plt.plot(abscissa, ordinada_F, label='Famale')
plt.plot(abscissa, ordinada_M, label='Male')
plt.legend()


# In[8]:


data['proportion'] = data['number'] / sum(data['number'])
data


# In[11]:


years = []
for i in range(1880, 2011):
    years.append(i)
Johnny = []
Natalie = []
Bob = []
Anton = []
s = []
for i in range(1880, 2011):
    local_df = pd.read_table('yob%d.txt'%i, sep=',', names=['name', 'sex', 'number'])
    summ_count = sum(local_df['number'])
    J_count= sum(local_df[local_df['name'] == 'Johnny']['number'])
    Johnny.append(J_count / summ_count)
    N_count= sum(local_df[local_df['name'] == 'Natalie']['number'])
    Natalie.append(N_count / summ_count)
    B_count= sum(local_df[local_df['name'] == 'Bob']['number'])
    Bob.append(B_count / summ_count)
    A_count= sum(local_df[local_df['name'] == 'Anton']['number'])
    Anton.append(A_count / summ_count)


plt.plot(years, Johnny, label='Johnny')
plt.plot(years, Natalie, label='Natalie')
plt.plot(years, Bob, label='Bob')
plt.plot(years, Anton, label='Anton')
plt.legend()


# In[12]:


max_count = []
for i in range(1880, 2011):
    loc = pd.read_table('yob%d.txt'%i, sep=',', names=['name', 'sex', 'number'])
    sort = loc.sort_values(by='number', ascending=False)
    max_count.append(sort['number'].iloc[0])
print('year : max')
for i in range(131):
    print(years[i], ':', max_count[i])


# In[ ]:




