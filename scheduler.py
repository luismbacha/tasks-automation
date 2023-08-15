from time import sleep
from orchestrator import Orchestrator

def timer_loop() -> None:
    orchestrator = Orchestrator.Initialize()
    repeat = True
    while repeat:
        try:
            repeat = orchestrator.orchestrate()
        except Exception as e:
            print("There was an error with timer loop")
            print(str(e))
            sleep(5)
