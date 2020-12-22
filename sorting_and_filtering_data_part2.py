# Ex2 - Filtering and Sorting Data
# This time we are going to pull data directly from the internet.

# Step 1. Import the necessary libraries
# In [ ]:
import pandas as pd


# Step 2. Import the dataset from this address.

euro12 = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv', sep=',')

# Step 3. Assign it to a variable called euro12.

# In [ ]:
print(euro12)

# Step 4. Select only the Goal column.
# In [ ]:
print(euro12['Goals'])
# Step 5. How many team participated in the Euro2012?
# In [ ]:
print('team participated in the Euro12=',euro12.shape[0])

# Step 6. What is the number of columns in the dataset?
# In [ ]:
print(euro12.shape[1])

# Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
# In [ ]:
discipline=euro12[['Team','Yellow Cards','Red Cards']]
print(discipline)

print('\n\n')
# Step 8. Sort the teams by Red Cards, then to Yellow Cards
# In [ ]:
print(discipline.sort_values(['Red Cards','Yellow Cards'],ascending= False))

# Step 9. Calculate the mean Yellow Cards given per Team
# In [ ]:

print('the mean Yellow Cards given per Team=',round(discipline['Yellow Cards'].mean()))

# Step 10. Filter teams that scored more than 6 goals
# In [ ]:

# Step 11. Select the teams that start with G
# In [ ]:

# Step 12. Select the first 7 columns
# In [ ]:

# Step 13. Select all columns except the last 3.
# In [ ]:

# Step 14. Present only the Shooting Accuracy from England, Italy and Russia
# In [ ]:
