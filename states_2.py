# Step 1. Import the necessary libraries
# In [ ]:
import pandas as pd
import datetime

print('\n\n')
# Step 2. Import the dataset from this address

data_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data'
# Step 3. Assign it to a variable called data and replace the first 3 columns by a proper datetime index.
# In [ ]:
data = pd.read_csv(data_url,sep='\s+',parse_dates=[[0,1,2]])
print(data)
# Step 4. Year 2061? Do we really have data from this year? Create a function to fix it and apply it.
# In [ ]:

def fix_century(x):
    year = x.year - 100 if x.year > 1989 else x.year
    return datetime.date(year, x.month, x.day)

data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_century)
print(data)

print('\n\n')
# Step 5. Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns].
# In [ ]:
data['Yr_Mo_Dy'] = pd.to_datetime(data['Yr_Mo_Dy'])
data = data.set_index('Yr_Mo_Dy')
print(data.head())


print('\n\n')
# Step 6. Compute how many values are missing for each location over the entire record.
# They should be ignored in all calculations below.
# In [ ]:
print(data.isnull().sum())

print('\n\n')
# Step 7. Compute how many non-missing values there are in total.
# In [ ]:
print(data.shape[0]-data.isnull().sum())
#OR
print('\n\n')
print(data.notnull().sum())

print('\n\n')
# Step 8. Calculate the mean windspeeds of the windspeeds over all the locations and all the times.
# A single number for the entire dataset.
# In [ ]:
print(data.sum().sum()/data.notnull().sum().sum())

print('\n\n')
# Step 9. Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days
# A different set of numbers for each location.
# In [ ]:
print(data.describe(percentiles=[]))
# Step 10. Create a DataFrame called day_stats and calculate the min, max and mean windspeed and standard deviations of the windspeeds across all the locations at each day.
# A different set of numbers for each day.
# In [ ]:
print('\n\n')
day_stats = pd.DataFrame()

day_stats['min'] = data.min(axis=1)
day_stats['max'] = data.max(axis = 1) # max
day_stats['mean'] = data.mean(axis = 1) # mean
day_stats['std'] = data.std(axis = 1) # standard deviations

print(day_stats.head())#
print('\n\n')
# Step 11. Find the average windspeed in January for each location.
# Treat January 1961 and January 1962 both as January.
# In [ ]:
print('average windspeed in January for each location=\n\n',data.loc[data.index.month == 1].mean())

print('\n\n')
# Step 12. Downsample the record to a yearly frequency for each location.
# In [ ]:
print(data.groupby(data.index.to_period('A')).mean())

# Step 13. Downsample the record to a monthly frequency for each location.
# In [ ]:
print(data.groupby(data.index.to_period('M')).mean())
# Step 14. Downsample the record to a weekly frequency for each location.
# In [ ]:
print('\n\n')
print(data.groupby(data.index.to_period('W')).mean())
# Step 15. Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 52 weeks.
# In [ ]:
print('\n\n')
weekly = data.resample('W').agg(['min','max','mean','std'])
print(weekly)
weekly.loc[weekly.index[1:53], "RPT":"MAL"] .head(10)

print('\n\n')
