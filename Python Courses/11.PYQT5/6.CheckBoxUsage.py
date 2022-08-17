import sys
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.checkbox = QCheckBox("Python'u seviyor musunuz?")
        self.text_area = QLabel("")
        self.button = QPushButton("Gönder")

        v_box = QVBoxLayout()

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.button)

        self.setLayout(v_box)
        
        self.setWindowTitle("Check Box")

        self.button.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.text_area))
        self.show()

    def click(self,checkbox,text_area):
        if checkbox:
            text_area.setText("Demek Python'ı seviyorsun!")
        else:
            text_area.setText("Neden sevmiyorsun?")

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())