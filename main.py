from tkinter import Tk
from title import Title
from risen import Risen
from g1 import G1
from g2 import G2
from g3 import G3
from randoms import Randoms
from search import Search
import json
import random

global title, risen, g1, g2, g3, search, randoms

with open('recipes.json', 'r', encoding='utf-8') as file:
    recipes_data = json.load(file)


def check_recipes(user_ingredients):
    matching_recipes = []
    for recipe in recipes_data:
        if any(ingredient_keyword.lower() in ingredient.lower() for ingredient_keyword in user_ingredients for
               ingredient in recipe['ingredients']):
            matching_recipes.append(recipe)
    return matching_recipes


def search_recipes_by_name(keywords):
    matching_recipes = []
    for recipe in recipes_data:
        if any(keyword.lower() in recipe['name'].lower() for keyword in keywords):
            matching_recipes.append(recipe)
        else:
            for ingredient in recipe['ingredients']:
                if any(keyword.lower() in ingredient.lower() for keyword in keywords):
                    matching_recipes.append(recipe)
                    break
    return matching_recipes


def generate_random_ingredients(number_of_ingredients=3):
    all_ingredients = set()
    for recipe in recipes_data:
        for ingredient in recipe['ingredients']:
            all_ingredients.add(ingredient)
    return random.sample(list(all_ingredients), number_of_ingredients)


def find_recipes_with_random_ingredients():
    random_ingredients = generate_random_ingredients()
    return check_recipes(random_ingredients)


def find_optimal_recipes_by_cost(budget):
    sorted_recipes = sorted(recipes_data, key=lambda x: x['hp'], reverse=True)
    selected_recipes = []
    total_cost = 0

    for recipe in sorted_recipes:
        recipe_cost = int(recipe['cost'])
        if total_cost + recipe_cost <= budget:
            selected_recipes.append(recipe)
            total_cost += recipe_cost

    return selected_recipes


def show_title():
    global title, risen, g1, g2, g3, search, randoms
    randoms.pack_forget()
    risen.pack_forget()
    g1.pack_forget()
    g2.pack_forget()
    g3.pack_forget()
    search.pack_forget()
    title.pack(fill='both', expand=True)


def show_randoms():
    global title, risen, g1, g2, g3, search, randoms
    title.pack_forget()
    risen.pack_forget()
    g1.pack_forget()
    g2.pack_forget()
    g3.pack_forget()
    search.pack_forget()
    randoms.pack(fill='both', expand=True)


def show_risen():
    global title, risen, g1, g2, g3, search, randoms
    randoms.pack_forget()
    title.pack_forget()
    g1.pack_forget()
    g2.pack_forget()
    g3.pack_forget()
    search.pack_forget()
    risen.pack(fill='both', expand=True)


def show_g1():
    global title, risen, g1, g2, g3, search, randoms
    randoms.pack_forget()
    title.pack_forget()
    risen.pack_forget()
    g2.pack_forget()
    g3.pack_forget()
    search.pack_forget()
    g1.pack(fill='both', expand=True)


def show_g2():
    global title, risen, g1, g2, g3, search, randoms
    randoms.pack_forget()
    title.pack_forget()
    risen.pack_forget()
    g1.pack_forget()
    g3.pack_forget()
    search.pack_forget()
    g2.pack(fill='both', expand=True)


def show_g3():
    global title, risen, g1, g2, g3, search, randoms
    randoms.pack_forget()
    title.pack_forget()
    risen.pack_forget()
    g1.pack_forget()
    g2.pack_forget()
    search.pack_forget()
    g3.pack(fill='both', expand=True)


def show_search():
    global title, risen, g1, g2, g3, search, randoms
    randoms.pack_forget()
    title.pack_forget()
    risen.pack_forget()
    g1.pack_forget()
    g2.pack_forget()
    g3.pack_forget()
    search.pack(fill='both', expand=True)


root = Tk()
root.title("Gothic/Risen. Cooking helper")
root.geometry("720x480")
root.configure(bg="#FFFFFF")

title = Title(root, show_risen, show_g1, show_g2, show_g3, show_search, show_randoms, find_optimal_recipes_by_cost)
risen = Risen(root, show_title)
g1 = G1(root, show_title)
g2 = G2(root, show_title)
g3 = G3(root, show_title)
search = Search(root, show_title, search_recipes_by_name)
randoms = Randoms(root, show_title, find_optimal_recipes_by_cost, recipes_data, check_recipes)

show_title()

root.resizable(False, False)
root.mainloop()
