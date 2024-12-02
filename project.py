
"""
TODO     
#pie chart for age of participants      ✓
#pie chart for sex of participants      ✓
histogram                               ✓
heatmap                                 ✓
is heatmap accurate?                     ✓
change colors for all graphs?            ✓
make sure everyting is mapped correctly  ✓

"""

# age, sex, and violent tendencies

###############################################################################
# IMPORTS
###############################################################################
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


#------------------------------------------------------------------------------


###############################################################################
# Creating dataframe and dataframe copies
###############################################################################
df1 = pd.read_csv("data.csv")
df2 = df1.copy()
df3 = df1.copy()
df4 = df1.copy()
X = df2
#------------------------------------------------------------------------------


###############################################################################
# age breakdown of participants
###############################################################################
###############################################################################
# age breakdown of participants
###############################################################################
def ageBreakdown():
    df4_age_map = {
        1:"12",
        2:"13",
        3:"14",
        4:"15",
        5:"16",
        6:"17",
        7:"18+"
        }
    colors = [
    '#0000FF',  # Blue
    '#1E90FF',  # DodgerBlue
    '#4169E1',  # RoyalBlue
    '#4682B4',  # SteelBlue
    '#5F9EA0',  # CadetBlue
    '#87CEEB',  # SkyBlue
    '#B0E0E6',  # PowderBlue
    ]
    
    df4['q1'] = df4['q1'].replace(df4_age_map)
    a = df4.groupby('q1').size()
    mylabels = ["12", "13", "14", "15", "16", "17", "18+"]
    exp_nums = [0.5, 0.5, 0.1, 0.1, 0.1, 0.1, 0.1]
    #print(a)
    plt.figure(figsize=(10,13))
    
    plt.pie(a, explode=exp_nums, labels=mylabels, labeldistance=0.7, colors=colors, shadow= True)
    plt.title("Age Breakdown of Participants")
    plt.legend(a)
    
    ## resources ##
    """
    https://www.w3schools.com/python/matplotlib_pie_charts.asp
    https://stackoverflow.com/questions/46542572/how-to-plot-pie-chart-using-data-frame-group-by-different-range
    https://www.freecodecamp.org/news/matplotlib-figure-size-change-plot-size-in-python/
    """
    plt.show()
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


###############################################################################
# sex breakdown of participants
###############################################################################
def sexBreakdown(): ## Pink & Blue
    df4_sex_map = {
        1:"male",
        2:"female"
        }
    colors = [
    '#0000FF',  # Blue
    'hotpink',  # Hotpink
    ]
    
    df4['q2'] = df4['q2'].replace(df4_sex_map)
    b = df4.groupby('q2').size()
    mylabels = ["male", "female"]
    
    
    plt.figure(figsize=(4,4))
    
    plt.pie(b, labels=mylabels, labeldistance=0.7, colors=colors)
    plt.title("Sex Breakdown of Participants")
    plt.legend(b)
    plt.show()
#------------------------------------------------------------------------------
    

###############################################################################
# how many female students brought weapons 4 or more days
###############################################################################
def possibleCorelationFemales():
    df4_sex_map = {
        1:"male",
        2:"female"
        }
    df4['q2'] = df4['q2'].replace(df4_sex_map)
    #plt.figure(figsize=(10,40))
    # start by seeing how many female participants exist in df
    #print("===============\n")
    female_participants = df4[df4['q2']=='female']
    
    #now  see how many of those female 
    weapons_4_or_more_days_females = female_participants[(female_participants['q12'] == 4) | (female_participants['q12'] == 5)]
    count = weapons_4_or_more_days_females.shape[0]
    
    
    #print(count)
    
    
    ## out of that number, how many got into frequent fights
    count2 = weapons_4_or_more_days_females[ (weapons_4_or_more_days_females['q17']==3) 
                                    | (weapons_4_or_more_days_females['q17']==4) 
                                    | (weapons_4_or_more_days_females['q17']==5) 
                                    | (weapons_4_or_more_days_females['q17']==6) 
                                    | (weapons_4_or_more_days_females['q17']==7)]
    count2 = count2.shape[0]
    #print(f"count 2 = {count2}")
    
    
    plt.bar('female sudents with weapons', count)
    plt.bar('weapons and fights', count2)
    
    plt.show()
    

    plt.figure(figsize=(8, 6))
    
    ### edit to make things accurate
#------------------------------------------------------------------------------


###############################################################################
# q12 graph
###############################################################################
def question12Graph():
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
    
    #------------------------------------------------------------------------------
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
    plt.show()
#------------------------------------------------------------------------------


###############################################################################
# q17 graph
###############################################################################
def question17Graph():
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
    #------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------


###############################################################################
# how many male students brought weapons 4 or more days
###############################################################################
def possibleCorelationMales():
    ## See how much male participants there are
    #print("===============\n")
    df4_sex_map = {
        1:"male",
        2:"female"
        }
    df4['q2'] = df4['q2'].replace(df4_sex_map)
    male_participants = df4[df4['q2']=='male']
    ## see how many males answered 4 or more days
    
    weapons_4_or_more_days_males = male_participants[(male_participants['q12'] == 4) | (male_participants['q12'] == 5)]
    count = weapons_4_or_more_days_males.shape[0]
    #print(count)
    
    count3 = weapons_4_or_more_days_males[
        (weapons_4_or_more_days_males['q17'] == 3) |
        (weapons_4_or_more_days_males['q17'] == 4) |
        (weapons_4_or_more_days_males['q17'] == 5) |
        (weapons_4_or_more_days_males['q17'] == 6) |
        (weapons_4_or_more_days_males['q17'] == 7)
    ]                                              
    count3 = count3.shape[0]
    
    plt.figure(figsize=(8, 6))
    plt.bar('male sudents with weapons', count)
    plt.bar('weapons and fights', count3)
    
    plt.show()
    

