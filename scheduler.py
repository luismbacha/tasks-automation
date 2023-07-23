from notifier import Notifier
from time import sleep

class Scheduler:
    def __init__(self, start_with_break=False) -> None:
        self.is_break = start_with_break
        self.block_type = { False: "Pomodoro", True:"Break" }
        self.toast_values = {"title": "", "message":"Specify time, 0 to exit", "input": "time",
                             "button": "OK", "dialogue": ""}
        self.notify_values = {"title": "Block", "total": ""}
        
    def timer_loop(self) -> None:
        while True:
            try:
                self.toast_values["title"] = self.block_type[self.is_break]
                self.toast_values["dialogue"] = "Se termino el " + self.block_type[not self.is_break]
                timer = Notifier().toast(self.toast_values)
                if(timer == 0):
                    return
                self.is_break = not self.is_break
                self.notify_values["total"] = str(timer)
                Notifier().notify(self.notify_values)
            except Exception as e:
                print("There was an error with timer loop")
                print(str(e))
                sleep(5)
