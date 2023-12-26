#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


real_estate_df=pd.read_excel(r"C:\Users\USER\Documents\Chat GPT Projects\RAW DATA\Real Estate\Real_Estate_Dataset.xlsx")


# In[3]:


real_estate_df.head()


# In[4]:


# Market Trends Over Time
# We'll first convert the transaction dates to just months and years for a clearer trend analysis
real_estate_df['Transaction Year-Month'] = real_estate_df['Transaction Date'].dt.to_period('M')


# In[5]:


# Grouping by Year-Month to see average prices over time
monthly_avg_prices = real_estate_df.groupby('Transaction Year-Month')['Transaction Price ($)'].mean()


# In[6]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


# Setting the style for the plots
sns.set(style="whitegrid")

# Plotting the trend
plt.figure(figsize=(12, 6))
monthly_avg_prices.plot(kind='line', marker='o')
plt.title('Average Property Price Trend Over Time')
plt.xlabel('Year-Month')
plt.ylabel('Average Transaction Price ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[8]:


# Price Fluctuations
# Plotting the distribution of transaction prices

plt.figure(figsize=(10, 6))
sns.histplot(real_estate_df['Transaction Price ($)'], bins=30, kde=True)
plt.title('Distribution of Property Prices')
plt.xlabel('Transaction Price ($)')
plt.ylabel('Frequency')
plt.show()


# In[9]:


# Impact of Location on Property Values
# Calculating average price for each location

avg_price_by_location = real_estate_df.groupby('Location')['Transaction Price ($)'].mean().sort_values()


# In[10]:


# Plotting
plt.figure(figsize=(10, 6))
avg_price_by_location.plot(kind='bar')
plt.title('Average Property Price by Location')
plt.xlabel('Location')
plt.ylabel('Average Transaction Price ($)')
plt.show()


# In[11]:


# Size vs. Price Analysis
# Scatter plot to show the relationship between property size and price

plt.figure(figsize=(10, 6))
sns.scatterplot(data=real_estate_df, x='Size (sqft)', y='Transaction Price ($)')
plt.title('Property Size vs Transaction Price')
plt.xlabel('Size (sqft)')
plt.ylabel('Transaction Price ($)')
plt.show()


# In[12]:


# Correlation Analysis: Economic Indicators and Property Prices
correlation_matrix = real_estate_df[['Transaction Price ($)', 'Regional Avg Income ($)', 'Regional Unemployment Rate (%)']].corr()


# In[13]:


# Plotting the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix: Economic Indicators and Property Prices')
plt.show()


# In[ ]:




