from tkinter import*


def draw_pattern(canvas, x, y, size, depth):
    if depth == 0:
        return

    canvas.create_rectangle(x, y, x + size, y + size, outline='black')
    new_size = size / 3

    # joonistame nurgad
    draw_pattern(canvas, x, y, new_size, depth - 1)
    draw_pattern(canvas, x + 2 * new_size, y, new_size, depth - 1)
    draw_pattern(canvas, x, y + 2 * new_size, new_size, depth - 1)
    draw_pattern(canvas, x + 2 * new_size, y + 2 * new_size, new_size, depth - 1)

    # joonistame keskmised ruudud
    draw_pattern(canvas, x + new_size, y, new_size, depth - 1)
    draw_pattern(canvas, x, y + new_size, new_size, depth - 1)
    draw_pattern(canvas, x + 2 * new_size, y + new_size, new_size, depth - 1)
    draw_pattern(canvas, x + new_size, y + 2 * new_size, new_size, depth - 1)


def submit():
    canvas.delete("all")
    try:
        depth = int(entry.get())
        size = int(entry2.get())
    except ValueError:
        return

    draw_pattern(canvas, 0, 0, size, depth)


# loome akna
root = Tk()
root.title("Rekursiivne muster")

# loome tekstikastid
label = Label(root, text="Sisesta sügavus:")
label.pack()

entry = Entry(root)
entry.pack()

label2 = Label(root, text="Sisesta suurus:")
label2.pack()

entry2 = Entry(root)
entry2.pack()

button = Button(root, text="Joonista muster", command=submit)
button.pack()

# loome lõuendi
canvas = Canvas(root, width=500, height=500)
canvas.pack()

# käivitame GUI
root.mainloop()