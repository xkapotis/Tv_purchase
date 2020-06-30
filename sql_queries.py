import pandas as pd
from datetime import date
import pyodbc


def queries(target_cursor_cnxn):

    today = str(date.today())
    file_name = "results_"+today+".csv"
    path = "./results/"+file_name
    results = pd.read_csv(path)

    x = results.values.tolist()

    insert_results = '''
    INSERT INTO Stores_TVs (tv_title, tv_id, store, current_price, date )
    VALUES (?, ?, ?, ?, ?);'''

    for row in x:
        target_cursor_cnxn.execute(insert_results, (row[0], row[1], row[2], row[3], row[4]))
    target_cursor_cnxn.commit()


