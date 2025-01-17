# timer.py
import datetime
from datetime import timedelta
import os
import time
from Menu import Menu

# Stopwatch function
def stopwatch():
    start_time = get_time()
    input("Press enter to stop")
    end_time = get_time()
    print(f"Time elapsed: {end_time - start_time}")

# Focus timer function
def get_custom_duration():
    while True:
        try:
            return int(input("Enter custom duration: "))
        except ValueError:
            print("Please enter an integer")

# Focus timer function
def focus(duration):
    os.system("cls" if os.name == "nt" else "clear")
    now = datetime.datetime.now()
    end_time = now + datetime.timedelta(minutes=duration)

    # Display countdown timer
    print("\n"*3)
    while now < end_time:
        remaining = format_timedelta(end_time-now)
        print(f"    Time remaining: {remaining}", end="\r")
        now = datetime.datetime.now()
        time.sleep(1)

# Show the focus menu
def focus_menu():
    focus_menu = Menu("Focus Timer", [("25 minutes", 25), ("45 minutes", 45), ("Custom", get_custom_duration), ("Exit", exit)], func=focus)
    focus_menu.show()

# Format timedelta
def format_timedelta(td):
    # Format a timedelta as H:M:S without leading zero for hours
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # Remove leading zeros
    if hours == 0:
        return f"{minutes}:{seconds:02}"
    return f"{hours}:{minutes:02}:{seconds:02}"

# Get time
def get_time_str(time=None):
    if time:
        return time.strftime("%H:%M:%S")
    return datetime.datetime.now().strftime("%H:%M:%S")

# Main menu
main_menu = Menu("Main menu", [("Stopwatch", stopwatch), ("Focus Timer", focus_menu), ("Exit", exit)])
main_menu.show()
