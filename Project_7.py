#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Setup Libraries


# In[2]:


conda install -c conda-forge jupyterthemes


# In[3]:


import jupyterthemes as jt


# In[ ]:


get_ipython().system('jt -l')


# In[ ]:


get_ipython().system('jt -t gruvboxd -h')


# In[4]:


cd C:\Users\joegi\Desktop\Project7_Data


# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import chart_studio.plotly as pl
import plotly.offline as of
import cufflinks as cf
import datetime as dt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


of.init_notebook_mode(connected = True)
cf.go_offline()


# In[7]:


#Load Datafiles


# In[8]:


donations = pd.read_csv("Donations.csv")


# In[9]:


donors = pd.read_csv("Donors.csv")


# In[10]:


projects = pd.read_csv("Projects.csv")


# In[11]:


resources = pd.read_csv("Resources.csv")


# In[12]:


schools = pd.read_csv("Schools.csv")


# In[13]:


teachers = pd.read_csv("Teachers.csv")


# In[14]:


#Describe and show data for column ideas


# In[15]:


print("Shape of donations dataframe is: ", donations.shape)
print("Shape of donors dataframe is: ", donors.shape)
print("Shape of projects dataframe is: ", projects.shape)
print("Shape of resources dataframe is: ", resources.shape)
print("Shape of schools dataframe is: ", schools.shape)
print("Shape of teachers dataframe is: ", teachers.shape)


# In[16]:


#Create new data by using the datasets


# In[17]:


data = pd.merge(donations, projects, how = "inner", on = "Project ID")


# In[18]:


data2 = pd.merge(data, donors, how = "inner", on = "Donor ID")


# In[19]:


data3 = pd.merge(data2, schools, how = "inner", on = "School ID")


# In[20]:


data4 = pd.merge(data3, teachers, how = "inner", on = "Teacher ID")


# In[21]:


a =  data4.columns.values.tolist()
a


# In[22]:


#Which 10 states have the most number of schools that opened projects to gather donations? Bar Plot


# In[23]:


s = schools["School State"].value_counts().sort_values(ascending = False).head(10)
s


# In[24]:


s.iplot(kind='bar', xTitle='states', yTitle='Number of Schools', title='Top 10 states with schools involved in projects')


# In[25]:


s2 = data4.groupby('School State')['Donation Amount'].mean().sort_values(ascending=False).head(10)


# In[26]:


s2.iplot(kind='bar', xTitle='State', yTitle='Average donation per Project', title='Top 10 Schools w/Avg', colorscale='paired')


# In[27]:


#Analyze mean, median, mode, 25/75 percentiles


# In[37]:


mean = np.mean(donations['Donation Amount'])
percentiles = np.percentile(data4['Donation Amount'].dropna(), [25,75])
minimum = data4['Donation Amount'].dropna().min
maximum = data4['Donation Amount'].dropna().max

print ('Mean donation amount is: ', np.round(mean,2))
print ('Max donation amount is: ', maximum,2)
print ('Min donation amount is: ', minimum,2)
print ('Percentile donation amount is: ', percentiles)


# In[44]:


s3 = data4.groupby('Donor State')['Donation ID'].count().sort_values(ascending= False).head(15)


# In[47]:


s3.iplot(kind='bar', xTitle='State', yTitle='Number of donations', title = 'Donations count', colorscale='')


# In[ ]:














