import flet as ft

from user_controls.app_bar import NavBar

class IndexView(ft.UserControl):
    
    def __init__(self, page):
        super().__init__()
        self.page = page

    def header(self):
        return ft.AppBar(
                    leading=ft.Icon(ft.icons.ARROW_UPWARD_ROUNDED),
                    leading_width=40,
                    title=ft.Text("Market Indexes"),
                    actions=[
                        ft.ElevatedButton("Go back", on_click=lambda _: self.page.go('/main_page'))
                    ]
                )

    def build(self):
        return ft.Container(
                height=760, width=400,
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                ft.Text(f"Global market indexes are here in one place"),
                                ft.ElevatedButton("America's indexes", on_click=lambda _: self.page.go('/index_americas_view')),
                                ft.ElevatedButton("Europe's/Africa's indexes", on_click=lambda _: self.page.go('/index_europe-africa_view')),
                                ft.ElevatedButton("Asia's indexes", on_click=lambda _: self.page.go('/index_asia_pacific_view'))
                            ])
                        )
                    ]
                )
            )