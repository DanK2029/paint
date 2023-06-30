from PyQt5.QtWidgets import QWidget, QGraphicsBlurEffect
from PyQt5.QtGui import (
    QPainter,
    QPaintEvent,
    QMouseEvent,
    QResizeEvent,
    QPixmap,
)
from PyQt5.QtCore import (
    QPoint,
    Qt,
)


from tools.pen import Tool


class Canvas(QWidget):

    painter: QPainter
    pixmap: QPixmap
    cur_point: QPoint | None

    tool: Tool = None

    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)

        self.pixmap = QPixmap(self.size())
        self.painter = QPainter(self)
        self.pixmap.fill(Qt.white)

        blur = QGraphicsBlurEffect()
        blur.setBlurRadius(1.1)
        self.setGraphicsEffect(blur)

        self.update()

    def setTool(self, tool: Tool) -> None:
        if self.tool is not None:
            self.tool.onEnd()

        self.tool = tool
        self.tool.onStart(self.pixmap)

    def paintEvent(self, event: QPaintEvent) -> None:
        self.painter.begin(self)
        self.painter.drawPixmap(QPoint(), self.pixmap, self.rect())
        self.painter.end()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.tool.onMousePress(event, self.pixmap)
        self.update()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.tool.onMouseMove(event, self.pixmap)
        self.update()

    def resizeEvent(self, event: QResizeEvent) -> None:
        # TODO: make resize keep previous image
        old_pixmap = self.pixmap.copy(self.pixmap.rect())

        self.pixmap = QPixmap(event.size())
        self.pixmap.fill(Qt.white)

        painter = QPainter(self.pixmap)
        painter.begin(self.pixmap)
        painter.drawPixmap(QPoint(), old_pixmap, old_pixmap.rect())
        painter.end()

        self.update()
