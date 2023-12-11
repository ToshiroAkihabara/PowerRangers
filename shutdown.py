import os
import subprocess
from typing import Optional


class PowerManager:
    def __init__(self, shutdown, reboot, logout) -> None:
        self.shutdown = shutdown
        self.reboot = reboot
        self.logout = logout

    def power_off(self):
        subprocess.call(self.shutdown)

    def log_out(self):
        subprocess.call(self.logout)

    def restart(self):
        subprocess.call(self.reboot)


class PowerManagerLinux(PowerManager):
    def __init__(self) -> None:
        self.shutdown = ["shutdown", "now"]
        self.reboot = ["shutdown", "-r", "now"]
        self.logout = ["gnome-session-quit", "--no-prompt"]


class PowerManagerWindows(PowerManager):
    def __init__(self) -> None:
        self.shutdown = ["shutdown", "/s", "/t", "0"]
        self.reboot = ["shutdown", "/r", "/t", "0"]
        self.logout = ["shutdown", "/l"]


class PowerManageDefiner:
    def __init__(self) -> None:
        self.linux = PowerManagerLinux()
        self.windows = PowerManagerWindows()
        self.type = os.name

    def get_manager_os(self) -> Optional[PowerManagerLinux | PowerManagerWindows]:
        if self.type == "posix":
            return self.linux
        else:
            return self.windows
