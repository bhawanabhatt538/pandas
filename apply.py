# Student Alcohol Consumption
# Introduction:¶
# This time you will download a dataset from the UCI.

# Step 1. Import the necessary libraries
# In [ ]:
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called df.
# In [ ]:
df=pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv')
print(df)

# Step 4. For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column
# In [ ]:
print(df.loc[:,'school':'guardian'].to_string())

# Step 5. Create a lambda function that will capitalize strings.
# In [ ]
capitalizer=lambda x: x.capitalize()

# Step 6. Capitalize both Mjob and Fjob
# In [ ]:
print(df['Mjob'].apply(capitalizer))
print(df['Fjob'].apply(capitalizer))

# Step 7. Print the last elements of the data set.
# In [ ]:
print(df.tail())

# Step 8. Did you notice the original dataframe is still lowercase? Why is that? Fix it and capitalize Mjob and Fjob.
# In [ ]:
print(df['Mjob'].apply(capitalizer))
print(df['Fjob'].apply(capitalizer))
print(df.tail())
# Step 9. Create a function called majority that returns a boolean value to a new column called legal_drinker (Consider majority as older than 17 years old)
# In [ ]:
def majority(x):
    if x>17:
        return True
    else:
        return False

df['legal_drinker']=df['age'].apply(majority)
print(df['legal_drinker'])
print(df.head())

# In [ ]:

# Step 10. Multiply every number of the dataset by 10.
# I know this makes no sense, don't forget it is just an exercise
# In [ ]:

# In [ ]:
def multiplyby10(x):
    if type(x) is int:
        return x*10
    else:
        return x

print(df.applymap(multiplyby10).head())
