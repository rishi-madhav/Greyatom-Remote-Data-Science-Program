# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path,delimiter = ",",skip_header = 1)
print(data)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census = np.concatenate((data,new_record),axis=0)

print(census)
#Code starts here



# --------------
#Code starts here
age = np.array(census[:,0])
print(age)
max_age = np.max(age)
print(max_age)
min_age = np.min(age)
print(min_age)
age_mean = np.mean(age)
print(age_mean)
age_std = np.std(age)
print(age_std)



# --------------
#Code starts here
race_0 = census[census[:,2] == 0]
print(race_0)
race_1 = census[census[:,2] == 1]
print(race_1)
race_2 = census[census[:,2] == 2]
print(race_2)
race_3 = census[census[:,2] == 3]
print(race_3)
race_4 = census[census[:,2] == 4]
print(race_4)

len_0 = len(race_0)
print(len_0)
len_1 = len(race_1)
print(len_1)
len_2 = len(race_2)
print(len_2)
len_3 = len(race_3)
print(len_3)
len_4 = len(race_4)
print(len_4)

len_array = ([len_0,len_1,len_2,len_3,len_4])
print(len_array)

minority_race = len_array.index(min(len_array))
#for number in len_array:
 #  if minority_race > number:
  #    minority_race = number
print(minority_race)



# --------------
#Code starts here
senior_citizens = census[census[:,0]>60]
print(senior_citizens)

working_hours_sum = senior_citizens.sum(axis=0)[6]
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = np.mean(high[:,7]==1)
print(avg_pay_high)
avg_pay_low = np.mean(low[:,7]==1)
print(avg_pay_low)
print(avg_pay_high > avg_pay_low)


