from win11toast import toast
from scheduler import Scheduler

import sys
import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--is-break", action="store_true", help="Flag to determine if it starts with a break block")
    args = parser.parse_args()
    scheduler = Scheduler(args.is_break)
    scheduler.timer_loop()
    def signal_handler(signum, frame):
        print("Received signal")
        exit()
    # signal.signal(signal.SIGINT, signal_handler)
    
main()
