from src.models.power_manager import SystemPlatform
from src.views.window import PowerLogout, PowerOff, PowerReboot


class Controller:
    def __init__(self) -> None:
        self.system = SystemPlatform()
        self.platform = self.system.select_system_platform()

    def button_action(
        self, select: PowerOff | PowerLogout | PowerReboot | None
    ) -> None:
        if select == "Power Off":
            self.platform.power_off()
        elif select == "Power Reboot":
            self.platform.restart()
        elif select == "Power Logout":
            self.platform.log_out()