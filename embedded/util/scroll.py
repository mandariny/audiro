import sys

from PyQt5.QtWidgets import (
    QApplication,
    QFormLayout,
    QGridLayout,
    QLabel,
    QScrollArea,
    QScroller,
    QWidget,
)

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        scroll_area = QScrollArea()
        layout = QGridLayout(self)
        layout.addWidget(scroll_area)

        scroll_widget = QWidget()
        scroll_layout = QFormLayout(scroll_widget)

        for i in range(100):
            scroll_layout.addRow(QLabel('Label #{}'.format(i)))

        scroll_area.setWidget(scroll_widget)

        QScroller.grabGesture(
            scroll_area.viewport(), QScroller.LeftMouseButtonGesture
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())