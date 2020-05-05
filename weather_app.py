from tkinter import *
import requests

# Background for GUI display


def bg(temperature):
    temp = int(temperature)
    if(temp > 40):
        root.configure(background='#fc2e0a')
        label.configure(background='#fc2e0a')
        entry.configure(background='#fc2e0a')
        get_btn.configure(background='#fc2e0a')
        output.configure(background='#fc2e0a')
    elif(temp > 30):
        root.configure(background='#ff4000')
        label.configure(background='#ff4000')
        entry.configure(background='#ff4000')
        get_btn.configure(background='#ff4000')
        output.configure(background='#ff4000')
    elif(temp > 20):
        root.configure(background='#ff8400')
        label.configure(background='#ff8400')
        entry.configure(background='#ff8400')
        get_btn.configure(background='#ff8400')
        output.configure(background='#ff8400')
    elif(temp > 10):
        root.configure(background='#ffbf00')
        label.configure(background='#ffbf00')
        entry.configure(background='#ffbf00')
        get_btn.configure(background='#ffbf00')
        output.configure(background='#ffbf00')
    elif(temp > 0):
        root.configure(background='light blue')
        label.configure(background='light blue')
        entry.configure(background='light blue')
        get_btn.configure(background='light blue')
        output.configure(background='light blue')
    elif(temp > -10):
        root.configure(background='#00a6ff')
        label.configure(background='#00a6ff')
        entry.configure(background='#00a6ff')
        get_btn.configure(background='#00a6ff')
        output.configure(background='#00a6ff')
    elif(temp < -10):
        root.configure(background='#003cff')
        label.configure(background='#003cff')
        entry.configure(background='#003cff')
        get_btn.configure(background='#003cff')
        output.configure(background='#003cff')

# Weather information from API


def weather(city):
    key = ''  # OpenWeatherMap API key
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    # Can be customized to information user wants
    par = {'APPID': key, 'q': city, 'units': 'metric'}
    resp = requests.get(URL, params=par)
    data = resp.json()

    location = data['name']
    temperature = data['main']['temp']
    desc = data['weather'][0]['description']

    output['text'] = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (
        location, desc, temperature)
    bg(temperature)


root = Tk()
root.geometry("300x300")
root.title('Weather')

label = Label(root, text='Enter City')
label.pack()
entry = Entry(root)
entry.pack()

get_btn = Button(root, text="Get Weather",
                 command=lambda: weather(entry.get()))
get_btn.pack()

output = Label(root)
output.place(relwidth=1, relheight=1)
output.pack()
root.mainloop()
