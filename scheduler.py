from notifier import Notifier
from time import sleep

def timer_loop(is_break) -> None:
    block_type = { False: "Pomodoro", True:"Break" }
    toast_values = {"title": "", "message":"Specify time, 0 to exit", "input": "time",
                    "button": "OK", "dialogue": ""}
    notify_values = {"title": "Block", "total": ""}
    while True:
        try:
            toast_values["title"] = block_type[is_break]
            toast_values["dialogue"] = "Se termino el " + block_type[not is_break]
            timer = Notifier().toast(toast_values)
            if(timer == 0):
                return
            is_break = not is_break
            notify_values["total"] = str(timer)
            Notifier().notify(notify_values)
        except Exception as e:
            print("There was an error with timer loop")
            print(str(e))
            sleep(5)
