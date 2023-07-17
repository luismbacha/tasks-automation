from trello_connection import get_trello_client

class Orchestrator:
    
    def __init__(self) -> None:
        self.trello_client = get_trello_client()
        # Get boards and lists
        pass

    def orchestrate(self) -> None:
        # Define if it's break, tomato or eod
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