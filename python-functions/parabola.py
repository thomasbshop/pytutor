try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


def parabola(x):
    y = x * x / 100
    return y


def draw_axes(page):
    canvas.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, -y_origin, 0, y_origin, fill="black")
    print(locals())  # has to be in a function for this to be called


def plot(canvas, x, y):
    canvas.create_line(x, y, x+1, y+1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("900x640")

canvas = tkinter.Canvas(mainWindow, width=450, height=640)
canvas.grid(row=0, column=0)
canvas1 = tkinter.Canvas(mainWindow, width=450, height=640)
canvas1.grid(row=0, column=1)

print(repr(canvas), repr(canvas1))

draw_axes(canvas)
draw_axes(canvas1)

for x in range(-1000, 1001):
    y = parabola(x)
    plot(canvas, x, y)

mainWindow.mainloop()
