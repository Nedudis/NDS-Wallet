import flet as ft
from collectors.currencies import CurrenciesRate

cer = CurrenciesRate()
cerc = cer.combine_arrays()

def create_rows(index = None):
    items = []

    for ci in cerc:
        items.append(
            ft.Text(value = ci[index])
        )

    return items

class CurrenciesView(ft.UserControl):

    def __init__(self, page):
        super().__init__()
        self.page = page
    
    def header(self):
        return ft.AppBar(
                    leading=ft.Icon(ft.icons.ATTACH_MONEY),
                    leading_width=40,
                    title=ft.Text("Currency rates"),
                    actions=[
                        ft.ElevatedButton("Go back", on_click=lambda _: self.page.go('/main_page'))
                    ]
                )

    def build(self):
        return ft.Container(
                height=800, width=400,
                content=ft.Column(
                    scroll=ft.ScrollMode.ALWAYS,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Column(
                                    controls=create_rows(0)
                                ),
                                ft.Column(
                                    controls=create_rows(1)
                                )
                            ]
                        )
                    ]
                )
            )