import os
from typing import Callable

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QButtonGroup, QPushButton
from PyQt5.QtCore import Qt

from ui.canvas import Canvas
from tools.tool import Tool


class Toolbar(QWidget):

    canvas: Canvas
    tools: dict[str, Tool] = {}
    buttons: dict[str, QPushButton] = {}
    set_tool_funcs: dict[str, Callable[[str], None]] = {}

    def __init__(self, tools: list[Tool], canvas: Canvas):
        QWidget.__init__(self)
        self.setObjectName("Toolbar")
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(open("ui/css/toolbar.css").read())

        self.setFixedHeight(50)

        self.canvas = canvas

        self.setLayout(QHBoxLayout())
        self.layout().setAlignment(Qt.AlignLeft)
        self.layout().setSpacing(2)
        self.layout().setContentsMargins(5, 0, 0, 5)

        for tool in tools:
            self.tools[tool.id_name] = tool
            self.set_tool_funcs[tool.id_name] \
                = lambda state, tool_id=tool.id_name: self.setTool(tool_id)

            tool_button = QPushButton(tool.display_name)
            tool_button.clicked.connect(self.set_tool_funcs[tool.id_name])
            tool_button.setFixedWidth(50)
            tool_button.setFixedHeight(40)

            self.buttons[tool.id_name] = tool_button
            self.layout().addWidget(tool_button)

    def setTool(self, selected_tool_id: str):
        for tool_id in self.buttons:
            self.buttons[tool_id].setStyleSheet("")

        self.buttons[selected_tool_id].setStyleSheet("background-color: rgb(143, 165, 201);")
        self.canvas.setTool(self.tools[selected_tool_id])
