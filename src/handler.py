import flet as ft

from user_controls.app_bar import NavBar

from pages.crypto_view import CryptoView
from pages.index_view import IndexView
from pages.settings_view import SettingsView
from pages.main_view import MainPage
from pages.currencies_view import CurrenciesView
from pages.market_index_views.europe_africa_view import IndexesEuropeView
from pages.market_index_views.america_view import IndexesAmericaView
from pages.market_index_views.asia_view import IndexesAsiaView

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
                IndexView(page).header(),
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
        ),
        # Index routes
        '/index_europe-africa_view': ft.View(
            route='/index_europe-africa_view',
            controls=[
                IndexesEuropeView(page).header(),
                IndexesEuropeView(page)
            ]
        ),
        '/index_americas_view': ft.View(
            route='/index_americas_view',
            controls=[
                IndexesAmericaView(page).header(),
                IndexesAmericaView(page)
            ]
        ),
        '/index_asia_pacific_view': ft.View(
            route='/index_asia_pacific_view',
            controls=[
                IndexesAsiaView(page).header(),
                IndexesAsiaView(page)
            ]
        )
    }