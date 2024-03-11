import flet as ft

from collections import deque

from collectors.market_indexes.europe_africa import IndexesEurope

from pages.market_index_views.create_rows import CreateRow

ie_all = IndexesEurope().combine_arrays()


class IndexesEuropeView(ft.UserControl):

    def __init__(self, page):
        super().__init__()
        self.page = page
    
    def header(self):
        return ft.AppBar(
                    leading=ft.Icon(ft.icons.ARROW_UPWARD_ROUNDED),
                    leading_width=40,
                    title=ft.Text("Europe Indexes"),
                    actions=[
                        ft.ElevatedButton("Go back", on_click=lambda _: self.page.go('/main_page'))
                    ]
                )
    
    def build(self):
        return ft.Container(
            content=ft.Column(
                scroll=ft.ScrollMode.ALWAYS,
                controls=[
                    ft.Row(
                        controls = [
                            ft.Column(
                                controls = CreateRow(ie_all, 0).create_rows()
                            ),
                            ft.Column(
                                controls = CreateRow(ie_all, 1).create_rows()
                            ),
                            ft.Column(
                                controls = CreateRow(ie_all).create_rows()
                            )
                        ]
                    )
                ]
            )
        )

    