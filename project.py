# Name:          Jalyn Perry
# Course:        B104
# Assignment:    ICE 12_2

## Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


## Creating dataframe and dataframe copy
df1 = pd.read_csv("data.csv")
df2 = df1.copy()


X = df2

#print(df2.head())



countForQuestion12 = df2['q12'].value_counts()
print(countForQuestion12) 

countForQuestion17 = df2['q17'].value_counts()
print(countForQuestion17) 







