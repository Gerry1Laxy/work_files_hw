import os


def get_cook_book(file_name: str) -> dict:
    cookbook = dict()
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            dish = line.strip()
            cookbook[dish] = []
            for _ in range(int(file.readline())):
                ingredient = file.readline().strip().split(' | ')
                cookbook[dish].append({
                    'ingredient_name': ingredient[0],
                    'quantity': int(ingredient[1]),
                    'measure': ingredient[2]
                })
            file.readline()
    return cookbook


def get_shop_list_by_dishes(dishes: list, person_count: int, cookbook: dict) -> dict:
    shop_dict = dict()
    for dish in dishes:
        if dish in cookbook:
            for ingredient in cookbook[dish]:
                ingredient_name = ingredient['ingredient_name']
                if ingredient_name in shop_dict:
                    shop_dict[ingredient_name]['quantity'] += (
                            ingredient['quantity']
                            * person_count
                    )
                else:
                    shop_dict[ingredient_name] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
    return shop_dict


if __name__ == '__main__':
    dir_file = r'cook_book\file'
    name_file = 'recipes.txt'
    path_to_file = os.path.join(dir_file, name_file)

    cook_book = get_cook_book(path_to_file)

    assert (
            get_shop_list_by_dishes(['Омлет', 'Омлет'], 1, cook_book)
            == get_shop_list_by_dishes(['Омлет'], 2, cook_book)
    )

    shopping_list = get_shop_list_by_dishes(
        ['Омлет', 'Утка по-пекински', 'Фахитос'], 1, cook_book
    )

    print(shopping_list)
    print(cook_book)
