from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLayout, QBoxLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from sys import argv
from dataclasses import dataclass

# Widgets
from ui.canvas import Canvas
from ui.toolbar import Toolbar
from ui.tool_config import ToolConfig

# Tools
from tools.pen import Pen
from tools.brush import Brush


@dataclass()
class Config:
    window_title: str
    default_size: [int, int]
    default_tool_id: str


class MainWindow(QWidget):

    app: QApplication
    canvas: Canvas

    def __init__(self, config: Config):
        self.app = QApplication(argv)
        QWidget.__init__(self)

        self.setLayout(QHBoxLayout())

        self.setup_window(
            width=config.default_size[0],
            height=config.default_size[1],
            window_title=config.window_title,
            layout=self.layout(),
        )

        canvas_toolbar_layout = QVBoxLayout()
        self.setup_canvas(canvas_toolbar_layout)
        self.setup_toolbar(config.default_tool_id, canvas_toolbar_layout)
        self.layout().addLayout(canvas_toolbar_layout)

        self.setup_tool_config(self.layout())

        self.show()

    def setup_window(self, width: int, height: int, window_title: str, layout: QLayout):
        self.setMouseTracking(True)
        self.setWindowTitle(window_title)
        self.setGeometry(0, 0, width, height)
        self.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)

    def setup_tool_config(self, layout: QLayout):
        tool_config = ToolConfig()
        tool_config.setBaseSize(100, tool_config.size().height())
        layout.addWidget(tool_config)

    def setup_canvas(self, layout: QLayout):
        self.canvas = Canvas()
        self.canvas.setTool(Brush())
        layout.addWidget(self.canvas)

    def setup_toolbar(self, default_tool_id: str, layout: QLayout):
        toolbar = Toolbar([Pen(), Brush()], self.canvas)
        toolbar.setTool(default_tool_id)
        layout.addWidget(toolbar)

    def add_widget(self, widget: QWidget):
        self.layout().addWidget(widget)

    def run(self):
        self.app.exec()
