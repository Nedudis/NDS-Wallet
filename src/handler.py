import flet as ft

from user_controls.app_bar import NavBar

from pages.crypto_view import CryptoView
from pages.index_view import IndexView
from pages.settings_view import SettingsView
from pages.main_view import MainPage
from pages.currencies_view import CurrenciesView

def pages_handler(page):
    return {
        '/main_page': ft.View(
            route='/main_page',
            controls=[
                NavBar(page),
                MainPage(page)
            ]
        ),
        '/index_view': ft.View(
            route='/index_view',
            controls=[
                IndexView(page)
            ]
        ),
        '/crypto_view': ft.View(
            route='/crypto_view',
            controls=[
                CryptoView(page).header(),
                CryptoView(page)
            ]
        ),
        '/currencies_view': ft.View(
            route='/currencies_view',
            controls=[
                CurrenciesView(page).header(),
                CurrenciesView(page)
            ]
        ),
        '/settings_view': ft.View(
            route='/settings_view',
            controls=[
                SettingsView(page).header(),
                SettingsView(page)
            ]
        )
    }