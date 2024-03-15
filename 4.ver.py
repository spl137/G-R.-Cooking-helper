recipes = [
    {
        'name': 'Рагу из мяса жуков',
        'ingredients': {
            'квест': 1,
        }
    },
    {
        'name': 'Суп из ползуна',
        'ingredients': {
            'стражи': 1,
        }
    },
    {
        'name': 'Жареное мясо G1',
        'ingredients': {
            'мясо': 1,
        }
    },
    {
        'name': 'Суп из корней',
        'ingredients': {
            'жители': 1,
        }
    },
    {
        'name': 'Уха',
        'ingredients': {
            'Эдд': 1,
        }
    },
    {
        'name': 'Жареное мясо G2',
        'ingredients': {
            'Мясо': 1,
        }
    },
    {
        'name': 'Дымящаяся мясная похлебка',
        'ingredients': {
            'Яркендар': 1,
        }
    },
    {
        'name': 'Похлебка',
        'ingredients': {
            'Хильда': 1,
        }
    },
    {
        'name': 'Похлебка Теклы',
        'ingredients': {
            'квест "Похлебка"': 1,
        }
    },
    {
        'name': 'Тушеное мясо',
        'ingredients': {
            'Вино': 1,
            'морковь': 2,
            'Жареное мясо': 1,
            'Рис': 1,
        }
    },
    {
        'name': 'Рагу из мясного жука',
        'ingredients': {
            'Молоко': 1,
            'Жареный мясной жук': 1,
        }
    },
    {
        'name': 'Большое мясное рагу',
        'ingredients': {
            'Сырое мясо': 5,
            'Лук': 1,
            'Картофель': 1,
        }
    }
]

def print_recipes_menu():
    print("Доступные рецепты:")
    for recipe in recipes:
        print(f"- {recipe['name']}")
def check_recipes(user_ingredients):
    matching_recipes = []
    for recipe in recipes:
        if all(any(ingredient_keyword.lower() in ingredient.lower() for ingredient in recipe['ingredients']) for ingredient_keyword in user_ingredients):
            matching_recipes.append(recipe)
    return matching_recipes

def search_recipes_by_name(keywords):
    matching_recipes = []
    for recipe in recipes:
        if any(keyword.lower() in recipe['name'].lower() for keyword in keywords):
            matching_recipes.append(recipe)
    return matching_recipes

while True:
    user_choice = input("Введите '1' для вывода списка рецептов, '2' для проверки ингредиентов или '3' для поиска по названию: ")
    if user_choice == '1':
        print_recipes_menu()
    elif user_choice == '2':
        user_ingredients = input("Введите ингредиентов через пробел: ").split()
        matching_recipes = check_recipes(user_ingredients)
        if matching_recipes:
            print("Совпадающие рецепты:")
            for recipe in matching_recipes:
                print(f"{recipe['name']}: {', '.join(recipe['ingredients'])}")
        else:
            print("Нет совпадающих рецептов.")
    elif user_choice == '3':
        keywords = input("Введите название рецепта: ").split()
        matching_recipes = search_recipes_by_name(keywords)
        if matching_recipes:
            print("Найденные рецепты:")
            for recipe in matching_recipes:
                print(f"{recipe['name']}: {', '.join(recipe['ingredients'])}")
        else:
            print("Рецепты не найдены.")
    else:
        print("Неверный ввод. Пожалуйста, введите '1', '2' или '3'.")