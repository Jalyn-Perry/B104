# Name:          Jalyn Perry
# Course:        B104
# Assignment:    ICE 12_2

#TODO -> create pie chats (compring gender to question 12 and another comparing gender to question 17) plot that correlates), create heat map for all questions. create histogram.. create bar charts

###############################################################################
# IMPORTS
###############################################################################
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


###############################################################################
# Creating dataframe and dataframe copies
###############################################################################
df1 = pd.read_csv("data.csv")
df2 = df1.copy()
df3 = df1.copy()
df4 = df1.copy()
X = df2

# print(df2.head())
# countForQuestion1 = df2['q1'].value_counts()
# print(countForQuestion1)
# filtered_df = df2.query('= q17')
# print(filtered_df)
# countForQuestion12 = df2['q12'].value_counts()
# print(countForQuestion12) 
# countForQuestion17 = df2['q17'].value_counts()
# print(countForQuestion17) 


###############################################################################
# age breakdown of participants
###############################################################################
df4_age_map = {
    1:"12",
    2:"13",
    3:"14",
    4:"15",
    5:"16",
    6:"17",
    7:"18+"
    }

df4['q1'] = df4['q1'].replace(df4_age_map)
a = df4.groupby('q1').size()
mylabels = ["12", "13", "14", "15", "16", "17", "18+"]
exp_nums = [0.5, 0.5, 0.1, 0.1, 0.1, 0.1, 0.1]
#print(a)
plt.figure(figsize=(10,13))

plt.pie(a, explode=exp_nums, labels=mylabels, labeldistance=0.7)
plt.title("Age Breakdown")
plt.legend(a)

## resources ##
"""
https://www.w3schools.com/python/matplotlib_pie_charts.asp
https://stackoverflow.com/questions/46542572/how-to-plot-pie-chart-using-data-frame-group-by-different-range
https://www.freecodecamp.org/news/matplotlib-figure-size-change-plot-size-in-python/
"""


###############################################################################
# sex breakdown of participants
###############################################################################
df4_sex_map = {
    1:"male",
    2:"female"
    }

df4['q2'] = df4['q2'].replace(df4_sex_map)
b = df4.groupby('q2').size()
mylabels = ["male", "female"]
exp_nums = [0.5, 0.5]
plt.figure(figsize=(4,4))

plt.pie(b, labels=mylabels, labeldistance=0.7)
plt.legend(b)


#pie chart for age of participants ✓
#pie chart for sex of participants ✓

###############################################################################
# how many female students brought weapons 4 or more days
###############################################################################

# start by seeing how many female participants exist in df
print("===============\n")
female_participants = df4[df4['q2']=='female']

#now  see how many of those female 
weapons_4_or_more_days = female_participants[female_participants['q12']==4] 
count = weapons_4_or_more_days.shape[0]


print(count)
plt.bar('female sudents with weapons', count, 4, 4)
plt.show()


## out of that number, how many got into frequent fights
count2 = weapons_4_or_more_days[weapons_4_or_more_days['q17']=='1']
count2 = count2.shape[0]
print(f"count 2 = {count2}")
### edit to make things accurate






# how many female students fought more than 5 times in a year

# how many male students brought weapons 4 or more days
# how many male students fought more than 5 times in a year

# comparisons of question 17 to question 12 (if a student answered question 12 one way, were they more likely to answer question 17 a certian way)


############
##  test  ##
############


###############################################################################
# "fixing question 12"
###############################################################################
q12_map = {
    1.0 : "0 days",
    2.0 : "1 day",
    3.0 : "2 days",
    4.0 : "4 or 5 days",
    5.0 : "6+days",

    }


df2['q12'] = df2['q12'].replace(q12_map)


###############################################################################
# plot question 12
###############################################################################

plt.figure()
plt.subplot(1, 1, 1)
ax = sns.countplot(x='q12', data=X)
plt.title('How many days did you bring a weapon to school?', fontsize=15)
plt.xlabel("# of students who answered...") 
plt.ylabel("Number of days bringing weapon to school") 
#format graph
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height() + 805), ha='center', va='top', color='black', fontsize=10)
#plt.tight_layout()
      # how many days did you carry weapon
      # 0 days 
      # 1 day
      # 2 days
      # 4 or 5 days
      # 6 or more


###############################################################################
#fixing question 17
###############################################################################

q17_map = {
1.0: "0 ", 
2.0: "1 ", 
3.0: "2 or 3 ",
4.0: "4 or 5 ", 
5.0: "6 or 7 ", 
6.0: "8 or 9 ", 
7.0: "10 or 11 ",
8.0: "12 +",
    }
df3['q17'] = df3['q17'].replace(q17_map)
###############################################################################
# plot question 17
###############################################################################

plt.figure()
plt.subplot(1, 1, 1)
ax = sns.countplot(x='q17', data=df3)
plt.title('How many fights have you been in (last 12 months)', fontsize=25)
plt.xlabel("# of students who answered...") 
plt.ylabel("Number of fights") 
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height() + 655), ha='center', va='top', color='black', fontsize=8)

plt.show()







