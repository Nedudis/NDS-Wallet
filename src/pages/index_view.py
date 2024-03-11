import flet as ft

from user_controls.app_bar import NavBar

class IndexView(ft.UserControl):
    
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
                height=760, width=400,
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                ft.Text(f"Welcome, user"),
                                ft.ElevatedButton("Go back", on_click=lambda _: self.page.go('/main_page')),
                                ft.ElevatedButton("Go to crypto", on_click=lambda _: self.page.go('/crypto_view'))
                            ])
                        )
                    ]
                )
            )