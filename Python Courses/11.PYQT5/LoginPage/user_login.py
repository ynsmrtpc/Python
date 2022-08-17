import sys
from PyQt5 import QtWidgets
import sqlite3

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.create_connect()
        self.init_ui()
    
    def create_connect(self):
        connector = sqlite3.connect("11.PYQT5/LoginPage/database.db")
        self.cursor = connector.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS uyeler (username TEXT, password TEXT)")

        connector.commit()


    def init_ui(self):
        self.username = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login = QtWidgets.QPushButton("Login")
        self.text_box = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.username)
        v_box.addWidget(self.password)
        v_box.addWidget(self.text_box)
        v_box.addStretch()
        v_box.addWidget(self.login)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        
        self.setLayout(h_box)
        self.setWindowTitle("Login")
        self.login.clicked.connect(self.logined_up)

        self.show()

    def logined_up(self):
        name = self.username.text()
        psw = self.password.text()

        self.cursor.execute("SELECT *FROM uyeler WHERE username = ? and password = ?",(name,psw))
        data = self.cursor.fetchall()
        
        if len(data) == 0:
            self.text_box.setText("Kullanıcı bulunamadı!")
        else:
            self.text_box.setText("Hoşgeldiniz " + name)
app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())