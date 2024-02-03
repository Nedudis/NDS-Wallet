import flet as ft
import json

config = {}

with open('././config.json') as cfg:
    config = json.load(cfg)
    cfg.close()
theme = config['theme']
currency = config['currency']

class SettingsView(ft.UserControl):
    
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.theme_dropdown = ft.Dropdown(
            label="Select app's theme",
            width=250,
            options=[
                ft.dropdown.Option(text = "Dark theme", key = "DARK"),
                ft.dropdown.Option(text = "Light theme", key = "LIGHT"),
                ft.dropdown.Option(text = "System's default theme", key = "SYSTEM")
            ],
            on_change=self.change_theme
        )
        self.currency_dropdown = ft.Dropdown(
            label="Select currency",
            options=[
                ft.dropdown.Option(text = "Euro", key = "EUR"),
                ft.dropdown.Option(text = "US Dollar", key = "USD")
            ],
            on_change=self.change_currency
        )

    def change_theme(self, e):
        if self.theme_dropdown.value == 'DARK':
            config['theme_icon'] = "dark_mode_outlined"
            self.page.theme_mode = ft.ThemeMode.DARK
            config['theme'] = 'DARK'
        elif self.theme_dropdown.value == 'LIGHT':
            self.page.theme_mode = ft.ThemeMode.LIGHT
            config['theme_icon'] = "light_mode_outlined"
            config['theme'] = 'LIGHT'
        elif self.theme_dropdown.value == 'SYSTEM':
            self.page.theme_mode = ft.ThemeMode.SYSTEM
            config['theme_icon'] = "auto_mode_outlined"
            config['theme'] = 'SYSTEM'
        self.page.update()
    
    def change_currency(self, e):
        if self.currency_dropdown.value == 'EUR':
            config['currency'] = "EUR"
        elif self.currency_dropdown.value == 'USD':
            config['currency'] = "USD"

    def save_config(self):
        with open('././config.json', "w") as cfg:
            json.dump(config, cfg)
            cfg.close()

    def header(self):
        return ft.AppBar(
                    leading=ft.Icon(ft.icons.SETTINGS),
                    leading_width=40,
                    title=ft.Text("Settings"),
                    actions=[
                        ft.TextButton("Save", on_click=lambda _: self.save_config())
                    ]
                )

    def build(self):
        return ft.Container(
                height=800, width=400,
                content=ft.Column(
                    controls=[
                        ft.ElevatedButton("Go back", on_click=lambda _: self.page.go('/main_page')),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                            self.theme_dropdown,
                                            self.currency_dropdown,
                                            ft.ElevatedButton(
                                                text="Logout",
                                                on_click= lambda _: self.page.go('/logout_view')
                                            )
                                        ])
                                    )
                                ]
                            )
                        )
        


