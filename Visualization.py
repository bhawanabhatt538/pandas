# Step 1. Import the necessary libraries
# In [1]:
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# # set this so the graphs open internally
# %matplotlib inline
# Step 2. Import the dataset from this address.
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
# Step 3. Assign it to a variable called chipo.
# In [ ]:
chipo = pd.read_csv(url, sep = '\t' )


# # Step 4. See the first 10 entries
# # In [ ]:
# print(chipo.head(10))

# Step 5. Create a histogram of the top 5 items bought
# In [ ]:
x = chipo.item_name
print(x)

print('\n\n')
letter_counts = Counter(x)
print(letter_counts)

print('\n\n')

df = pd.DataFrame.from_dict(letter_counts, orient='index')
print(df)

print('\n\n')
df = df[0].sort_values(ascending = True)[45:50]
print(df)

df.plot(kind='bar')
plt.xlabel('Items')
plt.ylabel('Number of Times Ordered')
plt.title('Most ordered Chipotle items')
plt.show()
#


# Step 6. Create a scatterplot with the number of items orderered per order price
# Hint: Price should be in the X-axis and Items ordered in the Y-axis¶

# create a list of prices
chipo.item_price = [float(value[1:-1]) for value in chipo.item_price] # strip the dollar sign and trailing space
print(float(value[1:-1]))

# then groupby the orders and sum
orders = chipo.groupby('order_id').sum()

# creates the scatterplot
# plt.scatter(orders.quantity, orders.item_price, s = 50, c = 'green')
plt.scatter(x = orders.item_price, y = orders.quantity, s = 50, c = 'green')

# Set the title and labels
plt.xlabel('Order Price')
plt.ylabel('Items ordered')
plt.title('Number of items ordered per order price')
plt.ylim(0)
plt.show()
