import flet as ft
import json
import time

config: dict

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
        self.save_dialog = ft.AlertDialog(
            modal = True,
            title = ft.Text("Changes have been saved."),
            content=ft.Text("Some changes might require you to restart the application. Would you like to restart the application now?"),
            actions=[
                ft.TextButton("Yes", on_click= self.YES_save_dialog),
                ft.TextButton("No", on_click= self.NO_save_dialog)
            ]
        )
        self.logout_dialog = ft.AlertDialog(
            modal = True,
            title = ft.Text("Logging out"),
            content=ft.Text("Are you sure you want to logout?"),
            actions=[
                ft.TextButton("Yes", on_click = self.YES_logout_dialog),
                ft.TextButton("No", on_click = self.NO_logout_dialog)
            ]
        )
        self.logged_out_dialog = ft.AlertDialog(
            modal = True,
            title = ft.Text("You have been logged out"),
            actions=[
                ft.TextButton("OK", on_click = self.logged_out_dialog_close)
            ]
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

    def save_config(self, e):
        self.page.dialog = self.save_dialog
        with open('././config.json', "w") as cfg:
            json.dump(config, cfg)
            cfg.close()
        self.save_dialog.open = True
        self.page.update()

    def NO_save_dialog(self, e):
        self.page.dialog = self.save_dialog
        self.save_dialog.open = False
        self.page.update()

    def YES_save_dialog(self, e):
        self.page.dialog = self.save_dialog
        self.save_dialog.open = False
        self.page.update()

    def show_logout_dialog(self, e):
        self.page.dialog = self.logout_dialog
        self.logout_dialog.open = True
        self.page.update()

    def NO_logout_dialog(self, e):
        self.page.dialog = self.logout_dialog
        self.logout_dialog.open = False
        self.page.update()

    def YES_logout_dialog(self, e):
        self.page.dialog = self.logout_dialog
        self.logout_dialog.open = False
        self.page.update()
        time.sleep(0.2)
        self.page.dialog = self.logged_out_dialog
        self.logged_out_dialog.open = True
        self.page.update()

    def logged_out_dialog_close(self, e):
        self.page.dialog = self.logged_out_dialog
        self.logged_out_dialog.open = False
        self.page.update()

    def header(self):
        return ft.AppBar(
                    leading=ft.Icon(ft.icons.SETTINGS),
                    leading_width=40,
                    title=ft.Text("Settings"),
                    actions=[
                        ft.TextButton("Save", on_click=self.save_config)
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
                                                on_click= self.show_logout_dialog
                                            )
                                        ])
                                    )
                                ]
                            )
                        )
        


