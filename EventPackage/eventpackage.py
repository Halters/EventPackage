import datetime
import sqlite3
from sqlite3 import Error


class DatetimeEventStore():
    dbconnection = None

    def __init__(self):
        