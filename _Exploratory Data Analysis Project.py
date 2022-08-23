#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd


# In[52]:


df = pd.read_csv("US_Accidents_Dec21_updated.csv")


# In[53]:


df.head()


# In[54]:


df.info()


# In[55]:


df.describe().T


# In[56]:


numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

numeric_df = df.select_dtypes(include=numerics)
len(numeric_df.columns)


# In[57]:


missing_percentages = df.isnull().sum().sort_values(ascending=False) / len(df)


# In[58]:


missing_percentages


# In[59]:


type(missing_percentages)


# In[60]:


missing_percentages[missing_percentages != 0].plot(kind='barh')


# #### Exploratory Analysis and Visualization
# #### Columns we'll analyze:
# 
# 1.City
# 2.Start Time
# 3.Start Lat, Start Lng
# 4.Temperature
# 5.Weather Condition

# In[61]:


df.columns


# #### City

# In[62]:


df.City


# In[63]:


cities = df.City.unique()


# In[64]:


len(cities)


# In[65]:


cities_by_accident = df.City.value_counts()
cities_by_accident


# In[66]:


cities_by_accident[:20]


# In[67]:


type(cities_by_accident)


# In[68]:


cities_by_accident[:20].plot(kind='barh')


# In[69]:


import seaborn as sns
sns.set_style("darkgrid")


# In[70]:


sns.histplot(cities_by_accident, log_scale=True)


# In[71]:


cities_by_accident[cities_by_accident == 1]


# #### Start Time

# In[72]:


df.Start_Time


# In[73]:


df.Start_Time = pd.to_datetime(df.Start_Time)


# In[74]:


sns.distplot(df.Start_Time.dt.hour, bins=24, kde=False, norm_hist=True)


# In[75]:


sns.distplot(df.Start_Time.dt.dayofweek, bins=7, kde=False, norm_hist=True)


# In[76]:


sundays_start_time = df.Start_Time[df.Start_Time.dt.dayofweek == 6]
sns.distplot(sundays_start_time.dt.hour, bins=24, kde=False, norm_hist=True)


# In[77]:


monday_start_time = df.Start_Time[df.Start_Time.dt.dayofweek == 0]
sns.distplot(monday_start_time.dt.hour, bins=24, kde=False, norm_hist=True)


# In[81]:


df_2019 = df[df.Start_Time.dt.year == 2019]
df_2019_Bing = df_2019[df_2019.Source == 'MapQuest']
sns.distplot(df_2019_Bing.Start_Time.dt.month, bins=12, kde=False, norm_hist=True)


# In[50]:


df.Source.value_counts().plot(kind='pie')


# #### Start Latitude & Longitude

# In[82]:


df.Start_Lat


# In[83]:


df.Start_Lng


# In[84]:


sample_df = df.sample(int(0.1 * len(df)))


# In[85]:


sns.scatterplot(x=sample_df.Start_Lng, y=sample_df.Start_Lat, size=0.001)


# In[ ]:




