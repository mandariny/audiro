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