#------------------------------------------------------------------------------


###############################################################################
# age breakdown 2
###############################################################################
def pieChartAges():
    age_12 = (44/20005) * 100
    age_12 = round(age_12,2)
    age_13= (33/20005) * 100
    age_13 = round(age_13,2)
    age_14 = (2569/20005) * 100
    age_14 = round(age_14,2)
    age_15 = (5526/20005) * 100
    age_15 = round(age_15,2)
    age_16 = (5208/20005) * 100
    age_16 = round(age_16,2)
    age_17 = (4458/20005) * 100
    age_17= round(age_17,2)
    age_18= (2167/20005) * 100
    age_18 = round(age_18,2)
    y = np.array([age_12, age_13, age_14, age_15,age_16, age_17, age_18])
    mylabels = ['age 12','age 13','age 14','age 15','age 16','age 17', 'age 18 or older']
    plt.figure(figsize=(30,8))
    mycolors = [
    '#0000FF',  # Blue
    '#1E90FF',  # DodgerBlue
    '#4169E1',  # RoyalBlue
    '#4682B4',  # SteelBlue
    '#5F9EA0',  # CadetBlue
    '#87CEEB',  # SkyBlue
    '#B0E0E6',  # PowderBlue
    ]
    plt.pie(y, labels = mylabels, colors = mycolors, shadow = True)
    plt.title('Age Percenatage Breakdown')
    plt.legend(y)
    plt.figure(figsize=(4,5))
    
    plt.show()
#------------------------------------------------------------------------------


###############################################################################
# full histogram
###############################################################################
def hist():
    ### refrence code 
    """
    pyplot.hist(x, bins, alpha=0.5, label='x')
    pyplot.hist(y, bins, alpha=0.5, label='y')
    pyplot.legend(loc='upper right')
    pyplot.show()
    
    https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/
    https://seaborn.pydata.org/generated/seaborn.kdeplot.html
    """
    
    ### adapted code
    x = df4['q12']
    y = df4['q17']
    bins = 10
    sns.histplot(x, alpha=0.7, color='blue', bins=bins)
    sns.histplot(y, alpha=0.5, color='purple', bins=bins)
    
    plt.figure(figsize=(10, 6))
    plt.title('Correlation For Question 12')
    sns.kdeplot(x, alpha=0.7, color='blue')
    sns.kdeplot(y, alpha=0.7, color='purple')
    plt.show()
#------------------------------------------------------------------------------


###############################################################################
# heatmaps 
###############################################################################
def heatmap1():
    new_df = df1.drop('q5', axis=1)
    sns.heatmap(new_df.corr(), cmap='coolwarm', annot=True)
    plt.show()
    
def heatmap2():
    

        
    questionsToDrop = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'raceeth']
    df10 = df1.drop(questionsToDrop, axis=1)
    df10 = df10.dropna()
    sns.heatmap(df10.corr(method='spearman'), cmap='coolwarm', annot=True)
    plt.title('Heatmap corelation between all relevant questions in the Survey')
    plt.show()
#------------------------------------------------------------------------------

###############################################################################
# script 
###############################################################################

keepGoing = 'y'

while keepGoing == 'y':

    def displayMenu():
        print('Select 0 for Age Breakdown (Non-exploded graph)')
        print('Select 1 for Age Break Down')
        print('Select 2 for Sex Break Down')
        print('Select 3 for Analysis of female violent behavior')
        print('Select 4 for Analysis of Male violent behavior')
        print('Select 5 for Question 12 Data')
        print('Select 6 for Question 17 Data')
        print('Select 7 for Histogram')
        print('Select 8 for Heatmap 1')
        print('Select 9 for Heatmap 2')
        print('')
        
    def takeInput(number):
        if number == 0:
            print(f"you entered {number}")
            #load
            #do something
            pieChartAges()
        
        
        if number == 1:
            print(f"you entered {number}")
            #load
            #do something
            ageBreakdown()
            
        if number == 2:
            print(f"you entered {number}")
            #load
            #do something
            sexBreakdown()
        if number == 3:
            print(f"you entered {number}")
            #load
            #do something
            possibleCorelationFemales()
        if number == 4:
            print(f"you entered {number}")
            #load
            #do something
            possibleCorelationMales()
        if number == 5:
            print(f"you entered {number}")
            #load
            #do something
            question12Graph()
        if number == 6:
            print(f"you entered {number}")
            #load
            #do something
            question17Graph()
        if number == 7:
            print(f"you entered {number}")
            #load
            #do something
            hist()
        if number == 8:
            print(f"you entered {number}")
            #load
            #do something
            heatmap1()
        if number == 9:
            print(f"you entered {number}")
            #load
            #do something
            heatmap2()
        
            
    
    #userInput = 'y'
    displayMenu()
    A = int(input("\nWhat is your Selection?\t"))
    if A == 0 or A == 1 or A ==2 or A == 3 or A ==4 or A ==5 or A ==6 or A == 7 or A ==8 or A ==9:
        takeInput(A)
            
    else:
        print("invalid")
        continue 
    print('')
    keepGoing = input("continue?(y/n)")
