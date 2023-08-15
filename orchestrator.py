from trello_connection import get_trello_client
from notifier import Notifier
from time import sleep

class Orchestrator:
    _instance = None
        
    def __new__(cls, start_as_break=False):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @staticmethod
    def Initialize(start_as_break=False):
        return Orchestrator(start_as_break)
    

    def __init__(self, start_as_break) -> None:
        if not hasattr(self, "_is_break"):
            self._is_break = start_as_break
            self._is_starting = True
            self._block_type = { False: "Pomodoro", True:"Break" }
            self._toast_values = {"title": "", "message":"Specify time, 0 to exit", "input": "time",
                                "button": "OK", "dialogue": ""}
            self._notify_values = {"title": "Block", "total": ""}
            self._timer = -1
            # self.trello_client = get_trello_client()
            # Get boards and lists
    
    def _start_block(self) -> bool:
        self._toast_values["title"] = self._block_type[self._is_break]
        self._toast_values["dialogue"] = "Se termino el " + self._block_type[not self._is_break]
        try:
            self._timer = Notifier().notify(self._toast_values)
            if(self._timer == -1):
                print("Error loading time")
                return True
            if(self._timer == 0):
                return False
        except Exception as e:
            print("There was an error during " + self._block_type[self._is_break] + " start")
            return True
        self._is_starting = not self._is_starting
        return True
    
    def _finish_block(self) -> bool:
        self._is_starting = not self._is_starting
        self._notify_values["total"] = str(self._timer)
        self._timer = -1
        try:
            Notifier().notify(self._notify_values)
        except Exception as e:
            print("There was an error during " + self._block_type[self._is_break] + " finish")
            return True
        self._is_break = not self._is_break
        return True

    def orchestrate(self) -> bool:
        if(self._is_break and self._is_starting):
            return self._start_break()
        elif(self._is_break and not self._is_starting):
            return self._finish_break()
        elif(not self._is_break and self._is_starting):
            return self._start_tomato()
        elif(not self._is_break and not self._is_starting):
            return self._finish_tomato()
        # Define if it's break, tomato or eod
        # Return values for notification
        return None

    def _start_break(self) -> bool:
        return self._start_block()
        # suggest break, move break list or create cards

    def _start_tomato(self) -> bool:
        return self._start_block()
        # Move task to work on and multitasking task
        # Move "expired" cards to Doing
        # Ensure cards are correctly ordered
        # Show notification with tasks to work on

    def _finish_break(self) -> bool:
        return self._finish_block()
        # Remove breaks cards

    def _finish_tomato(self) -> bool:
        return self._finish_block()
        # Move tasks from Doing to Today, Multitasking or Tasks

    def _execute_eod(self) -> None:
        # Show next familiar reminder
        # Arrange cards in Pending and Scheduled boards
        pass
