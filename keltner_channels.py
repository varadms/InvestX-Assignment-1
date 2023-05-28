#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import yfinance as yf
from matplotlib import pyplot as plt


# In[2]:


def calculate_keltner_channels(df, period=20, multiplier=2):
    typical_price = (df['High'] + df['Low'] + df['Close']) / 3

    middle_band = typical_price.rolling(window=period).mean()
    atr = df['High'].rolling(window=period).max() - df['Low'].rolling(window=period).min()
    upper_band = middle_band + (multiplier * atr)
    lower_band = middle_band - (multiplier * atr)

    return middle_band, upper_band, lower_band


# In[4]:


df = yf.download('TCS.NS' , start = '2021-05-23' , end = '2023-05-23')
df = calculate_keltner_channels(df)


# In[13]:


plt.figure(figsize=(1, 1))
plt.plot(df.index, df['Close'], color='black', label='Close')
plt.plot(upper_band.index, upper_band, color='blue', label='Upper Band')
plt.plot(lower_band.index, lower_band, color='red', label='Lower Band')
plt.fill_between(upper_band.index, upper_band, lower_band, color='gray', alpha=0.2)
plt.title('Keltner Channels')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




