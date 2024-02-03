recipes = [
    {
        'name': 'Зелье лечения',
        'ingredients': {
            'Вода': 1,
            'Соль': 1,
            'Лесной гриб': 5
        }
    },
    {
        'name': 'Зелье маны',
        'ingredients': {
            'Вода': 1,
            'Пещерный гриб': 11
        }
    },
    {
        'name': 'Зелье полета',
        'ingredients': {
            'Крыло мухи': 8,
            'Зелье маны': 8,
            'Экстракт бабочки': 1
        }
    }
]

user_ingredients = input("Введите ингредиенты через пробел: ").split()

def check_recipes(user_ingredients):
    matching_recipes = []
    for recipe in recipes:
        is_matching = True
        for ingredient, quantity in recipe['ingredients'].items():
            if ingredient not in user_ingredients or user_ingredients.count(ingredient) < quantity:
                is_matching = False
                break
        if is_matching:
            matching_recipes.append(recipe['name'])
    return matching_recipes

matching_recipes = check_recipes(user_ingredients)
if len(matching_recipes) > 0:
    print("Совпадающие рецепты:")
    for recipe in matching_recipes:
        print(recipe)
else:
    print("Нет совпадающих рецептов.")