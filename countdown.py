import time
from datetime import datetime

def countdown_timer(seconds):
    print(f"\n⏳ Countdown started for {seconds} seconds.")
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"⏱️ {mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("\n⏰ Time's up!")

def alarm_clock(alarm_time):
    print(f"\n🔔 Alarm set for {alarm_time}")
    while True:
        now = datetime.now().strftime("%H:%M")
        if now == alarm_time:
            print("\n🚨 Wake up! It's", alarm_time)
            break
        time.sleep(10)

def stopwatch():
    input("\n▶️ Press Enter to start the stopwatch...")
    start_time = time.time()
    input("⏹️ Press Enter to stop the stopwatch...")
    elapsed = time.time() - start_time
    mins, secs = divmod(int(elapsed), 60)
    print(f"⏱️ Elapsed Time: {mins:02d}:{secs:02d}")

def main():
    while True:
        print("\n=== Multi-Tool Clock ===")
        print("1. Countdown Timer")
        print("2. Alarm Clock")
        print("3. Stopwatch")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                seconds = int(input("Enter time in seconds: "))
                countdown_timer(seconds)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "2":
            alarm_time = input("Set alarm time (HH:MM, 24-hour format): ")
            alarm_clock(alarm_time)
        elif choice == "3":
            stopwatch()
        elif choice == "4":
            print("👋 Exiting. Have a great day!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

