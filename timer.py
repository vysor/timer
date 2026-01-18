#!/usr/bin/env python3
"""
Simple Terminal Timer with ASCII Art Display
A focus timer and stopwatch that runs in your terminal with beautiful ASCII art.
"""
import datetime
import os
import sys
import threading
import time

# ASCII art digits (0-9) for timer display
ASCII_DIGITS = {
    '0': [
        " ███ ",
        "█   █",
        "█   █",
        "█   █",
        " ███ "
    ],
    '1': [
        "  █  ",
        " ██  ",
        "  █  ",
        "  █  ",
        " ███ "
    ],
    '2': [
        " ███ ",
        "█   █",
        "   █ ",
        "  █  ",
        "█████"
    ],
    '3': [
        " ███ ",
        "█   █",
        "  ██ ",
        "█   █",
        " ███ "
    ],
    '4': [
        "█   █",
        "█   █",
        "█████",
        "    █",
        "    █"
    ],
    '5': [
        "█████",
        "█    ",
        "████ ",
        "    █",
        "████ "
    ],
    '6': [
        " ███ ",
        "█    ",
        "████ ",
        "█   █",
        " ███ "
    ],
    '7': [
        "█████",
        "    █",
        "   █ ",
        "  █  ",
        " █   "
    ],
    '8': [
        " ███ ",
        "█   █",
        " ███ ",
        "█   █",
        " ███ "
    ],
    '9': [
        " ███ ",
        "█   █",
        " ████",
        "    █",
        " ███ "
    ],
    ':': [
        "     ",
        "  █  ",
        "     ",
        "  █  ",
        "     "
    ]
}


def clear_screen():
    """Clear the terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")


def draw_ascii_time(time_str):
    """Draw time string using ASCII art digits"""
    lines = ["", "", "", "", ""]
    for char in time_str:
        if char in ASCII_DIGITS:
            digit_lines = ASCII_DIGITS[char]
            for i in range(5):
                lines[i] += digit_lines[i] + "  "
    return "\n".join(lines)


def draw_progress_bar(elapsed, total, width=50):
    """Draw a progress bar"""
    progress = min(elapsed / total, 1.0)
    filled = int(width * progress)
    bar = "█" * filled + "░" * (width - filled)
    percentage = int(progress * 100)
    return f"[{bar}] {percentage}%"


def format_time(seconds):
    """Format seconds as MM:SS or HH:MM:SS"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    
    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def stopwatch():
    """Run a stopwatch"""
    clear_screen()
    print("\n" + "="*60)
    print("STOPWATCH".center(60))
    print("="*60 + "\n")
    print("Press ENTER to stop the stopwatch...\n")
    
    start_time = time.time()
    # Start async input wait
    stop_event = threading.Event()
    
    def wait_for_input():
        input()
        stop_event.set()
    
    input_thread = threading.Thread(target=wait_for_input)
    input_thread.daemon = True
    input_thread.start()
    
    while not stop_event.is_set():
        elapsed = time.time() - start_time
        time_str = format_time(elapsed)
        
        # Display ASCII art time
        clear_screen()
        print("\n" + "="*60)
        print("STOPWATCH".center(60))
        print("="*60 + "\n")
        print("Press ENTER to stop the stopwatch...\n")
        print(draw_ascii_time(time_str))
        
        time.sleep(0.1)
    
    elapsed = time.time() - start_time
    time_str = format_time(elapsed)
    
    clear_screen()
    print("\n" + "="*60)
    print("STOPWATCH STOPPED".center(60))
    print("="*60 + "\n")
    print(draw_ascii_time(time_str))
    print(f"\nTotal time: {time_str}")
    print("\nPress ENTER to continue...")
    input()


def focus_timer(duration_minutes):
    """Run a focus timer for specified duration"""
    clear_screen()
    total_seconds = duration_minutes * 60
    end_time = time.time() + total_seconds
    
    while time.time() < end_time:
        remaining = end_time - time.time()
        if remaining < 0:
            remaining = 0
        
        time_str = format_time(remaining)
        elapsed = total_seconds - remaining
        
        # Clear and draw
        clear_screen()
        print("\n" + "="*60)
        print(f"FOCUS TIMER - {duration_minutes} MINUTES".center(60))
        print("="*60 + "\n")
        
        # Draw ASCII time
        print(draw_ascii_time(time_str))
        print()
        
        # Draw progress bar
        print(draw_progress_bar(elapsed, total_seconds, 50))
        print()
        
        # Time info
        elapsed_str = format_time(elapsed)
        print(f"Elapsed: {elapsed_str} | Remaining: {time_str}")
        
        time.sleep(1)
    
    # Timer complete
    clear_screen()
    print("\n" + "="*60)
    print("✓ TIMER COMPLETE! ✓".center(60))
    print("="*60 + "\n")
    print(draw_ascii_time("00:00"))
    print("\n🎉 Great job! Time to take a break! 🎉\n")
    print("Press ENTER to continue...")
    input()


def get_number_input(prompt, min_val=1, max_val=None):
    """Get integer input from user with validation"""
    while True:
        try:
            value = int(input(prompt))
            if value < min_val:
                print(f"Please enter a number >= {min_val}")
                continue
            if max_val and value > max_val:
                print(f"Please enter a number <= {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number")


def main_menu():
    """Display main menu and handle user selection"""
    while True:
        clear_screen()
        print("\n" + "="*60)
        print("TERMINAL TIMER".center(60))
        print("="*60 + "\n")
        print("1. Focus Timer (25 minutes)")
        print("2. Focus Timer (45 minutes)")
        print("3. Custom Focus Timer")
        print("4. Stopwatch")
        print("5. Exit")
        print()
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            focus_timer(25)
        elif choice == "2":
            focus_timer(45)
        elif choice == "3":
            duration = get_number_input("Enter duration in minutes: ", min_val=1, max_val=999)
            focus_timer(duration)
        elif choice == "4":
            stopwatch()
        elif choice == "5":
            clear_screen()
            print("\nGoodbye! Stay focused! 👋\n")
            sys.exit(0)
        else:
            print("\nInvalid option. Please try again.")
            time.sleep(1)


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        clear_screen()
        print("\n\nTimer interrupted. Goodbye! 👋\n")
        sys.exit(0)
