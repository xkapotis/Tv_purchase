import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date



def scraper_plaisio(plaisio_links):

    plaisio_prices = []
    for url in plaisio_links:
        page_plaisio = requests.get(url)
        soup_plaisio = BeautifulSoup(page_plaisio.content, 'html.parser')
        
        # print(soup_plaisio.prettify())

        for item in soup_plaisio.find_all( 'div', class_ = "product" ):
            try:
                row = []
                title = item.find("span", class_ = "product-title").a.span.get_text()
                
                # print(title)
            
                current_price = item.find("div", class_ = "price").find("div", class_ = "price").get_text()
                # print(len(current_price))
                if len(current_price) <= 3:
                    main_price = item.find("div", class_ = "price").get_text()
                    main_price = float(main_price[0:3])
                else:
                    main_price = item.find("div", class_ = "price").get_text()
                    main_price = float(main_price[0:4])
                
                current_price = float(current_price)

                row.append(title)
                row.append(main_price)
                row.append(current_price)
                plaisio_prices.append(row)
            except AttributeError:
                print("None")

    plaisio_prices_df = pd.DataFrame(plaisio_prices, columns = ["Title", "Main Price", "Current Price"])
    plaisio_prices_df["Store"] = "PLAISIO"
    # print(plaisio_prices_df)

    today = str(date.today())
    file_name = "plaisio_prices_"+today+".csv"
    path = "./results/"+file_name
    plaisio_prices_df.to_csv(path, index = False)
