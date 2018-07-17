# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.
import tkinter

keys = [[('C', 2), ('CE', 2)],
        [('7', 2), ('8', 2), ('9', 2), ('+', 2)],
        [('4', 2), ('5', 2), ('6', 2), ('-', 2)],
        [('1', 2), ('2', 2), ('3', 2), ('*', 2)],
        [('0', 2), ('=', 4), ('/', 2)],
        ]

mainWindowPaddingX = 20
mainWindowPaddingY = 20

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('640x480')
mainWindow['padx'] = mainWindowPaddingX
mainWindow['pady'] = mainWindowPaddingY

result = tkinter.Entry(mainWindow)
result.grid(row=1, column=5)

keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=10, column=5)

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1

mainWindow.update()
# mainWindow.minsize(keyPad.winfo_width() + mainWindowPaddingX, result.winfo_height() + keyPad.winfo_height())
# mainWindow.maxsize(keyPad.winfo_width() + mainWindowPaddingX, result.winfo_height() + keyPad.winfo_height())

mainWindow.mainloop()
