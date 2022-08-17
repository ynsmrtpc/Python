import sys 
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text_box = QtWidgets.QLineEdit()
        self.clean = QtWidgets.QPushButton("Temizle")
        self.print = QtWidgets.QPushButton("Yazdir")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.text_box)
        v_box.addWidget(self.clean)
        v_box.addWidget(self.print)
        v_box.addStretch()

        self.setLayout(v_box)

        self.clean.clicked.connect(self.click)
        self.print.clicked.connect(self.click)
        self.show()

    def click(self):
        sender = self.sender()
        if sender.text() == "Temizle":
            self.text_box.clear()
        else:
            print(self.text_box.text())

app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())