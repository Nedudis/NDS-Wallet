import flet as ft

class MainPage(ft.UserControl):
    
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
                height=800, width=400,
                content=ft.Column(
                    controls=[
                        ft.Text("Welcome, user, to NDS Wallet"),
                        ft.ElevatedButton("Crypto prices", on_click=lambda _: self.page.go('/crypto_view')),
                        ft.ElevatedButton("Currency exchange rates", on_click=lambda _: self.page.go('/currencies_view')),
                        ft.ElevatedButton("Global Market Indexes", on_click = lambda _: self.page.go('/index_view'))
                    ]
                )
            )
        


