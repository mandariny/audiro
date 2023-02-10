<<<<<<< HEAD
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QPushButton, QTextEdit, QApplication
import random
app = QApplication([])

t = QTextEdit()

b = QPushButton("Click!!")


def preserve_cursor():
    c = t.textCursor()
    p = c.position()
    a = c.anchor()

    t.setText(

        " ".join("".join(chr(random.randint(ord('a'), ord('z')))
                         for _ in range(6)) for __ in range(1555))
    )
    c.setPosition(a)
    op = QTextCursor.NextCharacter if p > a else QTextCursor.PreviousCharacter
    c.movePosition(op, QTextCursor.KeepAnchor, abs(p - a))
    t.setTextCursor(c)


def preserve_viewport():
    vsb = t.verticalScrollBar()
    old_pos_ratio = vsb.value() / (vsb.maximum() or 1)

    t.setText(

        " ".join("".join(chr(random.randint(ord('a'), ord('z')))
                         for _ in range(6)) for __ in range(1555))
    )

    vsb.setValue(round(old_pos_ratio * vsb.maximum()))


def full_preserve():
    c = t.textCursor()
    p = c.position()
    a = c.anchor()

    vsb = t.verticalScrollBar()
    old_pos_ratio = vsb.value() / (vsb.maximum() or 1)

    t.setText(

        " ".join("".join(chr(random.randint(ord('a'), ord('z')))
                         for _ in range(6)) for __ in range(1555))
    )

    c.setPosition(a)
    op = QTextCursor.NextCharacter if p > a else QTextCursor.PreviousCharacter
    c.movePosition(op, QTextCursor.KeepAnchor, abs(p - a))
    t.setTextCursor(c)

    vsb.setValue(round(old_pos_ratio * vsb.maximum()))


b.clicked.connect(
    #full_preserve
    preserve_viewport
)
t.show()
b.show()
app.exec_()
=======
# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("Python ")

		# setting geometry
		self.setGeometry(100, 100, 500, 400)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()



	# method for components
	def UiComponents(self):

		scroll = QScrollBar(self)

		# setting geometry of the scroll bar
		scroll.setGeometry(100, 50, 30, 200)

		# setting value of scroll bar
		scroll.setValue(25)

		# making its background color to green
		scroll.setStyleSheet("background : lightgrey;")

		# creating a label
		label = QLabel("GeeksforGeeks", self)

		# setting geometry to the label
		label.setGeometry(200, 100, 300, 80)

		# making label multi line
		label.setWordWrap(True)

		# getting value changed signal
		scroll.valueChanged.connect(lambda: do_action())

		# method called when signal is emitted
		def do_action():

			# getting current value
			value = scroll.value()

			# setting text to the label
			label.setText("Current Value : " + str(value))




# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
>>>>>>> 61b658c0f071cbfc472765c06510c3df49d0a268
