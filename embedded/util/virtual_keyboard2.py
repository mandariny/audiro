import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5 import QtCore, QtGui, QtWidgets


def handleVisibleChanged():
    if not QtGui.QGuiApplication.inputMethod().isVisible():
        return
    for w in QtGui.QGuiApplication.allWindows():
        if w.metaObject().className() == "QtVirtualKeyboard::InputView":
            keyboard = w.findChild(QtCore.QObject, "keyboard")
            if keyboard is not None:
                region = w.mask()
                rect = [w.geometry()]
                rect[0].moveTop(keyboard.property("y"))
                region.setRects(rect)
                w.setMask(region)
                return


def main():
    os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
    app = QtWidgets.QApplication(sys.argv)

    QtGui.QGuiApplication.inputMethod().visibleChanged.connect(handleVisibleChanged)

    w = QtWidgets.QLineEdit()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()