import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *


class Kiwoom:
    def __init__(self):
        self.login_loop = QEventLoop()
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self._handler_login)

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")
        self.login_loop.exec()

    def _handler_login(self):
        self.login_loop.exit()

    def GetLoginInfo(self, tag):
        # tag
        # ACCOUNT_CNT, ACCNO, USER_ID, USER_NAME
        data = self.ocx.dynamicCall("GetLoginInfo(QString)", tag)
        return data


app = QApplication(sys.argv)
