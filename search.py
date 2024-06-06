from tkinter import Frame, Canvas, Button, PhotoImage, Entry, Text
from pathlib import Path
import json
def relative_to_assets(path: str) -> Path:
    return Path(r"assets\search") / Path(path)

class Search(Frame):
    def __init__(self, master, switch_function, search_func):
        super().__init__(master)
        self.switch_function = switch_function
        self.search_func = search_func
        self.create_widgets()

    def search_recipes_by_name(self, event=None):
        keywords = self.entry_1.get("1.0", "end-1c").split()
        matching_recipes = self.search_func(keywords)
        if matching_recipes:
            result = "\n".join([f"{recipe['name']} (Восстановление здоровья: {recipe['health_recovery']}, Стоимость: {recipe['cost']}): {', '.join(recipe['ingredients'])}"for recipe in matching_recipes])
            self.entry_2.delete("1.0", 'end')
            self.entry_2.insert("1.0", result)
        else:
            self.entry_2.delete("1.0", 'end')
            self.entry_2.insert("1.0", "Рецепты не найдены.")
            return 'break'
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

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = canvas.create_image(
            360.0,
            245.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = canvas.create_image(
            371.0,
            39.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = canvas.create_image(
            367.0,
            294.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = canvas.create_image(
            41.0,
            36.0,
            image=self.image_image_4
        )


        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_function,
            relief="flat"
        )
        button_1.place(
            x=22.0,
            y=17.0,
            width=39.0,
            height=38.0
        )
        button_1.image = button_image_1

        self.entry_1 = Text(
            canvas,
            bd=0,
            bg="#472D0E",
            font='Neucha',
            fg="#ffffff",
            highlightthickness=0
        )
        self.entry_1.place(x=210.0, y=78.0, width=275.0, height=29.0)
        self.entry_1.bind('<Return>', lambda e:('break', self.search_recipes_by_name())[0])
        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(
            canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.search_recipes_by_name,
            relief="flat"
        )
        button_2.place(x=490.0, y=77.0, width=38.0, height=31.0)
        button_2.image = button_image_2

        self.entry_2 = Text(
            canvas,
            bd=0,
            bg="#472D0E",
            font='Neucha',
            fg="#ffffff",
            highlightthickness=0
        )
        self.entry_2.place(x=90.0, y=150.0, width=550.0, height=290.0)

