#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import Series, DataFrame


# In[9]:


films = pd.read_table('films.csv', sep='::', names=['MovieID', 'Title', 'Tag'], engine='python')
films


# In[10]:


users = pd.read_table('users.txt', sep='::', names = ['UserID', 'Gender', 'Age', 'Occepation', 'ZipCode'], engine='python')
users


# In[12]:


ratings = pd.read_table('ratings.txt', sep='::', names=['UserID', 'MovieID', 'Rating', 'Timestap'], engine='python')
ratings


# In[13]:


merge = pd.merge(ratings, users)
merge


# In[15]:


merge = pd.merge(merge, films)
merge


# In[16]:


midMF = merge.pivot_table('Rating', index='Title', columns='Gender', aggfunc='mean')
midMF


# In[17]:


sortF = midMF.sort_values(by='F', ascending=False)
sortF


# In[18]:


sortAge = merge.pivot_table('Rating', index='Title', columns='Age', aggfunc='mean')
sortAge


# In[19]:


sortOld = sortAge.sort_values(by=56, ascending=False)
sortOld


# In[20]:


reznya = merge.groupby('Title').size()
reznya[reznya  >= 250]


# In[21]:


midMF['diff'] = midMF['F'] -  midMF['M']
midMF.sort_values(by='diff', ascending=False).head(15)


# In[22]:


midMF['diff'] = midMF['M'] -  midMF['F']
midMF.sort_values(by='diff', ascending=False).head(15)


# In[ ]:




