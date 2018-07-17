import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()
mainWindow = tkinter.Tk()
mainWindow.geometry('640x480+50+500')

label = tkinter.Label(mainWindow, text='It\'s a box Dude!')
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.pack()

mainWindow.mainloop()
