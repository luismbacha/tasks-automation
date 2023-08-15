from win11toast import toast, notify, update_progress
from time import sleep

class Notifier:
    def __init__(self) -> None:
        self.toast_keys = ("title", "message", "input", "button", "dialogue")
        self.notify_keys = ("title", "total")

    def _toast(self, toast_values) -> int:
        if not all(k in toast_values for k in self.toast_keys):
            raise ValueError("Not all require keys were sent")
        try:
            user_input = toast(
                toast_values["title"],
                toast_values["message"],
                input=toast_values["input"],
                button=toast_values["button"],
                dialogue=toast_values["dialogue"]
            )
            return int(user_input.get("user_input").get(toast_values["input"]))
        except Exception as e:
            print("There was an error with the toast")
            raise e
    
    def _notify(self, notify_values) -> int:
        if not all(k in notify_values for k in self.notify_keys):
            raise ValueError("Not all require keys were sent")
        try:
            notify(progress={
                "title": notify_values["title"],
                "status": "In progress",
                "value": "0",
                "valueStringOverride": "0/" + notify_values["total"] + " minutes"
            })
            total = int(notify_values["total"])
            for i in range (1, total + 1):
                sleep(55)
                update_progress({'value': i/total, 'valueStringOverride': f'{i}/{total} minutes'})
            update_progress({'status': "Completed"})
            sleep(7)
            return total
        except Exception as e:
            print("There was an error with the notification")
            raise e
    
    def notify(self, values):
        if not isinstance(values, dict):
            raise TypeError("Parameter should be a dict")
        if len(values) == 0:
            raise ValueError("Parameter should not be empty")
        if(len(values) == 5):
            return self._toast(values)
        elif(len(values) == 2):
            return self._notify(values)
        else:
            raise ValueError("Wrong number of arguments sent")