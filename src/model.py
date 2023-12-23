from models.PowerManager import SystemPlatform


class Model:
    def __init__(self) -> None:
        self.system = SystemPlatform()
        self.platform = self.system.get_platform()

    def button_action(self, select: str) -> None:
        if select == "Power Off":
            self.platform.power_off()
        elif select == "Power Reboot":
            self.platform.restart()
        else:
            self.platform.log_out()