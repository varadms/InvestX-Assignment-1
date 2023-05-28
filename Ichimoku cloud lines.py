#!/usr/bin/env python
# coding: utf-8

# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import yfinance as yf
from matplotlib import pyplot as plt


# In[11]:


def calculate_ichimoku_cloud(df, conversion_period=9, base_period=26, leading_span_b_period=52, displacement=26):
    df['ConversionLine'] = (df['High'].rolling(window=conversion_period).max() + df['Low'].rolling(window=conversion_period).min()) / 2
    df['BaseLine'] = (df['High'].rolling(window=base_period).max() + df['Low'].rolling(window=base_period).min()) / 2
    df['LeadingSpanA'] = ((df['ConversionLine'] + df['BaseLine']) / 2).shift(displacement)
    df['LeadingSpanB'] = ((df['High'].rolling(window=leading_span_b_period).max() + df['Low'].rolling(window=leading_span_b_period).min()) / 2).shift(displacement)
    df['LaggingSpan'] = df['Close'].shift(-displacement)
    
    return df


# In[14]:


df = yf.download('TCS.NS' , start = '2021-05-23' , end = '2023-05-23')
df = calculate_ichimoku_cloud(df)


# In[20]:


plt.figure(figsize=(9, 10))
plt.subplot(2 , 1 ,1)
plt.title('Ichimoku cloud lines')
plt.plot( df['ConversionLine'] , label = 'ConversionLine')
plt.plot(  df['LaggingSpan'] , label = 'LaggingSpan')
plt.plot( df['BaseLine'] , label = 'BaseLine')
plt.plot(  df['LeadingSpanA'] , label = 'LeadingSpanA')
plt.plot(  df['LeadingSpanB'] , label = 'LeadingSpanB')
plt.axhline(0 , color = 'black')
plt.legend()
plt.show()


# In[ ]:




