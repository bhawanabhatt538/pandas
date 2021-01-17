# Apple Stock
# Introduction:
# We are going to use Apple's stock price.

# Step 1. Import the necessary libraries
# In [ ]:
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Step 2. Import the dataset from this address
# In [ ]:
data = ('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv')
# Step 3. Assign it to a variable apple
# In [ ]:
df = pd.read_csv(data)
print(df.head())

print('\n\n')
# Step 4. Check out the type of the columns
# In [ ]:
print(df.dtypes)
# Step 5. Transform the Date column as a datetime type
# In [ ]:
print('\n\n')
df.Date = pd.to_datetime(df.Date)
print(df.dtypes)
# Step 6. Set the date as the index
# In [ ]:
print('\n\n')
df = df.set_index('Date')
print(df)
# Step 7. Is there any duplicate dates?
# In [ ]:
print(df.index.is_unique)
# Step 8. Ops...it seems the index is from the most recent date. Make the first entry the oldest date.
# In [ ]:
print('\n')
print(df.sort_index(ascending=True).head())

print('\n\n')
# Step 9. Get the last business day of each month
# In [ ]:
print(df.resample('BM').mean().head())
# Step 10. What is the difference in days between the first day and the oldest
# In [ ]:
print('\n\n')
print('difference in days between the first day and the oldest=',(df.index.max()-df.index.min()).days)
# Step 11. How many months in the data we have?
# In [ ]:
df.months = df.resample('bm').mean()
print(len(df.months.index))
# Step 12. Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches
# In [ ]:
df_open = df['Adj Close'].plot(title = "Apple Stock")

# changes the size of the graph
fig = df_open.get_figure()
fig.set_size_inches(13.5, 9)
plt.show()
# BONUS: Create your own question and answer it.
# In [ ]:
