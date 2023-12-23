import customtkinter
from views.Window import Window


class View(customtkinter.CTk):
    def __init__(self, controller) -> None:
        self.mode = customtkinter.set_appearance_mode("dark")
        self.color_theme = customtkinter.set_default_color_theme("dark-blue")
        super().__init__()
        self.controller = controller
        self.title("PowerRangers")
        self.geometry("300x300")
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.window = Window(master=self, command=self.controller.on_button_click)
        
    def get_select(self):
        return self.window.get()
    
    def main(self):
        self.mainloop()