#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd

x = {
    "calories" : [420, 380, 570],
    "duration" : [50, 40, 45]
}

y = pd.DataFrame(x)
print(y)


# In[26]:


import pandas as pd

x = {
    "names" : ["Joe", "Jacob", "Sarah"],
    "ages" : [32, 51, 28]
}

y = pd.DataFrame(x)
print(y.loc[1])


# In[29]:


import pandas as pd

x = {
    "names" : ["Joe", "Jacob", "Sarah"],
    "ages" : [32, 51, 28]
}

y = pd.DataFrame(x)
print(y.loc[[0, 2]])


# In[31]:


import pandas as pd

x = {
    "names" : ["Joe", "Jacob", "Sarah"],
    "ages" : [32, 51, 28]
}

y = pd.DataFrame(x, index = ["a", "b", "c"])
print(y)


# In[32]:


import pandas as pd

x = {
    "names" : ["Joe", "Jacob", "Sarah"],
    "ages" : [32, 51, 28]
}

y = pd.DataFrame(x, index = ["a", "b", "c"])
print(y.loc["b"])


# In[33]:


import pandas as pd

x = pd.read_csv('data.csv')
print(x)


# In[ ]:




