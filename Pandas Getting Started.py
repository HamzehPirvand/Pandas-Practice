#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas


# In[4]:


mydataset = {
    'cars' : ["BMW", "ford", "Volvo"],
    'passing' : [3, 7, 2]
}

x = pandas.DataFrame(mydataset)

print(x)


# In[5]:


import pandas as pd


# In[7]:


x = {
    'fruits' : ["apple", "kiwi", "banana"],
    'quantity' : [6, 8, 5]
}

y = pandas.DataFrame(x)
print(y)


# In[8]:


import pandas as pd
print(pd.__version__)

