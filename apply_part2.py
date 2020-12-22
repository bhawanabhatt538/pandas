import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv')
print(df)

print(df.head())

print(df.info())

print(df.columns)


df.Year=pd.to_datetime(df.Year,format='%Y')
print(df.info())
print(df.head())

# Step 6. Set the Year column as the index of the dataframe
# In [ ]:

df = df.set_index('Year' , drop = True)
print(df.head())

# Step 7. Delete the Total column
# In [ ]:

df.pop('Total')
print(df.head())

# Step 8. Group the year by decades and sum the values
# Pay attention to the Population column number, summing this column is a mistake
# In [ ]:

# Uses resample to sum each decade
#crimes = crime.resample('10AS').sum()
df=df.resample('10AS').sum()
print(df)
# Uses resample to get the max value only for the "Population" column
#population = crime['Population'].resample('10AS').max()

population = df['Population'].resample('10AS').max()


# Updating the "Population" column
# crimes['Population'] =
df['Population'] = population
print(df)
# Step 9. What is the most dangerous decade to live in the US?
#In [276]:

print(df.idxmax(0))











# Step 9. What is the most dangerous decade to live in the US?
# In [ ]:
