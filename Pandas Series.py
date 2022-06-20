#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

x = [10, 24, 39]

y = pd.Series(x)
print(y)


# In[11]:


import pandas as pd

x = [1, 2, 7]

y = pd.Series(x)
print(y[1])


# In[13]:


import pandas as pd

x = [2, 6, 9]

y = pd.Series(x, index = ["a", "b", "c"])
print(y)


# In[15]:


import pandas as pd

x = [2, 6, 9]

y = pd.Series(x, index = ["a", "b", "c"])
print(y["c"])


# In[16]:


import pandas as pd

x = {"day1" : 420, "day2" : 380, "day3" : 390}

y = pd.Series(x)
print(y)


# In[18]:


import pandas as pd

x = {"day1" : 420, "day2" : 380, "day3" : 390}

y = pd.Series(x, index = ["day1", "day2"])
print(y)

