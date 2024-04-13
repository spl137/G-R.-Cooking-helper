import json
import random

with open('recipes.json', 'r', encoding='utf-8') as file:
    recipes = json.load(file)

def print_recipes_menu():
    print("Доступные рецепты:")
    for recipe in recipes:
        print(f"- {recipe['name']} (Восстановление здоровья: {recipe['health_recovery']}, Стоимость: {recipe['cost']}, Ингредиенты: {', '.join(recipe['ingredients'])}")

def check_recipes(user_ingredients):
    matching_recipes = []
    for recipe in recipes:
        if any(ingredient_keyword.lower() in ingredient.lower() for ingredient_keyword in user_ingredients for ingredient in recipe['ingredients']):
            matching_recipes.append(recipe)
    return matching_recipes

def search_recipes_by_name(keywords):
    matching_recipes = []
    for recipe in recipes:
        if any(keyword.lower() in recipe['name'].lower() for keyword in keywords):
            matching_recipes.append(recipe)
    return matching_recipes

def generate_random_ingredients(number_of_ingredients=3):
    all_ingredients = set()
    for recipe in recipes:
        for ingredient in recipe['ingredients']:
            all_ingredients.add(ingredient)
    return random.sample(list(all_ingredients), number_of_ingredients)

def find_recipes_with_random_ingredients():
    random_ingredients = generate_random_ingredients()
    print(f"Случайный набор ингредиентов: {', '.join(random_ingredients)}")
    return check_recipes(random_ingredients)

while True:
    user_choice = input("Введите '1' для вывода списка рецептов, '2' для проверки ингредиентов, '3' для поиска по названию, '5' для генерации случайного набора ингредиентов, '4' для выхода из программы: ")
    if user_choice == '1':
        print_recipes_menu()
    elif user_choice == '2':
        user_ingredients = input("Введите ингредиентов через пробел: ").split()
        matching_recipes = check_recipes(user_ingredients)
        if matching_recipes:
            print("Совпадающие рецепты:")
            for recipe in matching_recipes:
                print(f"{recipe['name']} (Восстановление здоровья: {recipe['health_recovery']}, Стоимость: {recipe['cost']}): {', '.join(recipe['ingredients'])}")
        else:
            print("Нет совпадающих рецептов.")
    elif user_choice == '3':
        keywords = input("Введите название рецепта: ").split()
        matching_recipes = search_recipes_by_name(keywords)
        if matching_recipes:
            print("Найденные рецепты:")
            for recipe in matching_recipes:
                print(f"{recipe['name']} (Восстановление здоровья: {recipe['health_recovery']}, Стоимость: {recipe['cost']}): {', '.join(recipe['ingredients'])}")
        else:
            print("Рецепты не найдены.")
    elif user_choice == '5':
        matching_recipes = find_recipes_with_random_ingredients()
        if matching_recipes:
            print("Рецепты, которые можно приготовить из случайного набора ингредиентов:")
            for recipe in matching_recipes:
                print(f"{recipe['name']} (Восстановление здоровья: {recipe['health_recovery']}, Стоимость: {recipe['cost']}): {', '.join(recipe['ingredients'])}")
        else:
            print("Нет рецептов для данного набора ингредиентов.")
    elif user_choice == '4':
        print("Выход из программы.")
        break
    else:
        print("Неверный ввод. Введите 1, 2, 3, 5, 4.")
