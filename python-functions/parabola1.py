# use different names when naming local and global parameters, no shadowing
import math

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)


def circle(page, radius, g, h):
    # use this for better output and performance
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline='blue', width=1)

    # for x in range(g * 100, (g + radius) * 100):  # plot 100 times more, reduces performance
    #     x /= 100  # scale x back to the intended value
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, -y_origin, 0, y_origin, fill="black")
    print(locals())  # has to be in a function for this to be called, looks at the variables in that function.


def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill="red")
    # page.create_line(x, -y, x + 1, y + 1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("900x640")

canvas = tkinter.Canvas(mainWindow, width=900, height=640)
canvas.grid(row=0, column=0)

print(repr(canvas))

draw_axes(canvas)

# handled by function parabola
# for x in range(-1000, 1001):
#     y = parabola(x)
#     plot(canvas, x, y)

parabola(canvas, 100)
parabola(canvas, 200)
parabola(canvas, 89)
circle(canvas, 100, 100, 100)
circle(canvas, 100, 100, -100)
circle(canvas, 100, -100, 100)
circle(canvas, 100, -100, -100)
circle(canvas, 10, 100, 100)
circle(canvas, 10, 100, -100)
circle(canvas, 10, -100, 100)
circle(canvas, 10, -100, -100)
circle(canvas, 30, 0, 0)


mainWindow.mainloop()
