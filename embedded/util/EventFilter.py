import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QGesture, QGestureEvent, QSwipeGesture, QPanGesture

from PyQt6.QtCore import Qt, QEvent

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 800, 480
        self.setWindowTitle('Event Filter Example')
        self.setStyleSheet('''
            QWidget{
                font-size: 40px;
            }
        ''')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setPlaceholderText('Input 1')
        self.lineEdit1.installEventFilter(self)

        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setPlaceholderText('Input 2')
        self.lineEdit1.installEventFilter(self)

        self.layout.addWidget(self.lineEdit1)
        self.layout.addWidget(self.lineEdit2)

    def eventFilter(self, source, event):
        if source == self.lineEdit1 and event.type() == QEvent.Type.KeyPress:
            print('LineEdit 1 Keypress event')
        return super().eventFilter(source, event)

    def gestureEvent(self, event):
        if event.type() == QPanGesture():
            print('Pan Gesture!')
        return True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')