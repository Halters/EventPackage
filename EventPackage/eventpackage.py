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
        dateStr = None
        if (at == None or data == None or type(at != datetime)):
            print("One or two of the parameters is null / Datetime format isn't good")
        dateStr = at.strftime("%d-%b-%Y")
        args = (dateStr, data)
        try :
            print("1")
            self.dbcursor.execute("INSERT INTO event (data,date) VALUES (?, ?)", args)
            self.dbconnection.commit()
            print("2")
        except Error as e:
            print(e)
        