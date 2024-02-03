import flet as ft

def NavBar(page):

    NavBar = ft.AppBar(
            leading=ft.Icon(ft.icons.WALLET),
            leading_width=40,
            title=ft.Text("NDS Wallet"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.HOME, on_click = lambda _: page.go('/index_view')),
                ft.IconButton(ft.icons.ATTACH_MONEY, on_click = lambda _: page.go('/currencies_view')),
                ft.IconButton(ft.icons.CURRENCY_BITCOIN_OUTLINED, on_click = lambda _: page.go('/crypto_view')),
                ft.IconButton(ft.icons.SETTINGS, on_click = lambda _: page.go('/settings_view'))
            ]
        )

    return NavBar