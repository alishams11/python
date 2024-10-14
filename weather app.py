from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim  
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather APP")
root.geometry(f"{900}x{500}+300+200")
root.resizable(False, False)

def getweather():
    city = textfield.get()
    
    # Geolocation
    geolocator = Nominatim(user_agent=("geoapiExercises"))
    location = geolocator.geocode(city)
    
    if location is None:
        messagebox.showerror("Error", "Location not found!")
        return

    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")  
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    # Weather API Call
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid="
    
    try:
        json_data = requests.get(api).json()
        condition = json_data["weather"][0]["main"]
        description = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"] - 273.15)  # Kelvin to Celsius
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]

        # Update weather details in labels
        t.config(text=f"{temp}°C")
        c.config(text=f"{condition} | FEELS LIKE {temp}°C")
        w.config(text=f"{wind} m/s")
        h.config(text=f"{humidity}%")
        d.config(text=description)
        p.config(text=f"{pressure} hPa")
        
    except Exception as e:
        messagebox.showerror("Error", "Could not retrieve weather data. Please try again.")

# Search box
Search_image = PhotoImage(file="/home/ali11/Downloads/search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), 
                     bg="#404040", border=0, fg="white")
textfield.place(x=60, y=35)
textfield.focus()

Search_icon = PhotoImage(file="/home/ali11/Downloads/search_icon.png")
search_button = Button(image=Search_icon, borderwidth=0, cursor="hand2", 
                       bg="#404040", command=getweather)
search_button.place(x=400, y=32)

# Logo
Logo_image = PhotoImage(file="/home/ali11/Downloads/ logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# Bottom box 
Frame_image = PhotoImage(file="/home/ali11/Downloads/box.png")
Frame_myimage = Label(image=Frame_image)
Frame_myimage.place(relx=0.5, rely=1, anchor='s')

# Time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Labels
label1 = Label(root, text="WIND", font=("Helvetica", 10, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=420)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 10, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=420)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 10, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=420)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=420)

# Weather data display
t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)
w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=100, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=225, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=405, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=620, y=430)





root.mainloop()