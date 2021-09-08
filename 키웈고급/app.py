import sys
import datetime
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ocx = QAxWidget('KHOPENAPI.KHOpenAPICtrl.1')

        self.ocx.OnEventConnect.connect(self.__handler_login)
        self.ocx.OnReceiveTrCondition.connect(self.__handler_tr_condition)

        self.setGeometry(30, 200, 700, 500)
        self.setWindowTitle('키움 프로그램')

        self.plain_text_edit = QPlainTextEdit(self)
        self.plain_text_edit.setReadOnly(True)
        self.plain_text_edit.move(10, 10)
        self.plain_text_edit.resize(280, 280)

        self.get_condition_button = QPushButton('조건식 조회', self)
        self.get_condition_button.move(300, 10)
        self.get_condition_button.resize(100, 30)
        self.get_condition_button.clicked.connect(self.GetConditionNameList)

        self.get_condition_button = QPushButton('종목 조회', self)
        self.get_condition_button.move(300, 50)
        self.get_condition_button.resize(100, 30)
        self.get_condition_button.clicked.connect(self.GetConditionNameList)

        # self.timeVar = QTimer()
        # self.timeVar.setInterval(100)
        # self.timeVar.timeout.connect(self.__do_something)
        # self.timeVar.start()

        self.CommConnect()

    def GetConditionNameList(self):
        data = self.ocx.dynamicCall("GetConditionNameList()")
        print(data)
        conditions = data.split(';')[:-1]
        self.plain_text_edit.appendPlainText('get conditions')
        ret = []
        for condition in conditions:
            index, name = condition.split('^')
            ret.append((index, name))
            self.plain_text_edit.appendPlainText(f'{index} / {name}')

        print(ret[1][0])
        print(ret[1][1])
        self.ocx.dynamicCall("SendCondition(QString, QString, int, int)", "0101", ret[1][1], ret[1][0], 0)



        # self.SendCondition('0101', name, int(index), 0)

    def __handler_tr_condition(self, screen, code_list, condtion_name, condition_index, next):
        print('__handler_tr_condition')
        print(code_list)
        codes = code_list.split(';')
        condition_codes = codes[:-1]
        for code in condition_codes:
            name = self.GetMasterCodeName(code)
            self.plain_text_edit.appendPlainText(f'{code} / {name}')

    def GetMasterCodeName(self, code):
        name = self.ocx.dynamicCall("GetMasterCodeName(QString)", code)
        return name

    def __do_something(self):
        self.statusBar().showMessage(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

    def CommConnect(self):
        self.ocx.dynamicCall('CommConnect()')

    def GetLoginInfo(self, tag):
        data = self.ocx.dynamicCall('GetLoginInfo(QString)', tag)
        return data

    def __handler_login(self, err_code):
        if err_code == 0:
            # print('login success')
            self.plain_text_edit.appendPlainText('login success')
            self.run()

    def run(self):
        account_list = self.GetLoginInfo('ACCNO')
        account = account_list.split(';')[1]
        self.plain_text_edit.appendPlainText(account)

    def GetConditionLoad(self):
        self.ocx.dynamicCall('GetConditionLoad()')

    def SendCondition(self, screen, cond_name, cond_index, search):
        self.plain_text_edit.appendPlainText(f'{screen}/ {cond_name} / {cond_index}')
        self.ocx.dynamicCall("SendCondition(QString, QString, int, int)", screen, cond_name, cond_index, 0)



app = QApplication(sys.argv)
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     wo = MyWindow()
#     wo.show()
#     sys.exit(app.exec())
