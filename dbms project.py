# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 23:21:26 2018

@author: Shreyes
"""

import mysql.connector
from prettytable import from_db_cursor


try:
    db = mysql.connector.connect(
                host = 'HostIPAddr eg. localhost',
                port = 3306,
                user = 'username',
                passwd = 'password to connect to mysql server/host',
                database = 'Your_DB_Name',
                buffered = True)
    cursor = db.cursor()
    print('Connected to database')
except:
    db = mysql.connector.connect(
                host = 'HostIPAddr eg. localhost',
                port = 3306,
                user = 'username',
                passwd = 'password to connect to mysql server/host',
                buffered = True)
    db.cursor().execute('create database Your_DB_Name')
    db.commit()
    db.connect(database = 'Your_DB_Name')
    cursor=db.cursor()
        

def clear_database():
    global cursor,db
    cursor.execute('DROP DATABASE Your_DB_Name')
  
    
def create_tables():
    global cursor,db
    cursor.execute('''create table samplequery''')


if __name__=='__main__':
    #clear_database()
    create_tables()
    cursor.execute('describe samplequery')
    print(from_db_cursor(cursor))
    
    
    
