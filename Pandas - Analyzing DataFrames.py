#!/usr/bin/env python
# coding: utf-8

# In[37]:


import  pandas as pd

x = pd.read_csv('data.csv')
print(x.head(10))


# In[38]:


import pandas as pd

x = pd.read_csv('data.csv')
print(x.head())


# In[39]:


import pandas as pd

x = pd.read_csv('data.csv')
print(x.tail())


# In[40]:


import pandas as pd

x = pd.read_csv('data.csv')
print(x.info())

