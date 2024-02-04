import flet as ft
from collectors.crypto import CryptoCurrencyPrices
import json

ccp = CryptoCurrencyPrices()
cppc = ccp.combine_arrays()

config = {}
with open('././config.json', "r") as cfg:
    config = json.load(cfg)
    cfg.close()

def create_rows(index = None):
    items = []

    if index == 0:
        for ci in cppc:
            items.append(
                ft.PopupMenuButton(
                    content=(
                        ft.Text(ci[index])
                    ),
                    items=[
                        ft.PopupMenuItem(
                            text = ci[0]
                        ),
                        ft.PopupMenuItem(
                            text = str(ci[3]) + (" €" if config['currency'] == 'EUR' else " $")
                        )
                    ]
                )
            )
    elif index == 2:
        for ci in cppc:
            items.append(
                ft.Text(
                    ci[index],
                    color = ft.colors.GREEN if ci[3] >= 0 else ft.colors.RED
                ),
            )
    else:
        for ci in cppc:
            items.append(ft.Text(value = ("€" if config['currency'] == 'EUR' else "$")))
    return items

class CryptoView(ft.UserControl):

    def __init__(self, page):
        super().__init__()
        self.page = page
    
    def header(self):
        return ft.AppBar(
                    leading=ft.Icon(ft.icons.CURRENCY_BITCOIN_OUTLINED),
                    leading_width=40,
                    title=ft.Text("Crypto prices"),
                    actions=[
                        ft.ElevatedButton("Go back", on_click=lambda _: self.page.go('/main_page'))
                    ]
                )
    
    def build(self):
        return ft.Container(
                height=800, width=400,
                content=ft.Column(
                    scroll=ft.ScrollMode.ALWAYS,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Column(
                                    controls=create_rows(0)),
                                ft.Column(
                                    controls=create_rows(2)),
                                ft.Column(
                                    controls=create_rows())
                            ])
                        ]
                    )
                )