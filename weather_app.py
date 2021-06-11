import requests
from tkinter import *
from PIL import Image
from tkinter import messagebox

#   CREATE THE FRAME FOR TKINTER
window = Tk()
window.title("Weather App Challenge")
window.geometry("550x500")


#   THIS FUNCTION WILL CLOSE THE PROGRAM ON CLICK OF THE exit_btn
def exit_program():
    message_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit', icon='warning')
    if message_box == 'yes':
        window.destroy()
    else:
        #   ELSE, JUST GO BACK TO THE APPLICATION SCREEN
        pass


def clear_entries():
    location_entry.config(text="")


def get_weather():
    try:
        location = location_entry.get()
        #   CREATE A GET REQUEST AND PASS IN THE url AS A PARAMETER
        response = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=676c63797b39396a5409f7456d909ee3&units=metric")
        print(response.json())

        # CALL THE display_weather FUNCTION TO SHOW THE USER THE WEATHER AND PASS IN THE response.json()
        display_weather(response.json())
        #   CATCH THE EXCEPTION IS THERE IS NO INTERNET CONNECTION
    except requests.ConnectionError:
        #   NOTIFY THE USER
        messagebox.showerror("Connection Error", message="Please check your network connection.")
    #     CATCH AN EXCEPTION FOR INPUTTING A WRONG LOCATION
    except KeyError as exception:
        messagebox.showerror("Location Error", message="The city is not found.")


def display_weather(weather_object):
    try:
        skies_label.config(text="weather is " + weather_object["weather"][0]["main"] + " today.")
        description_label.config(text="Today, we have " + weather_object["weather"][0]["description"] + " today.")
        temperature_label.config(text="The temperature is: " + str(weather_object["main"]["temp"]) + " degrees, but it feels like " + str(weather_object["main"]["feels_like"]) + " degrees.")
        wind_label.config(text="The wind speed is currently: " + str(weather_object["wind"]["speed"]) + "km/h")
    #   IF ONE OF THE weather_objects CONTENTS RETURN A NUMBER THAT ISN'T CONVERTED
    except ValueError:
        print("Value error")


location_label = Label(window, text="Please enter your location", fg="blue")
location_label.place(x=10, y=10)
location_entry = Entry(window)
location_entry.place(x=200, y=10)

skies_label = Label(window, fg="blue")
skies_label.place(x=10, y=50)

description_label = Label(window, fg="blue")
description_label.place(x=10, y=100)

temperature_label = Label(window, fg="blue")
temperature_label.place(x=10, y=150)

wind_label = Label(window, fg="blue")
wind_label.place(x=10, y=200)


get_weather_btn = Button(window, text="Get Weather", command=get_weather, fg="blue").place(x=10, y=300)
clear_btn = Button(window, text="Clear entries", command=clear_entries, fg="blue").place(x=200, y=300)
exit_btn = Button(window, text="Exit programme", command=exit_program, fg="blue").place(x=400, y=300)

window.mainloop()
