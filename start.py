from win11toast import toast
from scheduler import Scheduler
import threading
import time
import signal
import sys

def get_time(block_type) -> int:
    user_input = toast(block_type, "Specify time, 0 to exit", input="time", button="OK", duration='long', dialogue='Hola mundo')
    if(len(user_input) == 1):
        return 0
    return(int(user_input.get("user_input").get("time")))

def main() -> None:
    start_with_break = False
    if(len(sys.argv) == 2):
        start_with_break = bool(sys.argv[1])
    scheduler = Scheduler(start_with_break)
    scheduler.timer_loop()
    def signal_handler(signum, frame):
        print("Received signal")
        exit()
    #signal.signal(signal.SIGINT, signal_handler)
    
main()
