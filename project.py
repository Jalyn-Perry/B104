# Name:          Jalyn Perry
# Course:        B104
# Assignment:    ICE 12_2

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df1 = pd.read_csv("data.csv")
df2 = df1.copy()


X = df2

print(df2.head())

columns_to_drop = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "raceeth"]
df3 = df2.drop(columns_to_drop, axis=1, inplace=True)
#sample_df = df3.sample(n=2)

# Plotting Area Plot
plt.figure(figsize=(80, 60))

df2.plot(kind='area', stacked=False)
plt.title('Area Plot')
plt.xlabel('q12')
plt.ylabel('q17')

plt.show()








