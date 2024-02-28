import flet
from flet import *

import json

config = {}
with open('./config.json', "r") as cfg:
    config = json.load(cfg)
    cfg.close()

theme = config['theme']

from handler import pages_handler

class Main(flet.UserControl):

    def __init__(self, page: flet.Page):
        super().__init__()

        page.window_frameless = True

        page.window_height = 800
        page.window_width = 400

        page.vertical_alignment = flet.alignment.center

        page.title = "NDS Wallet"

        if theme == "DARK" : page.theme_mode = flet.ThemeMode.DARK
        elif theme == "LIGHT" : page.theme_mode = flet.ThemeMode.LIGHT
        elif theme == "SYSTEM" : page.theme_mode = flet.ThemeMode.SYSTEM

        def route_change(route):
            page.views.clear()
            page.views.append(
                pages_handler(page)[page.route]
            )
        
        page.on_route_change = route_change

        page.go('/main_page')

if __name__ == "__main__":
    flet.app(target=Main)
