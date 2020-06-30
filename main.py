import pandas as pd
from scraper_kotsovolos import scraper_kotsovolos
from scraper_plaisio import scraper_plaisio
from comparison import comparison
from toSql import toSql

kotsovolos_link = "https://www.kotsovolos.gr/sound-vision/televisions/led-lcd?beginIndex=0&pageSize=200"

plaisio_links = [
    "https://www.plaisio.gr/tileoraseis/tvs/view-48",
    "https://www.plaisio.gr/tileoraseis/tvs/page-2/view-48",
    "https://www.plaisio.gr/tileoraseis/tvs/page-3/view-48",
    "https://www.plaisio.gr/tileoraseis/tvs/page-4/view-48"
]

scraper_kotsovolos(kotsovolos_link)
scraper_plaisio(plaisio_links)

comparison()
toSql()