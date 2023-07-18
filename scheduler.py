from orchestrator import Orchestrator
from win11toast import toast
import time

class Scheduler:
    def __init__(self, start_with_break=False) -> None:
        self.is_break = start_with_break
        self.block_type = { False: "Pomodoro", True:"Break" }

    def notify(self) -> int:
        timer = -1
        try:
            dialogue = "Se termino el " + self.block_type[not self.is_break]
            user_input = toast(
                self.block_type[self.is_break],
                "Specify time, 0 to exit",
                input="time",
                button="OK",
                duration='long',
                dialogue=dialogue)
            timer = int(user_input.get("user_input").get("time"))
        except Exception as e:
            print("Error getting time")
            print("Error", str(e))
            return -1
        self.is_break = not self.is_break
        return timer
        
    def timer_loop(self) -> None:
        timer = 1
        while timer != 0:
            timer = self.notify()
            if(timer < 0):
                timer = 1
            time.sleep(timer * 60)