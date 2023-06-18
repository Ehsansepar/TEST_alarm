import datetime
import time
import winsound

print("Alarm Clock")
print("Please enter the time in 24-hour format (HH:MM:SS)")
alarm_time = input(">> ")

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        print("Wake up!")
        # Play sound
        winsound.Beep(2500, 2000)
        break
    time.sleep(1)