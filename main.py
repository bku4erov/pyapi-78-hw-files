import os
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

# Merge files to one file
def merge_files(file_list, result_file_name, encoding='UTF-8'):
    content = []
    for file_name in file_list:
        with open(file_name, encoding=encoding) as file:
            file_content = file.readlines()
            content.append({'file_name': file_name, 'lines': file_content, 'lines_count': len(file_content)})
    content.sort(key=lambda file_info: file_info['lines_count'])
    with open(result_file_name, 'wt', encoding=encoding) as result_file:
        for file_content in content:
            result_file.writelines(os.path.basename(file_content['file_name']) + '\n')
            result_file.writelines(str(file_content['lines_count']) + '\n')
            result_file.writelines(file_content['lines'])
            # To start next file section from new line
            if file_content['lines'][-1][-1] != '\n':
                result_file.writelines('\n')


cook_book = load_cook_book('recipes.txt')
print('Кулинарная книга:')
pprint.pprint(cook_book, compact=True, width=100)
print()

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
print(f'Список покупка для приготовления блюд {", ".join(dishes)} на {person_count} персон(ы):')
pprint.pprint(shop_list, compact=True, width=100)

file_list = [os.path.join('files', '1.txt'), os.path.join('files', '2.txt'), os.path.join('files', '3.txt')]
merge_files(file_list, os.path.join('files', 'merged.txt'))