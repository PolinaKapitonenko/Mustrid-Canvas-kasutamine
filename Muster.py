from tkinter import*
from math import*

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=1300, height=700, background="white")
tahvel.grid()
k=10
x0=400
y0=50
x1=630
y1=280
a=115
r=(a**2+a**2)**(1/2)
p=(a-r)

for i in range(12):
    x0+=p
    y0+=p
    x1-=p
    y1-=p
    
    tahvel.create_rectangle(x0,y0,x1,y1, width=1, fill="red" )
    tahvel.create_oval(x0, y0, x1, y1,width=1, fill="yellow")
    p=r-a
    r=r-p
    a=((r)*sqrt(2))/2
tahvel.grid()


x1=40
y1=x1*8
for x in range(8):
    for c in range (8):
            x2=x*x1
            y2=c*x1
            if(x+c)%2==0:
                color="white"
            else:
                color="black"
            y=tahvel.create_rectangle(x2,y2,x2+x1,y2+x1,fill=color)
raam.mainloop()