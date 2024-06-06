from tkinter import Frame, Canvas, Button, PhotoImage, Entry
from pathlib import Path

def relative_to_assets(path: str) -> Path:
    return Path(r"assets\g3") / Path(path)

class G3(Frame):
    def __init__(self, master, switch_function):
        super().__init__(master)
        self.switch_function = switch_function
        self.create_widgets()

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
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            360.0,
            245.0,
            image=image_image_1
        )
        image_image_1.image = image_image_1
        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            308.0,
            70.0,
            image=image_image_2
        )
        image_image_2.image = image_image_2
        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            367.0,
            294.0,
            image=image_image_3
        )
        image_image_3.image = image_image_3
        image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(
            364.0,
            300.0,
            image=image_image_4
        )
        image_image_4.image = image_image_4
        image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(
            127.0,
            65.0,
            image=image_image_5
        )
        image_image_5.image = image_image_5
        image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = canvas.create_image(
            41.0,
            36.0,
            image=image_image_6
        )
        image_image_6.image = image_image_6
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
