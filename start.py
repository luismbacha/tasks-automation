from scheduler import timer_loop
from signal import signal, SIGINT
from win32gui import EnumWindows, IsWindowVisible, GetWindowText, PostMessage
from win32con import WM_CLOSE
from orchestrator import Orchestrator

import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--is-break", action="store_true", help="Flag to determine if it starts with a break block")
    args = parser.parse_args()
    Orchestrator.Initialize(args.is_break)
    def signal_handler(signum, frame):
        print("Received signal")
        for hwnd in EnumWindows():
            if IsWindowVisible and GetWindowText.startswith("Toast Notification"):
                PostMessage(hwnd, WM_CLOSE, 0, 0)
        timer_loop()
    signal(SIGINT, signal_handler)
    timer_loop()
    
main()
