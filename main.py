from shutdown import PowerManageDefiner
from frame import ImageFrame, SelectWidgetFrame, RunButtonFrame

import customtkinter


class App(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        #set style window 
        self.mode = customtkinter.set_appearance_mode("dark")
        self.color_theme = customtkinter.set_default_color_theme("dark-blue")
        #set default settings
        self.title("PowerRangers")
        self.geometry("300x300")
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        #add image frame
        self.image_frame = ImageFrame(master=self)
        self.image_frame.grid(row=0, column=0, padx=20, pady=15, sticky="nsw")
        self.image_frame.configure(fg_color="transparent")
        #add widget frame
        self.widget_frame = SelectWidgetFrame(
            master=self, title="Choose your Power Ranger", 
            values=["Power Off", "Power Reboot", "Power Logout"]
        )
        self.widget_frame.grid(row=1, column=0, padx=0, pady=(0, 0), sticky="nsw")
        self.widget_frame.configure(fg_color="transparent")
        #add button frame
        self.button_frame = RunButtonFrame(
            master=self,
            title="Go",
            command=self.go_button
        )
        self.button_frame.grid(row=3, column=0, padx=0, pady=(0, 0), sticky="nsw")
        self.button_frame.configure(fg_color="transparent")

    def go_button(self):
        definer = PowerManageDefiner()
        manager = definer.get_manager_os()
        result = self.widget_frame.get()
        if result == "Power Off":
            manager.power_off()
        elif result == "Power Reboot":
            manager.restart()
        else:
            manager.log_out()


if __name__ == "__main__":
    app = App()
    app.mainloop()
