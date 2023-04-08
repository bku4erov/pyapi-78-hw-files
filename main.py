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

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            shop_list.setdefault(ingredient['ingredient_name'], {'measure': ingredient['measure'], 'quantity': 0})
            shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return shop_list


cook_book = load_cook_book('recipes.txt')
print('Кулинарная книга:')
pprint.pprint(cook_book, compact=True, width=100)
print()

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
print(f'Список покупка для приготовления блюд {", ".join(dishes)} на {person_count} персон(ы):')
pprint.pprint(shop_list, compact=True, width=100)