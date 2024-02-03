from bs4 import BeautifulSoup
import requests
import json
from icecream import ic
LINK = "https://www.google.com/finance/markets/cryptocurrencies"

config = {}
with open('././config.json', "r") as jsonfile:
    config = json.load(jsonfile)
    jsonfile.close()
currency = config['currency']
currency_exchange_rate_cfg = config['currency_exchange_rate']

def check_rate():
    if currency == 'USD':
        return 1.0000
    elif currency == 'EUR':
        if currency_exchange_rate_cfg == 1.0000:
            r = requests.get('https://www.google.com/finance/quote/EUR-USD')
            page_parse = BeautifulSoup(r.text, 'html.parser')
            rate = float(page_parse.find("div", {"class":"YMlKec fxKbKc"}).text)
            config['currency_exchange_rate'] = rate
            with open('././config.json', "w") as cfg:
                json.dump(config, cfg)
                cfg.close()
            return rate
        elif currency_exchange_rate_cfg != 1.0000:
            return currency_exchange_rate_cfg
        
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
        return search_results_name_short, search_results_price, search_results_name

    def combine_arrays(self):
        name_list_short, price_list, name_list = self.request()
        crypto_names = []
        crypto_names_short = []
        crypto_prices = []
        for i in range(0, len(name_list_short)):
            crypto_names.append(name_list[i].text)
            crypto_names_short.append(name_list_short[i].text)
            crypto_prices.append(round(float(price_list[i].text.replace(",", "")) / exchange_rate, 4))

        return list(zip(crypto_names, crypto_names_short, crypto_prices))
