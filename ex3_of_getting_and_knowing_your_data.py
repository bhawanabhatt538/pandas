# Step 1. Import the necessary libraries
# In [ ]:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called users and use the 'user_id' as index
# In [ ]:
df=pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep='|',index_col='user_id')
print(df)
print('\n\n\n')

# Step 4. See the first 25 entries
# In [ ]:
print(df.head(25))
print('\n\n\n')



# Step 6. What is the number of observations in the dataset?
# In [ ]:
print('the no.of observation=',df.shape[0])
print('\n\n\n')
# Step 7. What is the number of columns in the dataset?
# In [ ]:
print('the no. of columns in dataset=',df.shape[1])
print('\n\n\n')

# Step 8. Print the name of all the columns.
# In [ ]:
print(df.columns)
print('\n\n\n')
# Step 9. How is the dataset indexed?
# In [ ]:
print(df.index)
print('\n\n\n')
# Step 10. What is the data type of each column?
# In [ ]:
print(df.dtypes)
print('\n\n\n')

# Step 11. Print only the occupation column
# In [ ]:
print(df.occupation)
print('\n\n\n')
# Step 12. How many different occupations are in this dataset?
# In [ ]:
print(df.occupation.nunique())
print('\n\n\n')
# Step 13. What is the most frequent occupation?
# In [ ]:
print(df.occupation.value_counts().head(1).index[0])
print('\n\n\n')
# Step 14. Summarize the DataFrame.
# In [ ]:
print(df.describe())
print('\n\n\n')
# Step 15. Summarize all the columns
# In [ ]:
print(df.describe(include = 'all'))

print('\n\n\n')
# Step 16. Summarize only the occupation column
# In [ ]:
print(df.occupation.describe())
print('\n\n\n')
# Step 17. What is the mean age of users?
# In [ ]:
print('mean age of users=',df.age.mean())
print('\n\n\n')
# Step 18. What is the age with least occurrence?
# In [ ]:
print('age with least occurrence=',df.age.value_counts().tail())
