import customtkinter # type: ignore

from src.views.window import Window
from src.controller import Controller

class View(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.mode = customtkinter.set_appearance_mode("dark")
        self.color_theme = customtkinter.set_default_color_theme("dark-blue")
        self.controller = Controller()
        self.title("PowerRangers")
        self.geometry("300x300")
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.window = Window(master=self, command=self.on_button_click)

    def on_button_click(self) -> None:
        select = self.window.get()
        self.controller.button_action(select)
        
    def main(self):
        self.mainloop()
