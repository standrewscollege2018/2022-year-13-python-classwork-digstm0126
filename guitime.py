''' into to tkinter '''

# inports tkinter
from tkinter import *

# set up the root windo
root = Tk()
root.title("my first tkinter gui very cool")
root.resizable(width=FALSE, height=FALSE)
root.geometry("800x500")

# add a label
heading_lbl = Label(root, text="brak the bad", fg="blue", font=("papyrus, 25"))
heading_lbl.pack()

root.mainloop()
