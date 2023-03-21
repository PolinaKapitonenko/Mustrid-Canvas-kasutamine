import tkinter as tk
from tkinter import*
from tkinter import font
raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=1000, height=1000, background="white")
tahvel.create_line(320, 550,570,550, width=500 , fill="#a3a7ad")
suur_font = font.Font (family='Helvetica', size=20, weight='bold')
tahvel. create_text (370, 310, text="Valgusfoor", font=suur_font, anchor=NW) 
tahvel.create_line(420, 400,470,400, width=45, fill="red")
tahvel.create_line(420, 450,470,450, width=45, fill="yellow")
tahvel.create_line(420, 500,470,500, width=45, fill="green")

tahvel.create_line(445,530, 445,750, width=8, fill="black")
tahvel.create_line(350,760, 530,760,width=4, fill="black")


raam.mainloop()
