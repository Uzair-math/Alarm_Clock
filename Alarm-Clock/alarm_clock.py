# Import required libraries
from tkinter import *
import datetime
import time
import winsound
from threading import *

# Create Tkinter Object
root = Tk()

# Set geometry
root.geometry("400x300")

# Global variable to control the alarm
alarm_active = False

# Function to handle threading
def Threading():
    global alarm_active
    alarm_active = True
    t1 = Thread(target=alarm)
    t1.start()

# Function to stop the alarm
def cancel_alarm():
    global alarm_active
    alarm_active = False
    status_label.config(text="Alarm Canceled", fg="red")

# Alarm function
def alarm():
    while alarm_active:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        # Display current time and set alarm time
        status_label.config(text=f"Current Time: {current_time}\nAlarm Time: {set_alarm_time}", fg="blue")
        
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            status_label.config(text="Time to Wake Up!", fg="green")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break
        
        # Wait for one second
        time.sleep(1)

# Add Labels, Frame, Button, OptionMenus
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

# Hour dropdown with label
hour_label = Label(frame, text="Hour", font=("Helvetica 10"))
hour_label.pack(side=LEFT)
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07', '08','09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22','23')
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

# Minute dropdown with label
minute_label = Label(frame, text="Minute", font=("Helvetica 10"))
minute_label.pack(side=LEFT)
minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
minute.set(minutes[0]) 
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

# Second dropdown with label
second_label = Label(frame, text="Second", font=("Helvetica 10"))
second_label.pack(side=LEFT)
second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
second.set(seconds[0])
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

# Label to show the alarm status and current time
status_label = Label(root, text="", font=("Helvetica 12"))
status_label.pack(pady=20)

# Set Alarm button
Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=5)

# Cancel Alarm button
Button(root, text="Cancel Alarm", font=("Helvetica 15"), command=cancel_alarm).pack(pady=5)

# Execute Tkinter mainloop
root.mainloop()
