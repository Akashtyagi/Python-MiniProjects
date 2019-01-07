# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 13:05:46 2018

@author: Akash
"""

import sqlite3

class Database_class:
    
    def __init__(self):
         # sqlite3.connect connects to database name if such database exist and if doesn't exist,
        # it creates a database by that name and then connects to it.
        self.connection = sqlite3.connect("BloodDatabase.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS donor (id INTEGER PRIMARY KEY,Name TEXT,BloodGroup Text,City Text,Contact integer)")
        self.connection.commit()
        
    def insertTable(self,name,bloodgroup,city,contact):
        self.connection = sqlite3.connect("BloodDatabase.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO donor VALUES (NULL,?,?,?,?)",(name,bloodgroup,city,contact))
        self.connection.commit()
        self.connection.close()
       
    def show(self):
        self.connection = sqlite3.connect("BloodDatabase.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM donor")
        databaseValue = self.cursor.fetchall()           # cursor.fetchall() to fetch all the data from table to python variable
        return databaseValue
    
    def delete(self,id):
        self.connection = sqlite3.connect("BloodDatabase.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM donor WHERE id=?",(id,))
        self.connection.commit()
    
    def updateTable(self,id,name,bloodgroup,city,contact):
        self.connection = sqlite3.connect("BloodDatabase.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("UPDATE donor SET name=?,bloodgroup=?,city=?,contact=? WHERE id=?",(name,bloodgroup,city,contact,id))
        self.connection.commit()
       
    def search(self,name="",bloodgroup="",city="",contact=""):
        self.connection = sqlite3.connect("BloodDatabase.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM  donor WHERE name=? OR bloodgroup=? OR City=? OR Contact=?",(name,bloodgroup,city,contact))
        databaseValue = self.cursor.fetchall()           # cursor.fetchall() to fetch all the data from table to python variable
        self.connection.commit()
        self.connection.close()
        return databaseValue
       
    
    #insertTable("Akash Tyagi","O+","Noida",7579212810)
    #insertTable("Amit","AB+","Delhi",9999415785)
    #insertTable("David","B+","Pune",9000415785) 
    #print(search(name="Madhu Tyagi"))
    #delete(2)
#    updateTable(8,"Madhu Tyagi","O-","Banglore",242424) 
    #print("Search Result: ",search(city="Noida"))
    #print("All: ",show())
    #updateTable("TVS",80000,"Apache180")
