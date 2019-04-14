import tkinter

root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack()

bottomframe = tkinter.Frame(root)
bottomframe.pack( side = "bottom" )

redbutton = tkinter.Button(frame, text="Red", fg="red")
redbutton.pack( side = "left")

greenbutton = tkinter.Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = "left" )

bluebutton = tkinter.Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = "left" )

blackbutton = tkinter.Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = "bottom")


root.mainloop()


