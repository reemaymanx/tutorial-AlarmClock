import tkinter as tk
import tkinter.ttk as t
from PIL import Image, ImageTk
import winsound as w
import datetime as dt
import threading
import time as time



# create color
background_colour = '#000000'
f1 = '#FFEBCD'
f2 = '#ffffff'

# window
window = tk.Tk()
window.title("")
window.geometry('350x150')
window.configure(bg=background_colour)

# frames
frame_line = tk.Frame(window, width=400, height=5, bg=f1)
frame_line.grid(row=0, column=0)
frame_body = tk.Frame(window, width=400, height=290, bg=f2)
frame_body.grid(row=1, column=0)

# frame body
img = Image.open('icon.png')  # Assuming the image file is in the same directory as the script
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)

icon_image = tk.Label(frame_body, height=100, image=img, bg=f2)
icon_image.place(x=10, y=10)

alarm_name = tk.Label(frame_body, text="Alarm Clock", height=1, font=('Ivy 18 bold'),bg=f2)
alarm_name.place(x=125, y=10)
##hour region
hour = tk.Label(frame_body, text="Hour", height= 1, font=('Ivy 10 bold'), bg=f2)
hour.place(x=150, y=40)
hour_counter = t.Combobox(frame_body, width=2, font=('arial 10'))
hour_counter['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12','13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24')
hour_counter.current(0)
hour_counter.place(x=150, y=58)

##minute region
minute = tk.Label(frame_body, text="Minute", height= 1, font=('Ivy 10 bold'), bg=f2)
minute.place(x=190, y=40)
min_counter = t.Combobox(frame_body, width=2, font=('arial 10'))
min_counter['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60')
min_counter.current(0)
min_counter.place(x=200, y=58)
##seconds region
second = tk.Label(frame_body, text="Second", height= 1, font=('Ivy 10 bold'), bg=f2)
second.place(x=240, y=40)
second_counter = t.Combobox(frame_body, width=2, font=('arial 10'))
second_counter['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60')
second_counter.current(0)
second_counter.place(x=250, y=58)


def activate_alarm():
    th = threading.Thread(target=alarm())
    th.start()



## activation radiobutton
selected = tk.IntVar()
rad1 = tk.Radiobutton(frame_body, font=('arial 10 bold'), value=1, text='Set Alarm', bg=f2, command=activate_alarm,variable=selected)
rad1.place(x=125, y=95)



def soundalarm():
    while True:
        w.Beep(1000, 1000)
      ##  w.PlaySound('Welcome.wav', w.SND_FILENAME)
    ##selected.set(0)

def alarm():
 while True:
  control = 1
  print(control)
  alarm_hour = hour_counter.get()
  alarm_minute = min_counter.get()
  alarm_second = second_counter.get()


  now = dt.datetime.now()
  hour = now.strftime("%I")
  minute = now.strftime("%M")
  second = now.strftime("%S")
  if control == 1:
    if alarm_hour == hour:
     if alarm_minute == minute:
      if alarm_second == second:
         print("Alarm is ON !!")
         soundalarm()
    time.sleep(1)



# start the main event loop
window.mainloop()
