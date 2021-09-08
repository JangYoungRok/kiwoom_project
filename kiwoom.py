import sys
import datetime
from pandas import DataFrame

from typing import Dict, Any, List, Tuple

from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *


class Kiwoom:
    condition_codes: object
    tr_df: DataFrame
    data_list: List[Tuple[Any, Any, Any, Any, Any, Any]]
    remained: bool  # tr 연속 조회시 남아 있는 데이터가 있는지 체크하는 변수

    def __init__(self):
        self.tr_data = {}
        self.condition_tr_loop = QEventLoop()
        self.condition_load_loop = QEventLoop()
        self.order_loop = QEventLoop()
        self.tr_loop = QEventLoop()
        self.login_loop = QEventLoop()
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self._handler_login)
        self.ocx.OnReceiveTrData.connect(self._handler_tr)
        # orderEvent
        self.ocx.OnReceiveChejanData.connect(self._handler_chejan)
        self.ocx.OnReceiveMsg.connect(self._handler_msg)
        self.ocx.OnReceiveConditionVer.connect(self._handler_condition_load)
        self.ocx.OnReceiveTrCondition.connect(self._handler_tr_condition)

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")
        self.login_loop.exec()

    def _handler_tr_condition(self, screen, codelist, cond_name, cond_index, next):
        codes = codelist.split(';')
        self.condition_codes = codes[:-1]
        self.condition_tr_loop.exit()

    def _handler_condition_load(self, ret, msg):
        print(f'OnReceiceConditionVer : {ret} // {msg}')
        self.condition_load_loop.exit()

    def _handler_chejan(self, gubun, item_cnt, fid_list):
        print("OnReceiceChejanData : ", gubun, item_cnt, fid_list)

    def _handler_msg(self, screen, rqname, trcode, msg):
        print("OnReceiceMsg", screen, rqname, trcode, msg)

    def _handler_login(self):
        self.login_loop.exit()

    def _handler_tr(self, screen, rqname, trcode, record, prev_next):
        if prev_next == '2':
            self.remained = True
        else:
            self.remained = False

        if rqname == 'opt10001':
            print('opt10001')
            per = self.GetCommData(trcode, rqname, 0, 'PER')
            pbr = self.GetCommData(trcode, rqname, 0, 'PBR')
            current_price = self.GetCommData(trcode, rqname, 0, '현재가')

            print(f'per : {per}')
            print(f'pbr : {pbr}')
            print(f'current_price : {current_price}')

            self.tr_data['PER'] = per
            self.tr_data['PBR'] = pbr
            self.tr_data['current_price'] = current_price

            print(self.tr_data)

        elif rqname == 'opt10081':
            print(rqname)
            self._opt10081(rqname, trcode)

        elif rqname == 'OPW00007':
            print(rqname)
            rows = self.GetRepeatCnt(trcode, rqname)
            self.data_list = []
            for i in range(rows):
                count = self.GetCommData(trcode, rqname, i, "체결수량")
                price = self.GetCommData(trcode, rqname, i, "체결단가")
                code = self.GetCommData(trcode, rqname, i, "종목번호")
                name = self.GetCommData(trcode, rqname, i, "종목명")

                self.data_list.append((count, price, code, name))

            self.tr_df = DataFrame(data=self.data_list, columns=['count', 'price', 'code', 'name'])

        elif rqname == '계좌평가잔고내역요청':
            print(f'rqname : {rqname}')
            print(f'trcode : {trcode}')

            rows = self.GetRepeatCnt(trcode, rqname)
            print(f'rows : {rows}')
            self.data_list = []
            for i in range(rows):
                count = int(self.GetCommData(rqname, trcode, i, "보유수량"))
                price = int(self.GetCommData(rqname, trcode, i, "현재가"))
                code = self.GetCommData(rqname, trcode, i, "종목번호")[1:]
                name = self.GetCommData(rqname, trcode, i, "종목명")

                print(f'count : {count}')
                print(f'price : {price}')
                print(f'code : {code}')
                print(f'name : {name}')

                self.data_list.append((count, price, code, name))

            self.tr_df = DataFrame(data=self.data_list, columns=['count', 'price', 'code', 'name'])

        elif trcode == 'opt10075':
            print(f'rqname : {rqname}')
            print(f'trcode : {trcode}')

            rows = self.GetRepeatCnt(trcode, rqname)
            print(f'rows : {rows}')
            self.data_list = []
            for i in range(rows):
                order_number = self.GetCommData(rqname, trcode, i, "주문번호")
                name = self.GetCommData(rqname, trcode, i, "종목명")
                code = self.GetCommData(rqname, trcode, i, "종목코드")
                order_qty = self.GetCommData(rqname, trcode, i, "주문수량")
                unsigned_qty = self.GetCommData(rqname, trcode, i, "미체결수량")

                self.data_list.append((order_number, name, code, order_qty, unsigned_qty))

            self.tr_df = DataFrame(data=self.data_list,
                                   columns=['order_number', 'name', 'code', 'order_qty', 'unsigned_qty'])

        try:
            self.tr_loop.exit()
        except:
            print('error')

    def GetLoginInfo(self, tag):
        # tag
        # ACCOUNT_CNT, ACCNO, USER_ID, USER_NAME
        data = self.ocx.dynamicCall("GetLoginInfo(QString)", tag)
        return data

    def GetCodeListByMarket(self, market):
        data = self.ocx.dynamicCall("GetCodeListByMarket(QString)", market)
        codes = data.split(";")
        return codes[:-1]

    def GetMasterCodeName(self, code):
        data = self.ocx.dynamicCall("GetMasterCodeName(QString)", code)
        return data

    def GetMasterListedStockCnt(self, code):
        data = self.ocx.dynamicCall("GetMasterListedStockCnt(QString)", code)
        return data

    def GetMasterListedStockDate(self, code):
        data = self.ocx.dynamicCall("GetMasterListedStockDate(QString)", code)
        return data

    def GetMasterLastPrice(self, code):
        data = self.ocx.dynamicCall("GetMasterLastPrice(QString)", code)
        return int(data)

    def GetMasterConstruction(self, code):
        data = self.ocx.dynamicCall("GetMasterConstruction(QString)", code)
        return data

    def GetMasterStockState(self, code):
        data = self.ocx.dynamicCall("GetMasterStockState(QString)", code)
        return data

    def GetThemeGroupList(self, type_name):
        data = self.ocx.dynamicCall("GetThemeGroupList(int)", type_name)
        token = data.split(";")
        data_dic = {}
        for t in token:
            code, name = t.split("|")
            if type == 0:
                data_dic[code] = name
            else:
                data_dic[name] = code

        return data_dic

    def GetThemeGroupCode(self, theme_code):
        data = self.ocx.dynamicCall("GetThemeGroupCode(QStirng)", theme_code)
        tokens = data.split(';')
        result = []
        for code in tokens:
            result.append(code[1:])
        return result

    def SetInputValue(self, item, value):
        self.ocx.dynamicCall("SetInputValue(QString, QString)", item, value)

    def CommRqData(self, rqname, trcode, prev_next, screen):
        self.ocx.dynamicCall("CommRqData(QString, QString, int, QString)", rqname, trcode, prev_next, screen)
        self.tr_loop.exec()

    def GetCommData(self, trcode, rqname, index, item):
        data = self.ocx.dynamicCall("GetCommData(QString, QString, int, QString)", rqname, trcode, index, item)
        return data.strip()

    def GetRepeatCnt(self, trcode, rqname):
        cnt = self.ocx.dynamicCall("GetRepeatCnt(QString, QString)", trcode, rqname)
        return cnt

    def _opt10081(self, rqname, trcode):
        rows = self.GetRepeatCnt(trcode, rqname)
        self.data_list = []
        for i in range(rows):
            date = self.GetCommData(trcode, rqname, i, "일자")
            open_price = self.GetCommData(trcode, rqname, i, "시가")
            high = self.GetCommData(trcode, rqname, i, "고가")
            low = self.GetCommData(trcode, rqname, i, "저가")
            close = self.GetCommData(trcode, rqname, i, "현재가")
            volume = self.GetCommData(trcode, rqname, i, "거래량")
            stock_date = datetime.datetime.strptime(date, '%Y%m%d')
            self.data_list.append((stock_date, open_price, high, low, close, volume))

        self.tr_df = DataFrame(data=self.data_list, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
        self.tr_df = self.tr_df.set_index('date')

    def SendOrder(self, rqname, screen, accno, order_type, code, quantity, price, hoga, order_no):
        # 주문 넣기
        # 매수 매도
        # 중요한건 시장가로 주문을 넣는가? 지정가로 넣는가?
        # 지정가로
        self.ocx.dynamicCall("SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)",
                             [rqname, screen, accno, order_type, code, quantity, price, hoga, order_no])

        # self.order_loop.exec()

    def GetConditionLoad(self):
        # 조건 검색식 읽기
        self.ocx.dynamicCall('GetConditionLoad()')
        self.condition_load_loop.exec()

    def GetConditionNameList(self):
        # 조건식의 목록을 받아옴
        # 리턴형태
        # 문자열
        # 인덱스^조건명^;인덱스^조건명;...
        # 마지막은 공백이라 마지막 제거하는 슬라이싱 필요
        data = self.ocx.dynamicCall('GetConditionNameList()')
        conditions = data.split(';')[:-1]

        ret = []
        for condition in conditions:
            index, name = condition.split('^')
            ret.append((index, name))

        return ret

    def SendCondition(self, screen, cond_name, cond_index, search):
        self.ocx.dynamicCall("SendCondition(QString, QString, int, int)", screen, cond_name, cond_index, search)
        self.condition_tr_loop.exec()

    # 계좌평가잔고내역요청
    def tr_opw00018(self, account, password):
        self.SetInputValue('계좌번호', account)
        self.SetInputValue('비밀번호', password)
        self.SetInputValue('비밀번호입력매체구분', '00')
        self.SetInputValue('조회구분', '2')
        self.CommRqData('계좌평가잔고내역요청', 'opw00018', 0, '0101')

    # 미체결요청
    def tr_opt10075(self, account):
        self.SetInputValue('계좌번호', account)
        self.SetInputValue('전체종목구분', '0')
        self.SetInputValue('매매구분', '2')
        self.SetInputValue('종목코드', '')
        self.SetInputValue('체결구분', '1')
        self.CommRqData('미체결요청', 'opt10075', 0, '0101')

    # 계좌주문체결내역상세요청
    def tr_opw00007(self, ):
        ...


app = QApplication(sys.argv)
