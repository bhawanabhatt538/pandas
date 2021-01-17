# Pokemon
# Introduction:
# This time you will create the data.

# Step 1. Import the necessary libraries
# In [ ]:
import pandas as pd
# Step 2. Create a data dictionary that looks like the DataFrame below
# In [3]:
raw_data = {"name": ['Bulbasaur', 'Charmander','Squirtle','Caterpie'],
            "evolution": ['Ivysaur','Charmeleon','Wartortle','Metapod'],
            "type": ['grass', 'fire', 'water', 'bug'],
            "hp": [45, 39, 44, 45],
            "pokedex": ['yes', 'no','yes','no']
            }
# Step3. Assign it to a variable called pokemon¶
# In [5]:
pokemon = pd.DataFrame(raw_data)
print(pokemon.head())

print('\n\n')

# Out[5]:
# evolution   hp  name    pokedex type
# 0   Ivysaur 45  Bulbasaur   yes grass
# 1   Charmeleon  39  Charmander  no  fire
# 2   Wartortle   44  Squirtle    yes water
# 3   Metapod 45  Caterpie    no  bug
# Step 4. Ops...it seems the DataFrame columns are in alphabetical order. Place the order of the columns as name, type, hp, evolution, pokedex
# In [ ]:
pokemon = pokemon[['name', 'type','hp','evolution','pokedex']]
print(pokemon)
# Step 5. Add another column called place, and insert what you have in mind.
# In [ ]:
print('\n\n')
pokemon['place'] = ['park' , 'street' , 'lake' , 'forest']
print(pokemon)

print('\n\n')
# Step 6. Present the type of each column
# In [ ]:
print(pokemon.dtypes)
# BONUS: Create your own question and answer it.
# In [ ]:
