# Pet store calculator created for Big Ol' Pets, Chicago, IL
# Created by Bess Hambleton, Oct. 2024
# Contact: bhambleton@yearup.org

# Current number of cats to be fed
num_cats = int(input('How many cats need to be fed today? '))

# Cat food currently in inventory
cat_food = {
    'fromm': int(input('How much Fromm do we have? ')), 
    'purina': int(input('How much Purina do we have? ')), 
    'kirkland': int(input('How muck Kirkland cat food in inventory? '))
    }

# Each cat receives an estimated 1/10 of a bag of food.
cats_fed = num_cats * .1  

# Confirming current number of cats and available inventory
print(f'Number of cats: {num_cats}')
print(f'Cat food in stock: {cat_food}')

# Taking cat food from inventory by order of preference:
if cat_food['kirkland'] > 0:
    cat_food['kirkland'] = cat_food['kirkland'] - (cats_fed)
elif cat_food['fromm'] > 0:
    cat_food['fromm'] = cat_food['fromm'] - (cats_fed)
else:
    cat_food['purina'] = cat_food['purina'] - (cats_fed)

#Final inventory
print(f'After feeding the cats: {cat_food}')
