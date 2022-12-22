import requests
import json
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

while True:
    iss = input('Latest news by categories - 1, website request - 2, Get.Weather - 3, kittens!! - 4, exit = 0 \n')
    match iss:
        case '0':
            print('Bye, have a good time!')
            break
        case '1':
            url1 = 'https://newsapi.org/v2/top-headlines?'
            api_key1 = '2ffd480868c34ed3b6873a3f0ba539c8'
            ctgr = input('business, entertainment, general, health, science, sports or technology news?\n')
            # ctgr = sports
            kwrds = input('Keywords or a phrase to search for\n')
            # kwrds = Barcelona
            cntr = input('The 2-letter code of the country you want to get headlines for:\n')
            # cntr = uk
            prmtrs = {'q': kwrds, 'pageSize': "10", 'apiKey': api_key1, 'category': ctgr,
                      'country': cntr}
            hdlns = requests.get(url1, params=prmtrs).json()
            print(f'\nLast headlines about \'{kwrds}\'')
            for i in range(len(hdlns["articles"])):
                print(f'\nTitle: {hdlns["articles"][i]["title"]}')
                print(f'\n{hdlns["articles"][i]["description"]}')
                print(f'Source: {hdlns["articles"][i]["source"]["name"]}')
                print(f'Url: {hdlns["articles"][i]["url"]}\n')
        case '2':
            r = requests.get('https://ya.ru/')
            print('https://ya.ru/ request:')
            print(r.text)
        case '3':
            city_name = input('Enter the city\'s name and (additionally) 2-letter country code divided by comma(en):\n')
            api_key = '38805aea81773674cd372da84df55233'
            url = 'https://api.openweathermap.org/data/2.5/weather?'
            units = 'metric'
            wthr = requests.get(url, params={"units": units, "appid": api_key, "q": city_name}).json()
            w1 = f"It's {wthr['weather'][0]['description']} in {wthr['name']}."
            w2 = f"Temperature: {wthr['main']['temp']}. Feels like: {wthr['main']['feels_like']}"
            print(w1 + w2)
            print(f"Humidity level: {wthr['main']['humidity']}% ")
            print(f"Pressure: {wthr['main']['pressure']}hPa ")
        case '4':
            def load_cat():
                url_p = 'https://aws.random.cat/meow'
                rqw = requests.get(url_p)
                inf = rqw.json()
                img_url = inf['file']
                cat_img = requests.get(img_url)
                img = ImageTk.PhotoImage(Image.open(BytesIO(cat_img.content)).resize((900, 900), Image.LANCZOS))
                label.config(image=img)
                label.image = img


            window = Tk()
            window.title('A little doze of Happiness')
            window.geometry('1000x1000')
            Button(window, text="Cat", bg='pink', fg='black', command=load_cat).pack()
            label = Label(window)
            label.pack()

            window.mainloop()

        case _:
            print('Try different values')
