import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.text_box = QtWidgets.QLabel("Bana Henüz Tıklanmadı!")
        self.button = QtWidgets.QPushButton("Bana Tıkla!")
        self.say  = 0

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.button)
        v_box.addWidget(self.text_box)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()


        self.setLayout(h_box)
        self.button.clicked.connect(self.click)
        self.show()
    
    def click(self):
        self.say += 1
        self.text_box.setText("Bana '" + str(self.say) + "' kez tıklandı!") 

app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())