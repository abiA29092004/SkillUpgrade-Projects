# -*- coding: utf-8 -*-
"""EDA.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vWjbmDvPxqgFD2msf2MW4AFQuhAXbh3A
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import seaborn as sns

import io
df = pd.read_csv(io.BytesIO(uploaded['Automobile_data.csv']))

df.head()

df.tail()

df.describe()

df.shape

df.columns

df.nunique()

df.isnull().sum()

Automobile=df.drop(['bore','stroke'], axis=1)
Automobile.head()

sns.pairplot(Automobile)

sns.distplot(Automobile['engine-size'])

sns.distplot(Automobile['engine-size'],bins=5)

sns.catplot(x='engine-size',kind='box',data=Automobile)