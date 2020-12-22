# Step 1. Import the necessary libraries
# In [ ]:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Step 2. Import the dataset from this address.

# Step 3. Assign it to a variable called chipo.
# In [ ]:
chipo=pd.read_csv("../datafile/data_chipotle.tsv", sep='\t')
print(chipo)

print('\n\n')
# Step 5. What is the price of each item?
print(chipo.item_price)

prices = [float(value[1:-1]) for value in chipo.item_price]
print(prices)

prices=[float(value[1:-1]) for value in chipo.item_price]
chipo.item_price=prices
print(chipo)

#delete the item_name and quantity
chipo_filtered=chipo.drop_duplicates(['item_name','quantity','choice_description'])
print(chipo_filtered)

# select only the products with quantity equals to 1
chipo_one_prod=chipo_filtered[chipo_filtered.quantity==1]
print('product with one quantity=','\n',chipo_one_prod)
chipo[(chipo['item_name'] == 'Chicken Bowl') & (chipo['quantity'] == 1)]
#Step 5. What is the price of each item?
print('price of each item','\n',chipo[(chipo['item_name']=='Chicken Bowl')&(chipo['quantity']==1)])

# print a data frame with only two columns item_name and item_price
# In [ ]:

# Step 6. Sort by the name of the item
# In [ ]:
print(chipo.item_name.sort_values())
# Step 7. What was the quantity of the most expensive item ordered?
# In [ ]:
print(chipo.sort_values(by='item_price',ascending=False).head(1))

# Step 8. How many times was a Veggie Salad Bowl ordered?
# In [ ]:
chipo_salad=chipo[chipo.item_name=='Veggie Salad Bowl']
print('chipo item name ordered in =',len(chipo_salad))
# Step 9. How many times did someone order more than one Canned Soda?
# In [ ]:
chipo_canned=chipo[(chipo.item_name=='Canned Soda') & (chipo.quantity>1)]
print(len(chipo_canned))
