from PyQt5.QtGui import QMouseEvent, QPixmap, QPainter, QPainterPath, QColor, QPaintDevice, QPaintEvent
from PyQt5.QtCore import QPoint, Qt

from tools.tool import Tool


class Pen(Tool):

    display_name = "Pen"
    id_name = "PEN"
    pixmap: QPixmap
    prev_point: QPoint | None

    def onStart(self, pixmap: QPixmap):
        self.prev_point = None
        self.pixmap = pixmap

    def onEnd(self):
        pass

    def onMousePress(self, event: QMouseEvent, pixmap: QPixmap):
        painter = QPainter(pixmap)
        if event.buttons() == Qt.LeftButton:
            painter.drawPoint(event.pos())
        self.prev_point = event.pos()

    def onMouseMove(self, event: QMouseEvent, pixmap: QPixmap):
        if event.buttons() == Qt.LeftButton:
            painter = QPainter(pixmap)

            if self.prev_point is None:
                painter.drawPoint(event.pos())
            else:
                painter.drawLine(self.prev_point, event.pos())

            self.prev_point = event.pos()
