from tkinter import *

window = Tk()

button1 = Button(window, text="1")
button2 = Button(window, text="2")
button3 = Button(window, text="3")

button1.pack(side=BOTTOM, fill=X, ipadx=10, ipady=10, padx=10, pady=10)
button2.pack(side=BOTTOM, fill=X, ipadx=10, ipady=10, padx=10, pady=10)
button3.pack(side=BOTTOM, fill=X, ipadx=10, ipady=10, padx=10, pady=10)

window.mainloop()