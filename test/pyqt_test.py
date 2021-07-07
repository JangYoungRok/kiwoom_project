import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyupbit
import datetime


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 500)
        self.move(300, 300)
        self.setWindowTitle("PyQt test")
        icon = QIcon("../material/paper_plane.png")
        self.setWindowIcon(icon)

        self.list_widget = QListWidget(self)
        self.list_widget.resize(250, 280)
        self.list_widget.move(150, 10)

        self.btn_add = QPushButton("추가", self)
        self.btn_add.move(440, 10)

        self.btn_clear = QPushButton("초기화", self)
        self.btn_clear.move(440, 60)

        self.btn_add.clicked.connect(self.btn_add_click)
        self.btn_clear.clicked.connect(self.btn_clear_click)

        btn_order = QPushButton("매수", self)
        btn_order.move(10, 10)
        btn_order.clicked.connect(self.btn_order_click)

        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        self.line_edit = QLineEdit(self)
        self.line_edit.move(10, 100)
        self.line_edit.resize(120, 30)

    def timeout(self):
        btc = pyupbit.get_current_price("KRW-BTC")
        self.line_edit.setText(str(btc))

        now = datetime.datetime.now()
        self.statusBar().showMessage(str(now))

    def btn_order_click(self):
        print("order button clicked!!")

    def btn_add_click(self):
        now = datetime.datetime.now()
        self.list_widget.addItem(str(now))

    def btn_clear_click(self):
        self.list_widget.clear()


app = QApplication(sys.argv)
win = MyWindow()
# qApplication 객체에는 파일의 경로를 파라미터로 전달해 줘야 생성이 됨

win.show()

app.exec_()
