#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import random
import matplotlib.pyplot as plt
m=[1, -1]
n=int(input('размер матрицы '))
a=np.zeros((n,n))
h=int(input('количество повторов '))
l=0 
per=int(input('нешахматы(1) или шахматы(2)'))
for i in range(n):
    for j in range(n):
        a[i, j]=random.choice(m)
print(a)                                   
c=a.copy()

for l in range(h):
    print("Петля №", l)
    b=a.copy()
    summ1=0
    summ2=0
    b[random.randrange(n), random.randrange(n)]*=-1 
    for i in range(n):
        for j in range(n):
            summ1+=a[i, j]*a[i, j-1]+a[i-1, j]*a[i, j]
            summ2+=b[i, j]*b[i, j-1]+b[i-1, j]*b[i, j]
    print('Сумма новой ',summ2)
    if per==1:
        dsumm=-1*(summ2-summ1)
    else:
        dsumm=summ2-summ1
    print('Разницы сумм ',dsumm)                                   
    if dsumm<=0:                                       
        a=b.copy()
    else:
        t=float(1)
        w=np.exp(-dsumm/t)
        p=round(random.uniform(0, 1), 5)
        if w>=p:
            c=a.copy()
        elif w<0:
            a=c.copy()
    i+=1
    plt.clf()
    plt.imshow(a)
    plt.draw()
    plt.show()
    plt.gcf().canvas.flush_events()


# In[ ]:




