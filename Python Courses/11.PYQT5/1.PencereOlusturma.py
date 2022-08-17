import sys
from PyQt5 import QtWidgets,QtGui

def Window():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("PyQt Ders-1")
    label1 = QtWidgets.QLabel(window)
    label1.setText("Hello World!")
    label1.move(200,30)
    label2 = QtWidgets.QLabel(window)
    label2.setPixmap(QtGui.QPixmap("png/wp.png"))
    window.setGeometry(100,100,500,500) # ilk iki değer nereden başlayacağını, son iki değer boyutunu belirler
    label2.move(180,50)
    window.show()
    sys.exit(app.exec_())

Window()