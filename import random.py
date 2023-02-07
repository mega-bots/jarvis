import random         

import tkinter          # pip install tkinter

from tkinter import *

import datetime    

import pyttsx3          # pip install pyttsx3

import os

import time

import subprocess

import webbrowser

from tkinter import _tkinter

from PIL import ImageTk,Image     # pip install PIL



engine = pyttsx3.init()

# in windows

# engine = pyttsx3.init('sapi5')

window = Tk()


window.configure(bg = "black")  

SET_WIDTH = 800

SET_HEIGHT = 700


global ques


ques = Entry(window,width=40,bg="black",fg="white",font = ('arial',18,'bold'))  

ques.pack(padx = 10,pady = 20)



def speak(audio):

    engine.say(audio)

    engine.runAndWait()


def wish():

    hour = int(datetime.datetime.now().hour)


    if hour == 0 and hour<=12:

        speak("Good morning MegaBot")


    elif hour>=12 and hour<=18:

        speak("Good afternoon MegaBot")


    else:

        speak("Good evening MegaBot")




def command():


    if 'open desktop' in ques.get():

       

        speak("ok MegaBot do it ")

        # d = "C:\Users\Public\Desktop"

        os.startfile(d)

        # or


        # os.system(d)

       

    elif 'open file' in ques.get():

       

        speak("which file MegaBot ")

        d = Toplevel()

        Toplevel.configure(bg="black")

        e = Entry(d,bg = "black", fg = "white" ,width = 20)

        e.pack()

        def open_file():

            os.system(e.get())

            speak("ok MegaBot i will open "+e.get())

        s = Button(d,bg = "black",font = ('arial',18,'bold'),fg  = "white",width = 10,activeforeground = "grey",activebackground = "black",text = "open it",command=open_file).pack()


    elif 'shutdown' in ques.get():

        os.system("shutdown now -h")

        speak("ok MegaBot i shutdown the computer")


    elif 'open stackoverflow' in ques.get():

        speak("ok MegaBot i will open the stck over flow website")

        webbrowser.open("https://wwww.stackoverflow.com")


    elif 'open website' in ques.get():

        speak("which website MegaBot ")

        d = Toplevel()

        e = Entry(d,bg = "black", fg = "white" ,font = ('arial',18,'bold'),width = 20)

        e.pack()

        def open_web():

            webbrowser.open("https://"+e.get()+".com")

            speak("ok MegaBot i will open "+e.get())

        s = Button(d,bg = "black",fg  = "white",width = 10,activeforeground = "grey",activebackground = "black",text = "open it",command=open_web).pack()


    elif 'open google' in ques.get():

        speak("ok MegaBot i will open google.com")

        webbrowser.open("https://wwww.google.com")


    elif 'open youtube' in ques.get():

        speak("ok MegaBot i will opwn youtube dot com")

        webbrowser.open("https://wwww.youtube.com")


    elif 'copy code' in ques.get():

        speak("of which file MegaBot ")

        d = Toplevel()

        e = Entry(d,bg = "black",font = ('arial',18,'bold'), fg = "white" ,width = 20)

        e.pack()

        def open_code():

            file = open(e.get(),"r+")

            re = file.read()

            speak(re)

        s = Button(d,bg = "black",fg  = "white",width = 10,activeforeground = "grey",activebackground = "black",text = "open it",command=open_code).pack()

       


    elif 'exit' in ques.get():

        exit()

        speak("good bye MegaBot have a good day")


    elif 'quite' in ques.get():

        speak("good bye MegaBot have a good day")

        exit()


    else :

        speak("sorry MegaBot i can not do this")


   


def you():

    speak("ok MegaBot open the youtube.com")

    webbrowser.open("https://www.youtube.com")



def win():

    speak("ok MegaBot i open it")

    webbrowser.open("https://techflayer.blogspot.com")

   


def main():

    # screen


    bgImg = Image.open("C:/Users/Mohit/Documents/DesktopAssistant/jarvis.png")

    window.title("J.A.R.V.I.S")

    canvas = tkinter.Canvas(window,width = SET_WIDTH,height = SET_HEIGHT)

  

   


    # image=ImageTk.PhotoImage(Image.open("back.png")

    image=ImageTk.PhotoImage(bgImg)

    canvas.create_image(0,0,anchor=NW,image=image)


    # entry



    btn = Button(text = "Open Techflayer" ,bg = "black" ,fg="white",width=20,activeforeground = "grey",activebackground = "black",command = win)

    btn.pack(padx = 0,pady= 0)


    btn = Button(text = " Open Youtube" ,bg = "black",fg = "white" ,width = 20,activeforeground  = "grey" ,activebackground = "black",command =you)

    btn.pack(side = TOP)


    btn = Button(bg = "black" ,fg = "white",width=20,activeforeground = "grey",activebackground = "black",text = "command",command=command).pack(side = BOTTOM,pady = 1 , padx = 3)

    canvas.configure(bg="black")


   

   

    shape = canvas.create_oval(10,10,60,60,fill = "blue")

    xspeed = random.randrange(1,8)

    yspeed = random.randrange(1, 8)


    shape2 = canvas.create_oval(10,10,60,60,fill = "blue")

    xspeed2 = random.randrange(1,9)

    yspeed2 = random.randrange(1,9)


    canvas.pack()

   

    while True:

        canvas.move(shape,xspeed,yspeed)

        pos = canvas.coords(shape)

        if pos[3]>= 700 or pos[1] <=0:

            yspeed = -yspeed

        if pos[2] >= 800 or pos[0] <=0:

            xspeed= -xspeed


        canvas.move(shape2,xspeed2,yspeed2)

        pos = canvas.coords(shape2)

        if pos[3]>= 700 or pos[1] <=0:

            yspeed2 = -yspeed2

        if pos[2] >= 800 or pos[0] <=0:

            xspeed2= -xspeed2                               

        window.update()

        time.sleep(0.01)

   

def ball():

    canvas = Canvas()



if __name__ == "__main__":

    wish()

    main()


window.mainloop()
