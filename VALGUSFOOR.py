import tkinter as tk
from tkinter import*
from tkinter import font
from math import*
raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=160, height=400, background="white")
tahvel.grid()
tahvel.create_line(0,0,  800,0,  width=800 , fill="#5c5959")
suur_font = font.Font(family='Helvetica', size=20, weight='bold')
tahvel.create_line(60,50,  100,50,  width=45 , fill="red")
tahvel.create_line(60,100,  100,100,  width=45 , fill="yellow")
tahvel.create_line(60,150,  100,150,  width=45 , fill="green")
tahvel.create_line(80 ,180,  80,300,  width=8 , fill="black")
tahvel.create_line(30,310,  140,310,  width=4 , fill="black")
raam.mainloop()