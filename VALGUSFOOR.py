import tkinter as tk
from tkinter import*
from tkinter import font
from math import*
raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=650, height=800, background="white")
tahvel.grid()
tahvel.create_line(320,550,  570,550,  width=500 , fill="#5c5959")
suur_font = font.Font(family='Helvetica', size=20, weight='bold')
tahvel.create_line(420,400,  470,400,  width=45 , fill="red")
tahvel.create_line(420,450,  470,450,  width=45 , fill="yellow")
tahvel.create_line(420,500,  470,500,  width=45 , fill="green")
tahvel.create_line(445 ,530,  445,750,  width=8 , fill="black")
tahvel.create_line(350,760,  530,760,  width=4 , fill="black")
raam.mainloop()