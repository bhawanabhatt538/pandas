#GETTING AND KNOWING YOUR DATA :

#Step 1. Import the necessary libraries
import pandas as pd
import numpy as np


chipo=pd.read_csv('../datafile/data_chipotle.tsv', sep='\t')
print(chipo)

# see the first 10 entries
print('the first 10 entries are;','\n',chipo.head(10))

#no of observations
print('no. of observations:',chipo.shape[0])

#info of data
print(chipo.info())

print('\n\n\n')

print('no. of columns in dataset:',chipo.shape[1])

print('\n')

print('name of columns in dataset:','\n', chipo.columns)

print('\n')

print('dataset index are:','\n',chipo.index)

print('\n')

print('most ordered item:','\n',chipo.groupby('item_name').sum().sort_values(['quantity'],ascending=False).head(1))

print('\n')

print('most ordered item in choice_description column-','\n',chipo.groupby('choice_description').sum().sort_values(['quantity'],ascending=False).head(1))

print('\n')

print('total items ordered=',chipo.quantity.sum())

print('\n')

#turn the item price into a float

#Check the item price type
print(chipo.item_price.dtype)

#Create a lambda function and change the type of item price

dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer)
print(chipo.item_price.dtype)



revenue=(chipo['quantity'] * chipo['item_price']).sum()
print('Revenue was:$'+str(np.round(revenue,2)))


print('order were made in the period=','\n',chipo.order_id.value_counts().count())

