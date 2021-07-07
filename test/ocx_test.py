import sys
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 키움API 객체 생성
        # 키움 증권의 도움말 .. 도움말이 친절하지 않음

        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.dynamicCall("CommConnect()")
        self.ocx.OnEventConnect.connect(self.handle_login)

        self.button_login_info = QPushButton("로그인 정보", self)
        self.button_login_info.move(10, 10)
        self.button_login_info.clicked.connect(self.handel_button_login_info_clicked)

    def handel_button_login_info_clicked(self):
        account_nums = self.ocx.dynamicCall("GetLoginInfo(QString)", "ACCNO")
        # PyQt의 문자열 Type QString, ACCNO라는 문자열을 GetLoginInfo에 넘겨줌
        # account_num 값을 받아옴
        print(account_nums)

    def handle_login(self, err_code):
        if err_code == 0:
            self.statusBar().showMessage("로그인 성공")
        else:
            self.statusBar().showMessage("로그인 실패")


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec()
