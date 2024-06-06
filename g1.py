from tkinter import Frame, Canvas, Button, PhotoImage
from pathlib import Path

def relative_to_assets(path: str) -> Path:
    return Path("assets/g1") / Path(path)

class G1(Frame):
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

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_1 = canvas.create_image(
            360.0,
            245.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.image_2 = canvas.create_image(
            308.0,
            70.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        self.image_3 = canvas.create_image(
            127.0,
            65.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        self.image_4 = canvas.create_image(
            367.0,
            294.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        self.image_5 = canvas.create_image(
            364.0,
            297.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        self.image_6 = canvas.create_image(
            41.0,
            36.0,
            image=self.image_image_6
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
