import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

chipo=pd.read_csv('../datafile/data_chipotle.tsv', sep='\t')
print(chipo)

prices=[float(value[1:-1]) for value in chipo.item_price]#****what is this

print(prices)
chipo.item_price= prices
print(chipo.item_price)

print('\n\n\n\n')

#delete duplicate item

chipo_filtered = chipo.drop_duplicates(['item_name','quantity','choice_description'])
print(chipo_filtered)

chipo.one_prod=chipo_filtered[chipo_filtered.quantity == 1]
print(chipo.one_prod)

chipo.query(price_per_item>10).item_name.nunique()
