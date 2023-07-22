#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import matplotlib.pyplot as plt

boston_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/boston_housing.csv'
df=pd.read_csv(boston_url)
pd.set_option("display.max.columns", None)
df.head(100)


# In[6]:


pd.plotting.boxplot(df, column=['MEDV'])
plt.show()


# In[20]:


X = ["CHAS"]
Y = list(df.iloc[5])
  
# Plot the data using bar() method
plt.bar(X, Y, color='g')
plt.show()


# In[ ]:




