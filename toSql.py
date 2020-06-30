import pyodbc
import pandas as pd
from sql_queries import queries


def toSql():
    #### DBs variables
    datawarehouse_name = "Stores"
    target_cnxn = pyodbc.connect(       "Driver={SQL Server Native Client 11.0};"
        "Server=DESKTOP-JTQP8GI\@@@@@@@@@@@;"
        "Database="+datawarehouse_name+";"
        "UID=@@@@@@@@@@@;"
        "PWD=@@@@@@@@@@@@@@@@@;"
        "Trusted_Connection=yes;"
        )

    ##### connections ######
    target_cursor_cnxn = target_cnxn.cursor()

    ######## Queries ##########
    queries(target_cursor_cnxn)

