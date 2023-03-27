import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path


from playsound import playsound
import pygame
from pygame import mixer


PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096
song_counter = 0
listBox = None
infoLabel =""
def play():
    global song_selected
    song_selected = listBox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected!=""):
        infoLabel.configure(text="Now Playing " +song_selected)
    else:
        infoLabel.configure(text="Nothing Playing")

def stop():
    global song_selected
    song_selected = listBox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.stop()
    infoLabel.configure(text="Nothing Playing")

def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()

def resume():
    global song_selected 
    pygame   
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.stop()   


def musicWindow():
    global listBox
    global song_counter
    global infoLabel


    window = Tk()
    window.title("Music Window")
    window.geometry("330x420")
    window.configure(bg="LightSkyBlue")

    selectLabel = Label(window, text="Select Song", bg="LightSkyBlue" ,font=("Calibri",10))    
    selectLabel.place(x=5,y=3)

    listBox = Listbox(window,height=10,width=33,activestyle="dotbox",font=("Calibri",13),bd=1,bg="LightSkyBlue")
    listBox.place(x=10,y=24)
    
    for file in os.listdir('shared_files'):
        filename = os.fsdecode(file)
        listBox.insert(song_counter,filename)
        song_counter+=1

    scrollbar1= Scrollbar(listBox)
    scrollbar1.place(relheight=1,relx=1.5)
    scrollbar1.config(command=listBox.yview)

    PlayButton = Button(window,text="Play",bd=1,font=("Calibri",11),bg="SkyBlue", width=10,command=play)
    PlayButton.place(x=30,y=270)

    Stop = Button(window,text="Stop",bd=1,font=("Calibri",11),bg="SkyBlue", width=10,command=stop)
    Stop.place(x=200,y=270)

    Upload = Button(window,text="Upload",bd=1,font=("Calibri",11),bg="SkyBlue", width=10)
    Upload.place(x=30,y=320)

    Download = Button(window,text="Download",bd=1,font=("Calibri",11),bg="SkyBlue", width=10)
    Download.place(x=200,y=320)

    Resume = Button(window,text="Resume",bd=1,font=("Calibri",11),bg="SkyBlue", width=10, command=resume)
    Resume.place(x=30,y=370)

    Pause = Button(window,text="Pause",bd=1,font=("Calibri",11),bg="SkyBlue", width=10,command=pause)
    Pause.place(x=200,y=370)

    infoLabel = Label(window, bg="SkyBlue" ,font=("Calibri",11))    
    infoLabel.place(x=4,y=400)

    window.mainloop()






def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()

setup()