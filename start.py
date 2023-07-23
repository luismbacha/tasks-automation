from scheduler import timer_loop
from signal import signal, SIGINT
from win32gui import EnumWindows, IsWindowVisible, GetWindowText, PostMessage
from win32con import WM_CLOSE

import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--is-break", action="store_true", help="Flag to determine if it starts with a break block")
    args = parser.parse_args()
    def signal_handler(signum, frame):
        print("Received signal")
        for hwnd in EnumWindows():
            if IsWindowVisible and GetWindowText.startswith("Toast Notification"):
                PostMessage(hwnd, WM_CLOSE, 0, 0)
        timer_loop(args.is_break)
    signal(SIGINT, signal_handler)
    timer_loop(args.is_break)
    
main()
