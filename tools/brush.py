from PyQt5.QtGui import QMouseEvent, QPixmap, QPainter, QPaintDevice, QBrush, QPen, QColor
from PyQt5.QtCore import QPoint, Qt

from tools.tool import Tool


class Brush(Tool):

    display_name = "Brush"
    id_name = "BRUSH"

    pixmap: QPixmap
    prev_point: QPoint | None
    pen: QPen

    def onStart(self, pixmap: QPixmap):
        self.prev_point = None
        self.pixmap = pixmap
        self.pen = QPen()
        self.pen.setWidth(15)
        self.pen.setColor(QColor(32, 156, 5))
        self.pen.setCapStyle(Qt.RoundCap)
        self.pen.setJoinStyle(Qt.BevelJoin)

    def onEnd(self):
        pass

    def onMousePress(self, event: QMouseEvent, pixmap: QPixmap):
        painter = QPainter(pixmap)
        painter.setPen(self.pen)
        if event.buttons() == Qt.LeftButton:
            painter.drawPoint(event.pos())
        self.prev_point = event.pos()

    def onMouseMove(self, event: QMouseEvent, pixmap: QPixmap):
        if event.buttons() == Qt.LeftButton:
            painter = QPainter(pixmap)
            painter.setPen(self.pen)

            if self.prev_point is None:
                painter.drawPoint(event.pos())
            else:
                painter.drawLine(self.prev_point, event.pos())

            self.prev_point = event.pos()

