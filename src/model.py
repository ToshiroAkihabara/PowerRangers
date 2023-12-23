from typing import Optional

from models.PowerManager import SystemPlatform
from views.Window import PowerLogout, PowerOff, PowerReboot


class Model:
    def __init__(self) -> None:
        self.system = SystemPlatform()
        self.platform = self.system.get_platform()

    def button_action(
        self, select: Optional[PowerOff | PowerLogout | PowerReboot]
    ) -> None:
        if select == "Power Off":
            self.platform.power_off()
        elif select == "Power Reboot":
            self.platform.restart()
        else:
            self.platform.log_out()
