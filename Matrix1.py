#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import random 
m=[1,-1] 
samm=0
l=0
n=int(input())
a=np.zeros((n,n))

for i in range(n):
    for j in range(n):
        a[i,j]=random.choice(m)
print(a)

for i in range(n):
    for j in range(n):
        samm+=a[i,j]*a[i,j-1]
        l+=a[i-1,j]*a[i,j]        
print(samm+l)

