# -*- coding: utf-8 -*-
"""
Created on Sun May 28 22:16:01 2017

@author: kande
"""

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('finn4.csv', encoding='utf-8')
print(df)

df['Price'] =df['Price'].astype(int)
#if not '':

#df['Area'] =df['Area'].astype(int)

#if not 'NaN':
    #df['bedroom'] =df['bedroom'].astype(int)
df.info()

df.plot(kind= 'scatter', x='Price', y='Area')
plt.show()
df.describe()
mean= df['Price'].mean()
print(mean)
_=sns.swarmplot(x='Price', y='Area', data=df)

plt.show()

