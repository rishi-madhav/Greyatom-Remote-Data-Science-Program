# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
data['Gender'].replace('-','Agender', inplace=True)
#print(data)

gender_count = data['Gender'].value_counts()
print(gender_count)

gender_count.plot(kind='bar')
plt.xlabel('Gender')
plt.ylabel('Gender Count')
plt.show()

#Code starts here 




# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
print(alignment)
#labels = ['good','bad','neutral']
#colors = ['gold', 'yellowgreen', 'lightcoral']
#sizes = 
#explode = (0.1, 0, 0)  # explode 1st slice
#label = 'Character Alignment'
plt.pie(alignment)
plt.title('Character Alignment')
plt.show()


# --------------
#Code starts here
sc_df = data[['Strength', 'Combat']]
sc_covariance = sc_df.Strength.cov(sc_df.Combat)
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()
sc_pearson = sc_covariance/(sc_combat*sc_strength)
print("The Pearson's coefficient for Strength and Combat variables is :", sc_pearson)

ic_df = data[['Intelligence', 'Combat']]
ic_covariance = ic_df.Intelligence.cov(ic_df.Combat)
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()
ic_pearson = ic_covariance/(ic_combat*ic_intelligence)
print("The Pearson's coefficient for Intelligence and Combat variables is :", ic_pearson)




# --------------
#Code starts here
total_high = data['Total'].quantile(0.99)
print(total_high)
super_best = data[data['Total'] > total_high]
#print(super_best)

super_best_names = list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
f, (ax_1, ax_2, ax_3) = plt.subplots(3,figsize=(15,5))
f.suptitle("Survival of the fittest", fontsize=12)
#print(super_best.head())

ax_1.boxplot(super_best['Intelligence'])
ax_1.set_title('Intelligence')

ax_2.boxplot(super_best['Speed'])
ax_2.set_title('Speed')

ax_3.boxplot(super_best['Power'])
ax_3.set_title('Power')


