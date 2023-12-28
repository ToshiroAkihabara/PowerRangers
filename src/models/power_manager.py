import subprocess
from platform import system


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
        super().__init__(
            shutdown = ["shutdown", "now"], 
            reboot = ["shutdown", "-r", "now"], 
            logout = ["gnome-session-quit", "--no-prompt"]
        )
  
class PowerManagerWindows(PowerManager):
    def __init__(self) -> None:
        super().__init__(
            shutdown = ["shutdown", "/s", "/t", "0"],
            reboot = ["shutdown", "/r", "/t", "0"],
            logout = ["shutdown", "/l"]
        )
            
class SystemPlatform:
    def __init__(self) -> None:
        self.os = system()

    def select_system_platform(
        self,
    ) -> PowerManagerWindows | PowerManagerLinux | None:
        if self.os == "Windows":
            return PowerManagerWindows()
        elif self.os == "Linux":
            return PowerManagerLinux()
