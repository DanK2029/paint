import os

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

from tools.tool import Tool


class ToolConfig(QWidget):

    tool: Tool | None = None

    tool_name_label: QLabel

    def __init__(self):
        super().__init__()
        self.setObjectName("ToolConfig")
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(open("ui/css/tool_config.css").read())

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        self.tool_name_label = QLabel("No Tool" if self.tool is None else tool.display_name)
        layout.addWidget(self.tool_name_label)
        self.setLayout(layout)

    def setTool(self, tool: Tool):
        self.tool = tool
