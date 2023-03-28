from tkinter import*

def valik5():
        raam = Tk()
        raam.title("Tahvel")
        tahvel = Canvas(raam, width=350, height=350, background="white")
        tahvel.grid()

        x1=35
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

