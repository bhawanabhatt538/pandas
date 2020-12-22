# Step 1. Import the necessary libraries
# In [ ]:
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called drinks.
# In [ ]:
# drinks=pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')
# print(drinks)
# print(drinks.columns)
# # Step 4. Which connent drinks more beer on average?
# # In [ ]:
# avgPerContinet=drinks.groupby('continent').beer_servings.mean().sort_values(ascending=False).head(1)
# print(avgPerContinet)
# #I.E
# # Step 5. For each continent print the statistics for wine consumption.
# # In [ ]:
# print(drinks.groupby('continent').wine_servings.describe())
# # Step 6. Print the mean alcohol consumption per continent for every column
# # In [ ]:
# print('\n\n')
# print(drinks.groupby('continent').mean())
# # Step 7. Print the median alcohol consumption per continent for every column
# # In [ ]:
# print(drinks.groupby('continent').median())
# # Step 8. Print the mean, min and max values for spirit consumption.
# # This time output a DataFrame
# print(drinks.groupby('spirit_servings').agg(['mean','min','max']))

# Step 1. Import the necessary libraries
# In [ ]:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called users.
# In [ ]:
users=pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user',sep='|')
print(users)
# Step 4. Discover what is the mean age per occupation
# In [ ]:
print('mean age per occupation=\n',users.groupby('occupation').age.mean())
# Step 5. Discover the Male ratio per occupation and sort it from the most to the least
# In [ ]:
#for this we create function
def gender_to_numeric(x):
    if x=='M':
        return 1
    else:
        0

# apply the function to the gender column and create a new column
users['gender_n'] = users['gender'].apply(gender_to_numeric)


a = users.groupby('occupation').gender_n.sum() / users.occupation.value_counts() * 100

# sort to the most male
print(a.sort_values(ascending = False))


print('\n\n')

# Step 6. For each occupation, calculate the minimum and maximum ages
# In [ ]:
print(users.groupby('occupation').age.agg([min,max]))


# Step 7. For each combination of occupation and gender, calculate the mean age
# In [ ]:
print(users.groupby(['occupation','gender']).age.mean())

# Step 8. For each occupation present the percentage of women and men
# In [ ]:
# create a data frame and apply count to gender

gender_ocup = users.groupby(['occupation','gender']).agg({'gender':'count'})
print(gender_ocup)

# create a DataFrame and apply count for each occupation

occup_count = users.groupby(['occupation']).agg('count')
print(occup_count)
# divide the gender_ocup per the occup_count and multiply per 100
occup_gender = gender_ocup.div(occup_count, level = 'occupation') * 100
print(occup_gender)

# present all rows from the 'gender column'
occup_gender.loc[: , 'gender']
print(occup_gender.loc[:,'gender'])
