from PyQt5.QtWidgets import (
    QWidget,
    QMainWindow,
    QApplication,
    QFileDialog,
    QStyle,
    QColorDialog,
    QAction,
    QToolBar,
    QSizePolicy,

)
from PyQt5.QtCore import (Qt, QSize, QStandardPaths ,pyqtSlot)
from PyQt5.QtGui import (
    QMouseEvent,
    QPaintEvent,
    QPen,
    #QAction,
    QPainter,
    QColor,
    QPixmap,
    QIcon,
    QKeySequence,

)
import sys


class PainterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 사이즈 policy (기본은 expanding이 좋을듯)
        self.setFixedSize(QSize(800, 960))
        #self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) # 위젯 확장시키려고 만든 코드
        #self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored) #기존 코드
        # 내가 ui 파일 뜯어서 보면서 직접 입력했다.... ㅠㅠ

        self.pixmap = QPixmap(self.size())
        self.pixmap.fill(Qt.white)

        self.previous_pos = None
        self.painter = QPainter()
        self.pen = QPen()
        self.pen.setWidth(10)
        self.pen.setCapStyle(Qt.RoundCap)
        self.pen.setJoinStyle(Qt.RoundJoin)

    def paintEvent(self, event: QPaintEvent):
        """Override method from QWidget

        Paint the Pixmap into the widget

        """
        with QPainter(self) as painter:
            painter.drawPixmap(0, 0, self.pixmap)

    def mousePressEvent(self, event: QMouseEvent):
        """Override from QWidget

        Called when user clicks on the mouse

        """
        self.previous_pos = [event.x(),event.y()]
        QWidget.mousePressEvent(self, event)

    def mouseMoveEvent(self, event: QMouseEvent):
        """Override method from QWidget

        Called when user moves and clicks on the mouse

        """
        current_pos = [event.x(),event.y()]
        self.painter.begin(self.pixmap)
        self.painter.setRenderHints(QPainter.Antialiasing, True)
        self.painter.setPen(self.pen)
        self.painter.drawLine(self.previous_pos[0],self.previous_pos[1],current_pos[0],current_pos[1])
        self.painter.end()


        self.previous_pos = current_pos
        self.update()

        QWidget.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        """Override method from QWidget

        Called when user releases the mouse

        """
        self.previous_pos = None
        QWidget.mouseReleaseEvent(self, event)

    def save(self, filename: str):
        """ save pixmap to filename """
        self.pixmap.save(filename)

    # 배경쓸때 아니면 불러올 필요가 없다. 배경이나 편지지,
    def load(self, filename: str):
        """ load pixmap from filename """
        self.pixmap.load(filename)
        self.pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatio)
        self.update()

    def clear(self):
        """ Clear the pixmap """
        self.pixmap.fill(Qt.white)
        self.update()

    def change_color(self,color):
        self.pen.setColor(color)
