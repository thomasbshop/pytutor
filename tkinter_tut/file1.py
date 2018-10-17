# Reference
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html, https://tkdocs.com/tutorial/index.html
# www.python-course.eu/python_tkinter.php, https://wiki.python.org/moin/TkInterhttps://wiki.python.org/moin/TkInter

try:
    import tkinter
except ImportError:  # running python2
    import TKinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()
mainWindow = tkinter.Tk()
mainWindow.title("Hello World!!!")
mainWindow.geometry('640x480+50+200')

# pack manager - everything in Tk is a window and objects are placed in a hirachy.
# mainwindow is the root window and everything must be placed within it or one ofits child windows.
# Not every window can have children but every window except the root one must have a master window
label = tkinter.Label(mainWindow, text="This is our window")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='w', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
# canvas.pack(side='top', fill=tkinter.Y, expand=True)
canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=False)
button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

# buttons


mainWindow.mainloop()
