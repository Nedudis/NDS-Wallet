from bs4 import BeautifulSoup
import requests
import json
from collections import deque
from dataclasses import dataclass

@dataclass
class LinkGetter():
    index: int
    base_url: str
    sname: str

LINKS: deque[LinkGetter] = [
    (0, "https://www.google.com/finance/markets/indexes/americas", "america"),
    (1, "https://www.google.com/finance/markets/indexes/asia-pacific", "asia"),
    (2, "https://www.google.com/finance/markets/indexes/europe-middle-east-africa", "europe")
]

config: dict
with open('././config.json', "r") as jsonfile:
    config = json.load(jsonfile)
    jsonfile.close()
currency = config['currency']

def check_rate():
    if currency == 'USD':
        return 1.0000
    elif currency == 'EUR':
        r = requests.get('https://www.google.com/finance/quote/EUR-USD')
        page_parse = BeautifulSoup(r.text, 'html.parser')
        rate = float(page_parse.find("div", {"class":"YMlKec fxKbKc"}).text)
        return rate

exchange_rate = check_rate()

class Indexes():

    def __init__(self, index: int) -> None:
        self.index: int = index

    def request(self):
        r = requests.get(LINKS[self.index][1])

        page_parse = BeautifulSoup(r.text, 'html.parser')

        sr = page_parse.find("ul", {"class":"sbnBtf"}, "li")

        sr_name: deque = sr.find_all("div", {"class":"ZvmM7"})
        sr_price: deque = sr.find_all("div", {"class":"YMlKec"})
        sr_changes: deque = sr.find_all("div", {"class":"BAftM"})

        return sr_name, sr_price, sr_changes
    
    def combine_arrays(self):
        name_list: deque[str]
        price_list: deque[str]
        changes_list: deque[str]

        name_list, price_list, changes_list = self.request()

        for i in range(0, len(name_list)):
            name_list[i] = name_list[i].text
            price_list[i] = round((float(price_list[i].text.replace(",", "")) / exchange_rate), 2)
            changes_list[i] = round((float(changes_list[i].text.replace(",", "")) / exchange_rate), 5)
        
        return deque(zip(name_list, price_list, changes_list))

if __name__ == "__main__":
    print(Indexes(1).combine_arrays())