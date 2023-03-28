import tkinter as tk
from tkinter import*
from tkinter import font


# LIPP
def bahamas():
    canvas.create_rectangle(0, 0, 300, 200, fill="#78DBE2")
    canvas.create_rectangle(0, 66, 300, 133, fill="yellow")
    canvas.create_polygon([0, 0], [100, 100], [0, 200], fill="black")

def estonia():
    canvas.create_rectangle(0, 0, 300, 200/3.0*1.0 , fill="blue")
    canvas.create_rectangle(0 ,200/3.0*1.0 ,300 ,200/3.0*2.0 ,fill="black")
    canvas.create_rectangle(0 ,200/3.0*2.0 ,300 ,200/3.0*3.1 ,fill="white")

root = tk.Tk()
root.title("Lippud")

canvas = tk.Canvas(root,
                   width=300,
                   height=200,
                   bg="cyan")
canvas.pack()

bahamas_button = tk.Button(root,text="Lipp Bahamas",command=bahamas)
bahamas_button.pack()

Eesti_button = tk.Button(root,text="Lipp Eesti",command=estonia)
Eesti_button.pack()



def kolumbi():
    canvas.create_rectangle(0, 0, 300, 200/3.0*1.0 , fill="yellow")
    canvas.create_rectangle(0 ,200/3.0*1.0 ,300 ,200/3.0*2.0 ,fill="blue")
    canvas.create_rectangle(0 ,200/3.0*2.0 ,300 ,200/3.0*3.1 ,fill="red")

kolumbi_button = tk.Button(root,text="Lipp Kolumbi",command=kolumbi)
kolumbi_button.pack()


root.mainloop()




            