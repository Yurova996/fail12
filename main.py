with open('data.txt') as file:
     cook_book = {}
     for line in file:
        recipes_name = line.strip()
        ingredients_count = int(file.readline())
        cook_book.setdefault(recipes_name,[])

        for _ in range(ingredients_count):
            ing = file.readline().strip().split(' | ')
            name_ingredient, quantity, measure = ing
            ingredient_book = {'ingredient_name': name_ingredient , 'ingredients_count': quantity, 'ingredients': measure}
            cook_book[recipes_name].append(ingredient_book)
        file.readline()


print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    menu = {}

    for dish, ingred in cook_book.items():
        if dish in dishes:
            for i in ingred:
                a = i.get('ingredient_name')
                i.pop('ingredient_name')
                if a not in menu.keys():
                    menu[a] = i
                    i['quantity'] *= person_count
                else:
                    menu[a]['quantity'] += i['quantity']
    print(menu)
    return


