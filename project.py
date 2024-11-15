# Name:          Jalyn Perry
# Course:        B104
# Assignment:    ICE 12_2

#TODO -> seperate graphs, create pie chats (compring gender to question 12 and another comparing gender to question 17) plot that correlates), create heat map for all questions. create histogram.. create bar charts


## Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



## Creating dataframe and dataframe copy
df1 = pd.read_csv("data.csv")
df2 = df1.copy()


X = df2

#print(df2.head())



countForQuestion12 = df2['q12'].value_counts()
print(countForQuestion12) 

countForQuestion17 = df2['q17'].value_counts()
print(countForQuestion17) 




# plot question 12
plt.subplot(1, 1, 1)
ax = sns.countplot(x='q12', data=X)
plt.title('question 12', fontsize=25)
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height() + 105), ha='center', va='top', color='black', fontsize=10)
#plt.tight_layout()
     # how many days did you carry weapon
     # 0 days 
     # 1 day
     # 2 days
     # 4 or 5 days
     # 6 or more

    
# # plot question 17
# plt.subplot(1, 1, 1)
# ax = sns.countplot(x='q17', data=X)
# plt.title('question 17', fontsize=25)
# for p in ax.patches:
#     ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height() + 105), ha='center', va='top', color='black', fontsize=10)
#      # how many days did you fight
#      #
#      #
#      #
#      #
#      #
#      #
# plt.tight_layout()
# plt.show()



# #plot question 1
# plt.subplot(1, 1, 1)
# ax = sns.countplot(x='q1', data=X)
# plt.title('age', fontsize=25)
# for p in ax.patches:
#     ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height() + 25), ha='center', va='top', color='black', fontsize=10)
    
#         # opt 1 - 12 or younger
#         # opt 2 - 13
#         # opt 3   14
#         # opt 4 = 15
#         # opt 5 = 16
#         # opt 6 = 17
#         # opt 7 = 18+


plt.scatter()



