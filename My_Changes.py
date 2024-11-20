import matplotlib.pyplot as plt
import numpy as np



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
mylabels = ['age 12:0.2%','age 13:0.16%','age 14:12.84%','age 15:27.62%','age 16:26.03%','age 17:22.28%', 'age 18 or older:10.83%']
plt.figure(figsize=(30,8))
plt.pie(y, labels = mylabels)
plt.legend(y)
plt.figure(figsize=(4,5))
plt.show()





