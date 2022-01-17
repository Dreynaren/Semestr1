#!/usr/bin/env python
# coding: utf-8

# In[5]:


#task1
a = [2,3,7,9]
a.append(15)
print(a)
a.clear()
print(a)
a = [2,3,7,9]
a.copy()
print(a)
a.count(3)
print(a)
a.index(3)
print(a)
a.insert(4,13)
print(a)
a.pop(4)
print(a)
a.remove(2)
print(a)
a.reverse()
print(a)
a.sort()
print(a)


# In[1]:


#task2
a = int(input("введите число:"))

def F (n):
    if n > 1 :return n * F(n-1)
    elif n == 1: return 1
    elif n < 0: return "Ошибка"
    else : return 1 
    
F (a)


# In[3]:


#task3
from random import randint
a = randint(0,2)
mas = ['камень', 'ножницы', 'бумага']
print ("Введите 'камень', 'ножницы' или 'бумага'")

def UserChoice():
    c = int = 0
    userk = input("Выберите:")
    print()    
    if userk == 'камень' or userk == 'камень': 
        c = 0        
        Game(c)
    elif userk == 'ножницы' or userk == 'ножницы': 
        c = 1       
        Game(c)
    elif userk == 'бумага' or userk == 'бумага': 
        c = 2        
        Game(c)
    else:
        print("Ошибка")
        UserChoice()       


def Game(b):
    
    if (b == 0) and (a == 1) : print('победа')
    elif (b == 0) and (a == 2) : print('поражение')
    elif (b == 0) and (a == 0) : print('ничья')
        
    if (b == 1) and (a == 2) : print('победа')
    elif (b == 1) and (a == 0) : print('поражение')
    elif (b == 1) and (a == 1) : print('ничья')
        
    if (b == 2) and (a == 0) : print('победа') 
    elif (b == 2) and (a == 1) : print('поражение')
    elif (b == 2) and (a == 2) : print('ничья')
        
    print("Противник выбрал:", mas[a])
    
UserChoice() 


# In[ ]:




