class Item():

    def __init__(self, name, value):

        self._name = name
        self._value = value

        all_items.append(self)

        #adds all the names to make the drop down
        item_name.append(name)

   
    def get_name(self):
        ''' Return name of item '''

        return self._name

    def get_value(self):
        ''' Return value of item '''

        return self._value
    

def generate_items():
    ''' Import students from a csv file'''
    # Import the csv package to enable the program to work with a csv
    import csv
    # Open the csv file, call is csvfile
    with open('products2.csv', newline='') as csvfile:
        # use the reader() function and put the results into a variable called filereader
        filereader = csv.reader(csvfile)
        # Loop through the csv, one row at a time
        
        for line in filereader:
            # For each row, create a new item
            
            Item(line[0], int(line[1]))

def print_selection():
    ''' prints the selected value '''

    print(items_listbox.curselection())

    for num in items_listbox.curselection():
        print(all_items[num].get_name())

def fill_listbox():
    """fills the listbox"""

     # delete all items for the listbox
    items_listbox.delete(0, END)  
    
    for i in all_items:
        items_listbox.insert(END, i.get_name())


def delete_item():
    """deletes a item"""

    for num in items_listbox.curselection():
        del all_items[num]
      
    # re populates the listbox
    fill_listbox()

item_name = []

all_items = []

generate_items()



from cProfile import label
from select import select
from tkinter import *
from tkinter import messagebox
from tokenize import Single
root = Tk()
root.title("opption")
root.geometry("800x500")

items_listbox = Listbox(root, selectmode=Single)
items_listbox.grid(row=0)

fill_listbox()



# button to selelet the selceted item

select_btn = Button(root, text="select", command=print_selection)
select_btn.grid(row=1)

# lable to display the name and value
details = StringVar()
details_lbl = Label(root, textvariable=details)
details_lbl.grid(row=2)

# button for deleting items
delete_btn = Button(root, text="delete", command=delete_item)
delete_btn.grid(row=1, column=1)


root.mainloop()