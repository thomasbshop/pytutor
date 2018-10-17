# easier to use than pack

try:
    import tkinter
except ImportError:  # running python2
    import TKinter as tkinter

keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)],
        ]

mainWindowPadding = 8

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('380x400-8-200')
mainWindow['padx'] = mainWindowPadding
mainWindow['pady'] = mainWindowPadding


# widget to display the screen
displayscreen = tkinter.Entry(mainWindow)
displayscreen.grid(row=0, column=0, sticky='nsew')

keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

# numbers
row = 1
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1

mainWindow.update()
mainWindow.minsize(keyPad.winfo_width() + (2 * mainWindowPadding), displayscreen.winfo_height() + keyPad.winfo_height()
                   + mainWindowPadding)
mainWindow.maxsize(keyPad.winfo_width() + (2 * mainWindowPadding), displayscreen.winfo_height() + keyPad.winfo_height()
                   + mainWindowPadding)

mainWindow.mainloop()
