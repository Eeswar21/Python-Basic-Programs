#weather-check.py
#install request library
#create account an open weather map site (openweathermap.org) and sign in
#once signed in click on API option and select API doc in current weather data -> click on the second link
#clikced link is for London city (JSON format)
#select the URL link and remove the samples word from it and copy the same

import requests
from tkinter import *

def weather():
    city=city_listbox.get() #extract option from the user selection
    url="https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22".format(city)
    #after create an account in open weather map, click on sign in and select API keys and this is my API : 8410d99cce487bfc3048ba3f3febe9f4
    res=requests.get(url)
    output=res.json()

    weather_status=output['weather'][0]['description']
    temprature=output['main']['temp']
    humidity=output['main']['humidity']
    wind_speed=output['wind']['speed']

    weather_status_label.configure(text="weather status : "+weather_status)
    temprature_label.configure(text="temprature : "+str(temprature))
    humidity_label.configure(text="humidity : "+str(humidity))
    wind_speed_label.configure(text="wind speed : "+str(wind_speed))

window=Tk()
window.geometry("400x350")

city_list=["chennai","madurai","trichy","tirunelveli","coimbatore","salem","thoothukudi","virudhunagar","dindigul","karur"]

city_listbox=StringVar(window)
city_listbox.set("select city")
option=OptionMenu(window,city_listbox,*city_list)
option.grid(row=0,column=2,padx=100,pady=10)

b1=Button(window,text="output",width=15,command=weather)
b1.grid(row=2,column=2,padx=150)

weather_status_label=Label(window,font=("times",10,"bold"))
weather_status_label.grid(row=10,column=2)

temprature_label=Label(window,font=("times",10,"bold"))
temprature_label.grid(row=12,column=2)

humidity_label=Label(window,font=("times",10,"bold"))
humidity_label.grid(row=14,column=2)

wind_speed_label=Label(window,font=("times",10,"bold"))
wind_speed_label.grid(row=16,column=2)

window.mainloop()
