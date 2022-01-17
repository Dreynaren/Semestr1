#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier


# In[2]:


iris_data = load_iris()
iris_data.keys()


# In[ ]:




iris_data['data']
# In[4]:


iris_data['target']


# In[5]:


iris_data['target_names']


# In[95]:


x_train, x_test, y_train, y_test = train_test_split(iris_data['data'], iris_data['target'], random_state = 0)


# In[96]:


knn = KNeighborsClassifier(n_neighbors = 3)


# In[97]:


knn.fit(x_train, y_train)


# In[98]:


prediction = knn.predict(x_test)


# In[99]:


print (prediction)
print (y_test)


# In[ ]:




