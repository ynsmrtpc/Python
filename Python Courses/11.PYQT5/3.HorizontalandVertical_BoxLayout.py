import sys
from typing import Text
from PyQt5 import QtWidgets

def Window():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("PyQt5 Ders-3")
    window.setGeometry(100,100,500,500)
    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")
    exit_button = QtWidgets.QPushButton("Çıkış")

    # Horizontal Box Layout
    
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)
    h_box.addWidget(exit_button)

    # Vertical Box Layout
    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)
    window.setLayout(v_box)

    exit_button.clicked.connect(click)

    window.show()
    sys.exit(app.exec_())

def click():
    sys.exit()
Window()