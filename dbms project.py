# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 23:21:26 2018

@author: Shreyes
"""

import mysql.connector
from prettytable import from_db_cursor
from tkinter import *


try:
    db = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                passwd = 'root',
                database = 'College',
                buffered = True)
    cursor = db.cursor()
    print('Connected to database')
except:
    db = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                passwd = 'root',
                buffered = True)
    db.cursor().execute('create database College')
    db.commit()
    db.connect(database = 'College')
    cursor=db.cursor()
        

def clear_database():
    global cursor,db
    cursor.execute('DROP DATABASE College')
  
    
def create_tables():
    global cursor,db
    cursor.execute('''create table if not exists Student(
            USN char(10) not null)''')


if __name__=='__main__':
    #clear_database()
    create_tables()
    cursor.execute('describe Student')
    print(from_db_cursor(cursor))
    
    
    