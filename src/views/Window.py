from dataclasses import dataclass
from typing import Optional

from views.Frame import ImageFrame, RunButtonFrame, SelectWidgetFrame


@dataclass
class PowerOff:
    power_off: str


@dataclass
class PowerReboot:
    power_reboot: str


@dataclass
class PowerLogout:
    power_logout: str


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

    def get(self) -> Optional[PowerOff | PowerLogout | PowerReboot]:
        return self.widget_frame.get()
