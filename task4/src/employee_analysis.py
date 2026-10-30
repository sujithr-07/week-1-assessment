#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np

df= pd.read_csv("../data/employees.csv")
print("Data shape:",df.shape)
display(df.head())


# In[7]:


df.info()
display(df.describe())
print("MIssing values:\n",df.isna().sum())


# In[8]:


# department analysis. employee headcount and average salary for each department


# In[9]:


department_summary=(
    df.groupby("department")
    .agg(
        headcount=("id","count"),
        average_salary=("salary","mean"),
        maximum_salary=("salary","max")
    )
    .reset_index()
)

display(department_summary)


# In[10]:


# filtering empolyees earning above 50000 and wroking in chennai


# In[11]:


high_earners= df[df["salary"] > 50000]
chennai_employees= df[df["city"] == "Chennai"]
print("high earners:")
display(high_earners)

print("employees in chennai:")
display(chennai_employees)


# In[12]:


#performance measurement
#using %timeit magic command


# In[14]:


get_ipython().run_line_magic('timeit', 'df.groupby("department")["salary"].mean()')


# In[ ]:





# In[ ]:




