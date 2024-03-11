import flet as ft

from collections import deque

from collectors.market_indexes.indexes import Indexes

from pages.market_index_views.create_rows import CreateRow

ie_all = Indexes(1).combine_arrays()


class IndexesAsiaView(ft.UserControl):

    def __init__(self, page):
        super().__init__()
        self.page = page
    
    def header(self):
        return ft.AppBar(
                    leading=ft.Icon(ft.icons.ARROW_UPWARD_ROUNDED),
                    leading_width=40,
                    title=ft.Text("Asia's Indexes"),
                    actions=[
                        ft.ElevatedButton("Go back", on_click=lambda _: self.page.go('/index_view'))
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