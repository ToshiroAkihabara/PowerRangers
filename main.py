import customtkinter  # type: ignore

from frame import ImageFrame, RunButtonFrame, SelectWidgetFrame
from shutdown import PowerManageDefiner


class Window:
    def __init__(self, master, command) -> None:
        self.image_frame = ImageFrame(master=master)
        self.image_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsw")
        self.image_frame.configure(fg_color="transparent")
        self.widget_frame = SelectWidgetFrame(
            master=master,
            title="Choose your Power Ranger",
            values=["Power Off", "Power Reboot", "Power Logout"],
        )
        self.widget_frame.grid(row=1, column=0, padx=0, pady=(0, 0), sticky="nsw")
        self.widget_frame.configure(fg_color="transparent")
        self.button_frame = RunButtonFrame(master=master, title="Go", command=command)
        self.button_frame.grid(row=2, column=0, padx=0, pady=(0, 0), sticky="nsw")
        self.button_frame.configure(fg_color="transparent")

    def get(self):
        return self.widget_frame.get()


class App(customtkinter.CTk):
    def __init__(self) -> None:
        self.mode = customtkinter.set_appearance_mode("dark")
        self.color_theme = customtkinter.set_default_color_theme("dark-blue")
        super().__init__()
        self.title("PowerRangers")
        self.geometry("300x300")
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.window = Window(master=self, command=self.go_button)

    def go_button(self):
        definer = PowerManageDefiner()
        manager = definer.get_manager_os()
        result = self.window.get()
        if result == "Power Off":
            manager.power_off()
        elif result == "Power Reboot":
            manager.restart()
        else:
            manager.log_out()


if __name__ == "__main__":
    app = App()
    app.mainloop()
