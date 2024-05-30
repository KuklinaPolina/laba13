from tkinter import *
import requests
root = Tk()
def get_weather():
    city = cityField.get()
    key = '9ca558ddcb2b5431bdbc2b87293495b4'
    ss = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(ss, params=params)
    weather = result.json()
    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'
root['bg'] = '#fafafa'
root.title('Погода')
root.geometry('300x300')
root.resizable(width=False, height=False)
frame_top = Frame(root, bg='#483D8B', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)
frame_bottom = Frame(root, bg='#FFC125', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)
cityField = Entry(frame_top, bg='#DCDCDC', font=30)
cityField.pack()
btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
btn.pack()
info = Label(frame_bottom, text='Температура: ', bg='#F08080', font=40)
info.pack()
root.mainloop()