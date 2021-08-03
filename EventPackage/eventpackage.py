import datetime
import sqlite3
from sqlite3 import Error


class DatetimeEventStore():
    dbconnection = None
    dbcursor = None

    def __init__(self):
        try: 
            temp = open("eventdb.db")
            temp.close()
            self.dbconnection = sqlite3.connect("eventdb.db")
            self.dbcursor = self.dbconnection.cursor()
        except IOError:
            print("\"eventdb.db\" doesn't exist.")

    def store_event(self, at, data):
        if (at == None or data == None):
            print("One or two of the parameters is null / Datetime format isn't good")
        args = (at, data)
        try :
            self.dbcursor.execute("INSERT INTO event (date,data) VALUES (?, ?)", args)
            self.dbconnection.commit()
        except Error as e:
            print (e)

    def get_events(self, start, end):
        if (start == None or end == None):
            print("One or two of the parameters is null / Datetime format isn't good")
        args = (start, end)
        try:
            self.dbcursor.execute("SELECT * FROM event WHERE date >= ? AND date <= ?", args)
            result = self.dbcursor.fetchall()
            return (result)
        except Error as e:
            print(e)