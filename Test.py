from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO


def load_cat():
    url_p = 'https://aws.random.cat/meow'
    r = requests.get(url_p)
    inf = r.json()
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
