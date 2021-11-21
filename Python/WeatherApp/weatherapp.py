from pyowm import OWM
from tkinter import*
from tkinter import messagebox
from pyowm.utils.config import get_default_config
from tkinter import ttk
 
root = Tk()
root.title("Weather")
root.geometry("400x450")
owm = OWM('your API-key')
 
config_dict = get_default_config()
config_dict['language'] = 'ru'
the_dict = {}
va = IntVar() 
 
Label(root, text="Погода", font="Calibri 15 bold").pack(pady=5)
Label(root, text="Введите название города:", font="Consolas 11 bold").pack(pady=5)
a = Entry(root, width=20)
a.place(x=85,y=75)
 
Label(root, text="Температура:", font="Consolas 11 bold").place(x=85,y=95)
temper = Label(root, text="", bg="white")
temper.place(x=105,y=145)
 
Label(root, text="Давление:", font="Consolas 11 bold").place(x=225,y=95)
pre = Label(root, text="", bg="white")
pre.place(x=230,y=125)
 
Label(root, text="Влажность:", font="Consolas 11 bold").place(x=230,y=170)
hu = Label(root, text="", bg="white")
hu.place(x=255,y=195)
 
Label(root, text="Облачность:", font="Consolas 11 bold").place(x=90,y=170)
clo = Label(root, text="", bg="white")
clo.place(x=115,y=195)
 
Label(root, text="Скорость ветра:", font="Consolas 11 bold").place(x=75,y=240)
wind = Label(root, text="", bg="white")
wind.place(x=115,y=270)
 
Label(root, text="Видимость:", font="Consolas 11 bold").place(x=230,y=240)
vds = Label(root, text="", bg="white")
vds.place(x=250,y=270)
 
Label(root, text="Статус:", font="Consolas 11 bold").place(x=105,y=310)
sta = Label(root, text="", bg="white")
sta.place(x=115,y=340)
 
Label(root, text="Погода:", font="Consolas 11 bold").place(x=240,y=310)
dts = Label(root, text="", bg="white")
dts.place(x=220,y=340)
 
Label(root, text="Код погоды:", font="Consolas 11 bold").place(x=230,y=370)
wec = Label(root, text="", bg="white")
wec.place(x=260,y=410)
 
Label(root, text="Справочное время:", font="Consolas 11 bold").place(x=105,y=370)
tim = Label(root, text="", bg="white")
tim.place(x=115,y=410)
 
def show_temperature():
    try:
        l = va.get()
        place = a.get()
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather
        #температура 
        if l == 1:
            temp = w.temperature('celsius')['temp']
            temper["text"] = (temp,"°C")
        elif l == 2:
            temp = w.temperature('celsius')['temp']
            far = temp * 9/5+32
            temper["text"] = (far,"°F")
        #скорость ветра
        wih = w.wind()['speed']
        wind["text"] = (wih,"м/с")
        #влажность
        humi = w.humidity
        hu["text"] = (humi,"%")
        #облачность
        cl = w.clouds
        clo["text"] = (cl,"%")
        #статус
        st = w.status
        sta["text"] = st
        #погода
        dt = w.detailed_status
        dts["text"] = dt
        #время
        ti = w.reference_time('iso')
        tim['text'] = ti
        #давление
        pr = w.pressure['press']
        pre['text'] = (pr,"м.рт.ст")
        #видимость
        vd = w.visibility_distance
        vds['text'] = (vd,"м")
        #код погоды
        wc = w.weather_code
        wec['text'] = wc
    
    except:
        messagebox.showwarning("Weather", "Что-то пошло не так.Возможно вы некорректно ввели название города!Попробуйте ещё раз!")
 
ttk.Button(root, text="Узнать погоду", command=show_temperature).place(x=225,y=72)
Radiobutton(root,variable=va,value=1,text="°C").place(x=95,y=115)
Radiobutton(root,variable=va,value=2,text="°F").place(x=135,y=115)
 
root.mainloop()
