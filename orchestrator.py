from trello_connection import get_trello_client

BREAK = "Break"
TOMATO = "Tomato"

class Orchestrator:
    
    def __init__(self, start_with_break) -> None:
        if(start_with_break):
            self.current_block = BREAK
        else:
            self.current_block = TOMATO
        # self.trello_client = get_trello_client()
        # Get boards and lists
        pass

    def orchestrate(self) -> dict:
        # Define if it's break, tomato or eod
        # Return values for notification
        pass

    def start_break(self) -> None:
        # suggest break, move break list or create cards
        pass

    def finish_break(self) -> None:
        # Remove breaks cards
        pass

    def start_tomato(self) -> None:
        # Move task to work on and multitasking task
        # Move "expired" cards to Doing
        # Ensure cards are correctly ordered
        # Show notification with tasks to work on
        pass

    def finish_tomato(self) -> None:
        # Move tasks from Doing to Today, Multitasking or Tasks
        pass

    def execute_eod(self) -> None:
        # Show next familiar reminder
        # Arrange cards in Pending and Scheduled boards
        pass