
import string

# crates the move class witch will hold all the info about the movie
class Movie():

    # adds all of the posable values to the movie object
    def init__(self, name, price, time, seats, theatre):

        self._name = name.strip()
        self._price = price
        self._time = time
        self._seats = seats
        self._theatre = theatre.strip()

        all_items.append(self)
    
    # can give the name of the movie 
    def get_name(self):
        return self._name
    # can give the price of the movie 
    def get_value(self):
        return self._price

    # can give the time of the movie 
    def get_time(self):
        return self._time

    # can give the amout of sets left for the movie 
    def get_seats(self):
        return self._seats

    # can give the therter  the movie is in
    def get_theatre(self):
        return self._theatre

    # allows you to check if the amount of tickets is to much or the wrong input and then remove them
    def sell_seats(self, q):

        if self._seats - q < 0:
            messagebox.showerror("slow down", f"unfortanaly we dont have enghouth tickets for you.")
        elif q < 1:
            messagebox.showerror("try agin that one was terable", f"it has to be a psitive number above 1")
        else:
            self._seats -= q

            
# this generates the movies from the csv into there objects
def generate_items():
    import csv
    with open('movies.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile)

        for line in filereader:
            Movie(line[0], int(line[1]), int(line[2]), int(line[3]), line[4])

# this shows the selected movie and the amount of tickets as well as the show time
def print_selection():

    
    for num in items_listbox.curselection():

        print(selected_theatre_movies[num].get_name())
        details.set(f"{selected_theatre_movies[num].get_name()} will cost ${selected_theatre_movies[num].get_value()} and will start at {selected_theatre_movies[num].get_time()}. There are {selected_theatre_movies[num].get_seats()} seats left.")
        totalprice.set(f"all up the cost is going to be ${selected_theatre_movies[num].get_value() * qty.get()}")


# just populates the list box with the seleced therter
def populate_listbox():
    for i in all_items:
        items_listbox.insert(END, i.get_name())

# this populatests the list box
def movie_theatre(theatre_get):
    items_listbox.delete(0, END)
    global selected_theatre_movies
    selected_theatre_movies = []
    for i in all_items:
        a = i.get_theatre()
        if a == theatre_get:
            selected_theatre_movies.append(i)
            
    for m in selected_theatre_movies:
        items_listbox.insert(END, m.get_name())
    return selected_theatre_movies

# this allows you to acluy book the tickits
def book_ticket():
    try:
        print(items_listbox.curselection())
        for num in items_listbox.curselection():
            if messagebox.askyesno("Confirm sale", f"Confirm booking for {selected_theatre_movies[num].get_name()}, cost of ${selected_theatre_movies[num].get_value() * qty.get()}"):
                selected_theatre_movies[num].sell_seats(qty.get())  
                print_selection()
                clear_entry()
    except:
        messagebox.showerror("Not a number", f"Can't input letters as a number")

# removes the movies
def clear_entry():
    qty_entry.delete(5)

# dose some of the starting stuff so it works
all_items = []
selected_theatre_movies = []
generate_items()


# =========================================

# imports tkinter and all used parts
from tkinter import *
from tkinter import messagebox
from functools import partial

# crates the main box
root = Tk()
root.title("the therters programe")
root.resizable(width=False, height=False)
root.geometry('950x500')

# addeds the tital to the root box as well
title_label = Label(root, text="cool kids therter program")
title_label.grid(row=0, column=3)


# adds the lable for the list box and then adds the list box 
movie_label = Label(root, text="Movies")
movie_label.grid(row=1, column=3)

items_listbox = Listbox(root, selectmode=SINGLE)
items_listbox.grid(row=2, column=3)

# addes the buttons for the 3 difirt therters 
mann_btn = Button(root, text="Mann Theatre", command=partial(movie_theatre, "Mann"))
mann_btn.grid(row=3, column=2)

academy_btn = Button(root, text="Academy", command=partial(movie_theatre, "Academy"))
academy_btn.grid(row=3, column=3)

fern_btn = Button(root, text="Fern Theatre", command=partial(movie_theatre, "Fern"))
fern_btn.grid(row=3, column=4)




# lable for tickets input
tickets_label = Label(root, text="Tickets")
tickets_label.grid(row=4, column=2)

# tickets input
qty = IntVar()
qty_entry = Entry(root, textvariable=qty)
qty_entry.grid(row=4,column=3)

# button to book the tickets
qty_entry_btn = Button(root, text="Book", command=book_ticket)
qty_entry_btn.grid(row=4, column=4)


# separtaing line for the text to spawn in after.
tickets_label = Label(root, text="======================================================================================")
tickets_label.grid(row=5, column=3)


# dislplats the total price
totalprice = StringVar()
totalprice_lbl = Label(root, textvariable=totalprice)
totalprice_lbl.grid(row=6, column=3)

# dislplays how many sets there are left
details = StringVar()
details_lbl = Label(root, textvariable=details)
details_lbl.grid(row=7, column=3)

# coses the main loop 
root.mainloop()