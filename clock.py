import tkinter as ui
import time
import math

window = ui.Tk()
window.geometry('200x200')

def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    # seconds line
    seconds_x = seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x
    seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(second_hand, center_x, center_y, seconds_x, seconds_y)

    # minutes line
    minutes_x =  minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
    minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

    # hours line
    hours_x = hours_hand_len * math.sin(math.radians(hours * 30)) + center_x
    hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

    window.after(1000, update_clock)

# canvas
canvas = ui.Canvas(window, width=200, height=200, bg="white")
canvas.pack(expand=True, fill="both")

# background
bg =ui.PhotoImage(file="C:\Users\Yash\Desktop\download.jpg")
canvas.create_image(100, 100, image=bg)

# clock hands
center_x = 100
center_y = 100
seconds_hand_len = 90
minutes_hand_len = 80
hours_hand_len = 75

# clock hands
# second hands
second_hand = canvas.create_line(100, 100, 100 + seconds_hand_len, 100 + seconds_hand_len, width=3, fill="red")
# minutes hands
minutes_hand = canvas.create_line(100, 100, 100 + minutes_hand_len, 100 + minute_hand_len, width=4, fill="#a594e2")
# hours hands
hours_hand = canvas.create_line(100, 100, 100 + hours_hand_len, 100 + hours_hand_len, width=5, fill="#a594e2")

update_clock()
window.mainloop()