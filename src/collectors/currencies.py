from bs4 import BeautifulSoup
import requests
from decimal import Decimal
import json

LINK = "https://www.google.com/finance/markets/currencies"

class CurrenciesRate():
    def __init__(self) -> None:
        pass

    def request(self):
        r = requests.get(LINK)
        page_parse = BeautifulSoup(r.text, 'html.parser')

        s_name1 = page_parse.find("ul", {"class":"sbnBtf"}, "li")
        s_name2 = s_name1.find_next("ul", {"class":"sbnBtf"})

        s_changes1 = page_parse.find("ul", {"class":"sbnBtf"}, "li")
        s_changes2 = s_changes1.find_next("ul", {"class":"sbnBtf"})

        s_rate1 = page_parse.find("ul", {"class":"sbnBtf"}, "li")
        s_rate2 = s_rate1.find_next("ul", {"class":"sbnBtf"})

        s_name = s_name1.find_all("div", {"class":"ZvmM7"}) + s_name2.find_all("div", {"class":"ZvmM7"})

        s_rate = s_rate1.find_all("div", {"class":"YMlKec"}) + s_rate2.find_all("div", {"class":"YMlKec"})

        s_changes = s_changes1.find_all("div", {"class":"BAftM"}) + s_changes2.find_all("div", {"class":"BAftM"})

        return s_name, s_rate, s_changes

    def combine_arrays(self):
        name_list_short, rate_list, changes_list = self.request()
        currencies_names = []
        currencies_rate = []
        currencies_changes = []

        for i in range(0, len(name_list_short)):
            currencies_names.append(
                name_list_short[i].text
                )
            currencies_rate.append(
                Decimal(rate_list[i].text)
            )
            currencies_changes.append(
                Decimal(changes_list[i].text)
            )
        return list(zip(currencies_names, currencies_rate, currencies_changes))
