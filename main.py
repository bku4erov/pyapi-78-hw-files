import pprint


# Read cook book from text file
def load_cook_book(filename):
    with open(filename, encoding='UTF-8') as file:
        cook_book = {}
        while True:
            dish_name = file.readline().strip()
            ingredients_num = int(file.readline())
            ingredients = []
            for i in range(ingredients_num):
                ingredient_info = file.readline()
                ingredient_name, quantity, measure = ingredient_info.split('|')
                ingredients.append({'ingredient_name': ingredient_name.strip(), 'quantity': quantity.strip(), 'measure': measure.strip()})
            cook_book[dish_name] = ingredients
            if ingredient_info[-1] == '\n':
                file.readline()
            else:
                break
    return cook_book


cook_book = load_cook_book('recipes.txt')
pprint.pprint(cook_book, compact=True, width=100)