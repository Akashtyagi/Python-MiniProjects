# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 20:26:56 2018

@author: Akash
"""
# =============================================================================
# GUI Application to store information about all the blood donors
# =============================================================================

import tkinter as tk
from database import Database_class

database = Database_class()

def selected_row(event):
    global selected_rowdata
    global index
    try:
        index = database_list.curselection()[0]
        selected_rowdata = database_list.get(index)
        print(selected_rowdata)
        print(selected_rowdata[0])
        name_entry1.delete(0,tk.END)
        name_entry1.insert(tk.END,selected_rowdata[1])
        blood_entry1.delete(0,tk.END)
        blood_entry1.insert(tk.END,selected_rowdata[2])
        city_entry1.delete(0,tk.END)
        city_entry1.insert(tk.END,selected_rowdata[3])
        contact_entry1.delete(0,tk.END)
        contact_entry1.insert(tk.END,selected_rowdata[4])
    except IndexError:
        pass


def viewDatabase():
    database_list.delete(0,tk.END)
    for row in database.show():
        database_list.insert(tk.END,row)
        
def searchDatabase():
    database_list.delete(0,tk.END)
    for row in database.search(name.get(),blood_group.get(),city.get(),contact.get()):
        database_list.insert(tk.END,row)
        
def addToDatabase():
    database.insertTable(name.get(),blood_group.get(),city.get(),contact.get())
    database_list.delete(0,tk.END)
    database_list.insert(tk.END,(name.get(),blood_group.get(),city.get(),contact.get()))

def deleteEntry():
    database.delete(selected_rowdata[0])
    database_list.delete(0,tk.END)
    for row in database.show():
        database_list.insert(tk.END,row)

def updateDatabase():
    print("X",selected_rowdata[0],name.get(),blood_group.get(),city.get(),contact.get())
    database.updateTable(selected_rowdata[0],name.get(),blood_group.get(),city.get(),contact.get())
    database_list.delete(0,tk.END)
    for row in database.show():
        database_list.insert(tk.END,row)

    

window = tk.Tk()

#   Label-1
blood_label1 = tk.Label(window,text = "Blood Group")
blood_label1.grid(row=0,column=2)
#   Entry-1
blood_group = tk.StringVar()
blood_entry1 = tk.Entry(window,textvariable=blood_group)
blood_entry1.grid(row=0,column=3)

#   Label-2
name_label2 = tk.Label(window,text = "Name")
name_label2.grid(row=0,column=0)
#   Entry-2
name = tk.StringVar()
name_entry1 = tk.Entry(window,textvariable=name)
name_entry1.grid(row=0,column=1)

#   Label-3
label3 = tk.Label(window,text = "City")
label3.grid(row=1,column=0)
#   Entry-3
city = tk.StringVar()
city_entry1 = tk.Entry(window,textvariable=city)
city_entry1.grid(row=1,column=1)

#   Label-4
label4 = tk.Label(window,text = "Contact")
label4.grid(row=1,column=2)
#   Entry-4
contact = tk.StringVar()
contact_entry1 = tk.Entry(window,textvariable=contact)
contact_entry1.grid(row=1,column=3)

#   List Box
database_list = tk.Listbox(window,height=6,width=35)
database_list.grid(row=2,column=0,rowspan=6,columnspan=2)


database_list.bind('<<ListboxSelect>>',selected_row)        # .bind() is used to bind a functionality to specific element.In this case on 
                                                            # selecting list from Listbox to show all the data of that list.

#   Scrollbar
scrollbar = tk.Scrollbar(window)
scrollbar.grid(row=2,column=2,rowspan=6)

#   Relating List and Scrollbar to each other
database_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=database_list.yview)

#    View Donors
view_button = tk.Button(window,text="View Database",command=viewDatabase)
view_button.grid(row=2,column=3,sticky=tk.NSEW)

#    Search Donor
search_button = tk.Button(window,text="Search Donor",command=searchDatabase)
search_button.grid(row=3,column=3,sticky=tk.NSEW)

#   Add Donor Button!
add_button = tk.Button(window,text = "Add Donor",command=addToDatabase)
add_button.grid(row=4,column=3,sticky=tk.NSEW)


#    Update Do-not Button
update_button = tk.Button(window,text="Update Donor",command=updateDatabase)
update_button.grid(row=5,column=3,sticky=tk.NSEW)

#    Delete Donor
delete_button = tk.Button(window,text="Delete Donor",command=deleteEntry)
delete_button.grid(row=6,column=3,sticky=tk.NSEW)

    
window.mainloop()

# =============================================================================
# Creating a executeable .exe file
# =============================================================================
#pyinstaller --onefile --windowed BloodBank.py






