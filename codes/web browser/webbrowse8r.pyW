import tkinter as tk
from tkinter import *
import webbrowser

win=tk.Tk()
win.title("web browser")
win.geometry("350x250")

def google():
    webbrowser.open("www.google.com")

def flipkart():
    webbrowser.open("www.flipkart.com")

def whatsapp():
    webbrowser.open("www.whatsapp.com")

def instagram():
    webbrowser.open("www.instagram.com")

def youtube():
    webbrowser.open("www.youtube.com")

def amazon():
    webbrowser.open("www.amazon.com")

igoogle=PhotoImage(file="google.png")
google=tk.Button(win,image=igoogle,command=google)
google.grid(row=0,column=0)

iyoutube=PhotoImage(file="youtube.png")
youtube=tk.Button(win,image=iyoutube,command=youtube)
youtube.grid(row=0,column=1)

iamazon=PhotoImage(file="amazon.png")
amazon=tk.Button(win,image=iamazon,command=amazon)
amazon.grid(row=1,column=0)

iinstagram=PhotoImage(file="insta.png")
instagram=tk.Button(win,image=iinstagram,command=instagram)
instagram.grid(row=1,column=1)

iflipkart=PhotoImage(file="flipkart.png")
flipkart=tk.Button(win,image=iflipkart,command=flipkart)
flipkart.grid(row=0,column=2)

iwhatsapp=PhotoImage(file="whatsapp.png")
whatsapp=tk.Button(win,image=iwhatsapp,command=whatsapp)
whatsapp.grid(row=0,column=3)

win.mainloop()
