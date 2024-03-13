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
            'Морковь': 2,
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
        is_matching = True
        for ingredient, quantity in recipe['ingredients'].items():
            if ingredient not in user_ingredients or user_ingredients.count(ingredient) < quantity:
                is_matching = False

        if is_matching:
            matching_recipes.append(recipe['name'])
    return matching_recipes

while True:
    user_choice = input("Введите '1' для вывода списка рецептов или '2' для проверки ингредиентов: ")
    if user_choice == '1':
        print_recipes_menu()

    elif user_choice == '2':
        user_ingredients = input("Введите ингредиенты через пробел: ").split()
        matching_recipes = check_recipes(user_ingredients)
        if len(matching_recipes) > 0:
            print("Совпадающие рецепты:")
            for recipe in matching_recipes:
                print(recipe)
        else:
            print("Нет совпадающих рецептов.")

    else:
        print("Неверный ввод. Пожалуйста, введите '1' или '2'.")