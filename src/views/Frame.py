from typing import Any

import customtkinter  # type: ignore
from PIL import Image


class ImageFrame(customtkinter.CTkFrame):
    __IMAGE_PATH = r"src/image/main.png"

    def __init__(self, master) -> None:
        super().__init__(master)
        self.image = customtkinter.CTkImage(
            dark_image=Image.open(self.__IMAGE_PATH), size=(250, 150)
        )
        self.label = customtkinter.CTkLabel(master=self, image=self.image, text="")
        self.label.grid(row=1, column=0, padx=30, pady=(0, 0))


class SelectWidgetFrame(customtkinter.CTkFrame):
    def __init__(self, master, title: Any, values: list[str]) -> None:
        self.title = title
        self.values = values
        super().__init__(master)
        self.title = customtkinter.CTkLabel(
            self, text=self.title, fg_color="transparent"
        )
        self.title.grid(row=0, column=0, padx=70, pady=(0, 10), sticky="w")
        self.option = customtkinter.CTkComboBox(master=self, values=self.values)
        self.option.grid(row=2, column=0, padx=80, pady=(0, 10), sticky="w")

    def get(self):
        return self.option.get()


class RunButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master, title: str, command) -> None:
        self.title = title
        self.command = command
        super().__init__(master)
        self.button_img = Image.open(r"src/image/light.png")
        self.select = customtkinter.CTkButton(
            master=self,
            text=self.title,
            command=self.command,
            image=customtkinter.CTkImage(dark_image=self.button_img),
        )
        self.select.grid(row=3, column=0, padx=80, pady=(0, 30), sticky="w")
