# Investor - Flow of Funds - US
# Introduction:
# Special thanks to: https://github.com/rgrp for sharing the dataset.

# Step 1. Import the necessary libraries
# In [ ]:
import pandas as pd

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called¶
# In [ ]:
df = pd.read_csv('https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv')
print(df)
# Step 4. What is the frequency of the dataset?
# In [ ]:

# Step 5. Set the column Date as the index.
# In [ ]:
print(df.set_index('Date'))
# Step 6. What is the type of the index?
# In [ ]:
print(df.index)

# Step 7. Set the index to a DatetimeIndex type
# In [ ]:
df.index = pd.to_datetime(df.index)
type(df.index)

# Step 8. Change the frequency to monthly, sum the values and assign it to monthly.
# In [ ]:

monthly = df.resample('M').sum()
print(monthly)
# Step 9. You will notice that it filled the dataFrame with months that don't have any data with NaN. Let's drop these rows.
# In [ ]:
monthly = monthly.dropna()
print(monthly)
# Step 10. Good, now we have the monthly data. Now change the frequency to year.
# In [ ]:
year = monthly.resample('AS-JAN').sum()
print(year)
# BONUS: Create your own question and answer it.
# In [ ]:
