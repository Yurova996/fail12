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


##################################

with open('text/1.txt', 'r', encoding='utf-8') as file1, \
     open('text/2.txt', 'r', encoding='utf-8') as file2,\
     open('text/3.txt', 'r', encoding='utf-8') as file3,\
     open('text/resul.txt', 'a+', encoding='utf-8') as file_result:
    def lines_file(file_):
        line_file = file_.readlines()
        file_info = ['\n' + file_.name + '\n', str(len(line_file)) + '\n']
        return file_info + line_file

    list_files = [lines_file(file1), lines_file(file2), lines_file(file3)]
    r = sorted(list_files, key=len)
    result_text = r[0] + r[1] + r[2]
    for line in result_text:
        file_result.write(line)