from collections import deque
import ctypes
import os
import json

import flet as ft


path = os.getcwd()
cpp_count = ctypes.CDLL(os.path.join(path, "src/collectors/func.so"))
cpp_count.GetPercentage.restype = ctypes.c_double

config: dict
with open('./././config.json', "r") as cfg:
    config = json.load(cfg)
    cfg.close()

class CreateRow():

    def __init__(self, list: deque[tuple], index: int = None):
        super().__init__()
        self.list = list
        self.index = index

    def create_rows(self):
        items: deque = []

        if self.index == 0:
            for i in self.list:
                items.append(
                    ft.PopupMenuButton(
                        tooltip="More information",
                        content=(
                            ft.Text(i[0],
                                    weight=ft.FontWeight.BOLD)
                        ),
                        items=[
                            ft.PopupMenuItem(
                                text = i[0]
                            ),
                            ft.PopupMenuItem(
                                text = "In the past the 24 hours: "
                            ),
                            ft.PopupMenuItem(
                                text = ("+" if i[2] >= 0 else "") + str(i[2])
                                    + (" €" if config['currency'] == 'EUR' else " $")
                            ),
                            ft.PopupMenuItem(
                                text = ("+" if i[2] >= 0 else "") + f"{round(cpp_count.GetPercentage(ctypes.c_double(i[1]), ctypes.c_double(i[2])), 3)} %"
                            )
                        ]
                    )
                )
        if self.index == 1:
            for i in self.list:
                items.append(
                    ft.Text(
                        i[1],
                        color = ft.colors.GREEN if i[2] >= 0 else ft.colors.RED
                    )
                )
        if self.index == None:
            for i in self.list:
                items.append(ft.Text(value = ("€" if config['currency'] == 'EUR' else "$")))
        return items