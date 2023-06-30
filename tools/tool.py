from PyQt5.QtGui import QMouseEvent, QPixmap, QPainter, QPaintDevice

from abc import ABC, abstractmethod


class Tool(ABC):

    display_name: str
    id_name: str
    painter: QPainter

    @abstractmethod
    def onStart(self, pixmap: QPixmap):
        pass

    @abstractmethod
    def onEnd(self):
        pass

    @abstractmethod
    def onMousePress(self, event: QMouseEvent, pixmap: QPixmap):
        pass

    @abstractmethod
    def onMouseMove(self, event: QMouseEvent, pixmap: QPixmap):
        pass
