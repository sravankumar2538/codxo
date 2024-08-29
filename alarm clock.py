import time
from datetime import datetime
import winsound  

def set_alarm(alarm_time):
    print(f"Setting alarm for {alarm_time}...")

    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}", end="\r")  

        # Check if the current time matches the alarm time
        if current_time == alarm_time:
            print("\nAlarm! Time to wake up!")
            winsound.Beep(1000, 1000)  # Beep for 1 second
            break

        # Sleep for 1 second to avoid high CPU usage
        time.sleep(1)

def main():
    # Get the alarm time from the user
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")

    try:
        # Validate the alarm time format
        datetime.strptime(alarm_time, "%H:%M:%S")
        set_alarm(alarm_time)
    except ValueError:
        print("Invalid time format! Please enter the time in HH:MM:SS format.")

if __name__ == "__main__":
    main()
