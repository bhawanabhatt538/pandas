# Step 1. Import the necessary libraries
# In [ ]:
import pandas as pd
import numpy as np

# Step 2. Import the first dataset cars1 and cars2.
# Step 3. Assign each to a variable called cars1 and cars2
# In [ ]:
cars1= pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv")
cars2= pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv")
print(cars1.head())
print(cars2.head())
print(cars1.columns)
print(cars2.columns)
# Step 4. Oops, it seems our first dataset has some unnamed blank columns, fix cars1
# In [ ]:
cars1=cars1.loc[: , 'mpg':'car']
print(cars1)

print(cars1.columns)


# Step 5. What is the number of observations in each dataset?
# In [ ]:
print('shape of cars 1 is=',cars1.shape)
print('shape of cars 2 is=',cars2.shape)

# Step 6. Join cars1 and cars2 into a single DataFrame called cars
# In [ ]:
cars = cars1.append(cars2)
print(cars.to_string())

# Step 7. Oops, there is a column missing, called owners. Create a random number Series from 15,000 to 73,000.
# In [ ]:'1'
owners = np.random.randint(15000, high = 73001 ,size = 398 ,dtype = 'I' )
print(owners)

# Step 8. Add the column owners to cars
# In [ ]:
cars['owners'] = owners
print(cars.tail())


