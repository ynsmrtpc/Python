import sys
from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.radio_text = QLabel("Hangi dili daha çok seviyorsun?")
        self.java = QRadioButton("Java")
        self.python = QRadioButton("Python")
        self.php = QRadioButton("PhP")

        self.text_area = QLabel("")
        self.button = QPushButton("Gönder")

        v_box = QVBoxLayout()
        v_box.addWidget(self.radio_text)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addWidget(self.text_area)
        v_box.addStretch()
        v_box.addWidget(self.button)

        self.button.clicked.connect(lambda : self.click(self.java.isChecked(),self.python.isChecked(),self.php.isChecked(),self.text_area))

        self.setLayout(v_box)
        self.setWindowTitle("Radio Button")
        self.show()

    def click(self,java,python,php,text_area):
        if java:
            text_area.setText("Java")
        elif python:
            text_area.setText("Pyhton")
        elif php:
            text_area.setText("PhP")
        else:
            text_area.setText("Lütfen bir seçim yapınız...")

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())