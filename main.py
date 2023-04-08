import pprint


# Read cook book from text file
def load_cook_book(filename):
    with open(filename, encoding='UTF-8') as file:
        cook_book = {}
        while True:
            # Read the dish name
            dish_name = file.readline().strip()
            # If the dish name is empty - we have read all dishes from the file
            if not dish_name:
                break
            # Read the number of ingredients
            ingredients_num = int(file.readline())
            # Read ingreadients for the current dish
            ingredients = []
            for i in range(ingredients_num):
                ingredient_info = file.readline().strip()
                ingredient_name, quantity, measure = ingredient_info.split('|')
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
            # Add dish to the cook book
            cook_book[dish_name] = ingredients
            # Read the empty line after each dish
            file.readline()
    return cook_book


cook_book = load_cook_book('recipes.txt')
pprint.pprint(cook_book, compact=True, width=100)