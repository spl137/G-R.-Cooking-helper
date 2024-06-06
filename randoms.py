from tkinter import Frame, Canvas, Button, PhotoImage, Entry, Text
from pathlib import Path
import json
import random
def relative_to_assets(path: str) -> Path:
    return Path("assets/randoms") / Path(path)

class Randoms(Frame):
    def __init__(self, master, switch_function, find_optimal_recipes_by_cost_func, recipes_data, check_recipes_func):
        super().__init__(master)
        self.switch_function = switch_function
        self.find_optimal_recipes_by_cost_func = find_optimal_recipes_by_cost_func
        self.recipes = recipes_data
        self.check_recipes = check_recipes_func
        self.create_widgets()

    def combined_button_action(self):
        self.display_random_ingredients()
        self.find_recipes_with_random_ingredients()
    def generate_random_ingredients(self, number_of_ingredients=3):
        all_ingredients = set()
        for recipe in self.recipes:
            for ingredient in recipe['ingredients']:
                all_ingredients.add(ingredient)
        return random.sample(list(all_ingredients), number_of_ingredients)

    def find_recipes_with_random_ingredients(self):
        ingredients_text = self.entry_2.get('1.0', 'end-1c')
        random_ingredients = ingredients_text.split(', ')
        matching_recipes = self.check_recipes(random_ingredients)
        if matching_recipes:
            result = "\n".join([f"{recipe['name']} (Получаемый эффект: {recipe['health_recovery']}, Стоимость: {recipe['cost']}): {', '.join(recipe['ingredients'])}"for recipe in matching_recipes])
        else:
            result = "Нет рецептов для данного набора ингредиентов."
        self.entry_1.delete('1.0', 'end')
        self.entry_1.insert('1.0', result)
    def display_random_ingredients(self):
        random_ingredients = self.generate_random_ingredients()
        ingredients_text = ', '.join(random_ingredients)
        self.entry_2.delete(1.0, 'end-1c')
        random_ingredients = ingredients_text.split(', ')
        self.entry_2.insert(1.0, ', '.join(random_ingredients))
    def find_optimal_recipes_by_cost(self):
        cost = self.entry_3.get()
        if not cost.strip():
            self.entry_1.delete(1.0, 'end')
            self.entry_1.insert(1.0, 'Введите сумму')
        else:
            budget = int(self.entry_3.get())
            optimal_recipes = self.find_optimal_recipes_by_cost_func(budget)
            result = "\n".join([f"{recipe['name']} (Восстановление здоровья: {recipe['health_recovery']}, Стоимость: {recipe['cost']}): {', '.join(recipe['ingredients'])}" for recipe in optimal_recipes])
            self.entry_1.delete(1.0, 'end')
            self.entry_1.insert(1.0, result)

    def create_widgets(self):
        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=480,
            width=720,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_1 = canvas.create_image(
            360.0,
            245.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.image_2 = canvas.create_image(
            367.0,
            294.0,
            image=self.image_image_2
        )

        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = canvas.create_image(
            5690.0,
            594.5,
            image=self.entry_image_1
        )
        self.entry_1 = Text(
            canvas,
            bd=0,
            bg="#472D0E",
            font='Neucha',
            fg="#ffffff",
            highlightthickness=0,
            wrap="word"
        )
        self.entry_1.place(
            x=108.0,
            y=220.0,
            width=500.0,
            height=210.0
        )

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_function,
            relief="flat"
        )
        self.button_1.place(
            x=22.0,
            y=17.0,
            width=39.0,
            height=38.0
        )

        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        self.image_4 = canvas.create_image(
            380.0,
            40.0,
            image=self.image_image_4
        )


        self.entry_2 = Text(
            canvas,
            bd=0,
            bg="#472D0E",
            font='Neucha',
            fg="#ffffff",
            highlightthickness=0
        )
        self.entry_2.place(
            x=105.0,
            y=156.0,
            width=510.0,
            height=38.0
        )

        self.entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = canvas.create_image(
            3700.0,
            80.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            canvas,
            bd=0,
            bg="#472D0E",
            font='Neucha',
            fg="#ffffff",
            highlightthickness=0
        )
        self.entry_3.place(
            x=303.0,
            y=74.0,
            width=134.0,
            height=32.0
        )

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.find_optimal_recipes_by_cost,
            relief="flat",
        )
        self.button_2.place(
            x=250,
            y=70.0,
            width=39.0,
            height=38.0
        )


        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.combined_button_action,
            relief="flat"
        )
        self.button_3.place(
            x=450.0,
            y=70.0,
            width=39.0,
            height=38.0
        )
