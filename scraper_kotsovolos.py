import requests
from  bs4 import BeautifulSoup
import pandas as pd
import re 
from datetime import date


def scraper_kotsovolos(kotsovolos_link):

    page = requests.get(kotsovolos_link)
    soup = BeautifulSoup(page.content, "html.parser")

    kotsovolos = []
    for item in soup.find_all( 'div', class_ = "product" ):
        try:
            row = []
            title = item.div.h2.get_text()
            price = item.find("div", class_ = "price").get_text()
            row.append(title)
            row.append(price)
            kotsovolos.append(row)

        except AttributeError:
            print("No Title")
            print("No Price")

    df = pd.DataFrame(kotsovolos, columns = ["Title", "price"])
    df["Title"] = df["Title"].str.replace("\n", "")
    df["price"] = df["price"].str.replace("\n", "")
    df["price"] = df["price"].str.replace("\t", "")
    df["price"] = df["price"].str.split("κερδίζεις").str[0]

    price_table = []
    for price in df["price"]:
        row = []
        if len(price) <= 8:
            main_price = price
            current_price = price
        else:
            main_price = price[4:10]
            current_price = price[11:19]
    
        row.append(main_price)
        row.append(current_price)
        price_table.append(row)


    price_table_df = pd.DataFrame(price_table, columns = ["Main Price", "Current Price"])

    df = df.drop(columns=["price"])
    df["Main Price"] = price_table_df["Main Price"]
    df["Current Price"] = price_table_df["Current Price"]
    df["Main Price"] = df["Main Price"].str.replace("€", "")
    df["Current Price"] = df["Current Price"].str.replace("€", "")
    df["Store"] = "KOTSOVOLOS"



    # print(df.head())
    today = str(date.today())
    file_name = "kotsovolos_prices_"+today+".csv"
    path = "./results/"+file_name
    df.to_csv(path, index=False)




