from typing import Optional

import subprocess
import os


class PowerManager:
    def __init__(self, shutdown, reboot, logout, name) -> None:
        self.name = name
        self.shutdown = shutdown
        self.reboot = reboot
        self.logout = logout

    def power_off(self):
        # subprocess.call(self.shutdown)
        print(f"Выключаю {self.name}. Code: {self.shutdown}")

    def log_out(self):
        # subprocess.call(self.logout)
        print(f"Выхожу из {self.name}. Code: {self.logout}")

    def restart(self):
        # subprocess.call(self.reboot)
        print(f"Перезагружаю {self.name}, Code: {self.reboot}")

class PowerManagerLinux(PowerManager):
    def __init__(self, name=None) -> None:
        self.name = name
        self.shutdown = ["shutdown", "now"]
        self.reboot = ["shutdown", "-r", "now"]
        self.logout = ["gnome-session-quit", "--no-prompt"]

class PowerManagerWindows(PowerManager):
    def __init__(self, name=None) -> None:
        self.name = name
        self.shutdown = ["shutdown", "/s"]
        self.reboot = ["shutdown", "/r"]
        self.logout = ["shutdown", "/l"]

class PowerManageDefiner:
    def __init__(self) -> None:
        self.type = os.name
        self.name = self.get_name_os()
        self.linux = PowerManagerLinux(self.name)
        self.windows = PowerManagerWindows(self.name)
        
    def get_manager_os(self) -> Optional[PowerManagerLinux | PowerManagerWindows]:
        if self.type == "posix":
            return self.linux
        else:
            return self.windows
    
    def get_name_os(self):
        if self.type == "posix":
            return "Linux"
        else:
            return "Windows"