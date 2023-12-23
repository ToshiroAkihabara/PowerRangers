import subprocess
from platform import system
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


class SystemPlatform:
    def __init__(self) -> None:
        self.os = system()
        self.platform = self.select_system_platform()

    def select_system_platform(
        self,
    ) -> Optional[PowerManagerWindows | PowerManagerLinux]:
        if self.os == "Windows":
            return PowerManagerWindows()
        else:
            return PowerManagerLinux()

    def get_platform(self):
        return self.platform
