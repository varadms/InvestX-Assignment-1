#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import yfinance as yf
from matplotlib import pyplot as plt


# In[46]:


def calculate_ease_of_movement(df):
    lookback_period=14
    df[high_low_avg] = (df['High'] + df['Low']) / 2
    df[diff] = df[high_low_avg].diff(1)
    df[box_ratio] = df['Volume'] / ((df['High'] - df['Low'])*1000000)
    df[ease_of_movement] = df[diff] / df[box_ratio]
    df[ease_of_movement_smoothed] = df[ease_of_movement].rolling(window=lookback_period).mean()
    return df


# In[ ]:





# In[48]:


df = yf.download('TCS.NS' , start = '2021-05-23' , end = '2023-05-23')
df = calculate_ease_of_movement(df)


# In[ ]:





# In[49]:


plt.figure(figsize=(10, 6))
plt.subplot(2 , 1 ,1)
plt.title('ease of movement')
plt.plot( df['ease_of_movement_smoothed'] , label ='emv_movement' )
plt.axhline(0 , color = 'black')
plt.legend()
plt.show()


# In[ ]:




