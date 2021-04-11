from tkinter import *
import pygame
import time
t=0
t2=0

def set_timer():
    global t
    
    t=t+int(entry1.get())
    return t 

def set_timer2():
    global t2 
    t2=t2+int(entry2.get())
    return t2

def countdown():
    global t
    if t>0:
        label1.config(text=t)
        t=t-1
        label1.after(1000,countdown)
    elif t==0:
        label1.config(text="Fin de trabajo")
        pygame.mixer.init()
        #pygame.mixer.Sound.play(pygame.mixer.Sound('alarma1.ogg'))
        sound = pygame.mixer.Sound("alarma2.ogg")
        sound.play()
        time.sleep(2)
        label1.after(1000,countdown2)


def countdown2():
    global t2
    if t2>0:
        label1.config(text=t2)
        t2=t2-1
        label1.after(1000,countdown2)
    elif t2==0:
        print("end")
        label1.config(text="El descanso acabó")
        pygame.mixer.init()
        #pygame.mixer.Sound.play(pygame.mixer.Sound('alarma1.ogg'))
        sound = pygame.mixer.Sound("alarma1.ogg")
        sound.play()
        time.sleep(2) 





root =Tk()

root.geometry("540x150")

label1=Label(root,font="times 20")
label1.grid(row=1,column=2)

label2=Label(root,font="times 20",text="Trabajo")
label2.grid(row=3,column=1)

label3=Label(root,font="times 20",text="Descanso")
label3.grid(row=4,column=1)

times=StringVar()
entry1=Entry(root,textvariable=times)
entry1.grid(row=3,column=2)
times2=StringVar()
entry2=Entry(root,textvariable=times2)
entry2.grid(row=4,column=2)

boton1=Button(root,text="Trabajo",width=20,command=set_timer)
boton1.grid(row=6,column=1,padx=10)

boton3=Button(root,text="Descanso",width=20,command=set_timer2)
boton3.grid(row=6,column=2,padx=10)


boton2=Button(root,text="comenzar",width=20,command=countdown )
boton2.grid(row=6,column=3,padx=15)


root.mainloop()