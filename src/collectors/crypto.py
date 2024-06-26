from bs4 import BeautifulSoup
import requests
import json
from decimal import Decimal

from collections import deque

import os
import ctypes

path = os.getcwd()
func = ctypes.CDLL(os.path.join(path, "src/collectors/func.so"))
func.get_subname.restype = ctypes.c_char

LINK = "https://www.google.com/finance/markets/cryptocurrencies"

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

class CryptoCurrencyPrices():
    def __init__(self) -> None:
        pass

    def request(self):
        r = requests.get(LINK)
        page_parse = BeautifulSoup(r.text, 'html.parser')
        search_results_name_short = page_parse.find("ul", {"class":"sbnBtf"}, "li").find_all("div", {"class":"COaKTb"})
        search_results_price = page_parse.find("ul", {"class":"sbnBtf"}, "li").find_all("div", {"class":"YMlKec"})
        search_results_name = page_parse.find("ul", {"class":"sbnBtf"}, "li").find_all("div", {"class":"ZvmM7"})
        search_results_changes = page_parse.find("ul", {"class":"sbnBtf"}, "li").find_all("div", {"class":"BAftM"})
        return search_results_name_short, search_results_price, search_results_name, search_results_changes

    def combine_arrays(self):
        name_list_short: deque
        price_list: deque
        name_list: deque
        changes_list: deque
        name_list_short, price_list, name_list, changes_list = self.request()
        cn_temp: deque = []

        for i in range(0, len(changes_list)):
            cn_temp.append(name_list[i].text.encode())
            name_list_short[i] = name_list_short[i].text
            price_list[i] = round(Decimal(float(price_list[i].text.replace(",", "")) / exchange_rate), 5)
            changes_list[i] = round(Decimal(float(changes_list[i].text.replace(",", "")) / exchange_rate), 5)
        size = len(cn_temp)
        name_list = (ctypes.c_char_p * size)()
        cn_temp_c = (ctypes.c_char_p * size)(*cn_temp)
        func.get_subname(cn_temp_c, size, name_list)
        
        return deque(zip(name_list, name_list_short, price_list, changes_list))
