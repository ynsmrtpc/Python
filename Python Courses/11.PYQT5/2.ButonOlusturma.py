import sys
from PyQt5 import QtWidgets

def Window():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.setWindowTitle("PtQt5 Ders-2")
    window.setGeometry(100,100,500,500)

    button = QtWidgets.QPushButton(window)
    button.setText("burası bir buton")
    label = QtWidgets.QLabel(window)
    label.setText("hello world!")
    label.move(200,30)
    button.move(200,0)
    window.show()
    sys.exit(app.exec_())

Window()