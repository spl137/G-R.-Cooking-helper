from tkinter import Frame, Canvas, Button, PhotoImage, Entry
from pathlib import Path

def relative_to_assets(path: str) -> Path:
    return Path("assets/title") / Path(path)

class Title(Frame):
    def __init__(self, master, show_risen, show_g1, show_g2, show_g3, show_search, show_randoms, find_optimal_recipes_by_cost):
        super().__init__(master)
        self.show_risen = show_risen
        self.show_g1 = show_g1
        self.show_g2 = show_g2
        self.show_g3 = show_g3
        self.show_search = show_search
        self.show_randoms = show_randoms
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
            364.0,
            139.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        self.image_3 = canvas.create_image(
            315.0,
            95.0,
            image=self.image_image_3
        )

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_g1,
            relief="flat"
        )
        self.button_1.place(
            x=18.0,
            y=264.0,
            width=156.0,
            height=204.0
        )

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_g2,
            relief="flat"
        )
        self.button_2.place(
            x=193.0,
            y=264.0,
            width=157.0,
            height=204.0
        )

        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_g3,
            relief="flat"
        )
        self.button_3.place(
            x=365.0,
            y=264.0,
            width=159.0,
            height=204.0
        )

        self.button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            canvas,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_risen,
            relief="flat"
        )
        self.button_4.place(
            x=538.0,
            y=264.0,
            width=159.0,
            height=204.0
        )

        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        self.image_4 = canvas.create_image(
            356.0,
            70.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        self.image_5 = canvas.create_image(
            360.0,
            170.0,
            image=self.image_image_5
        )



        self.button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_search,
            relief="flat"
        )
        self.button_5.place(
            x=23.0,
            y=60.0,
            width=38.0,
            height=31.0
        )

        self.button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
        self.button_7 = Button(
            canvas,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_randoms,
            relief="flat"
        )
        self.button_7.place(
            x=22.0,
            y=17.0,
            width=39.0,
            height=38.0
        )