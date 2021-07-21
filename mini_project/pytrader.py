from kiwoom import *
import pickle
import time


class PyTrader:
    def __init__(self):
        self.kiwoom = Kiwoom()
        self.kiwoom.CommConnect()

    # data.db 읽어서
    # 해당 종목 리스트에 있는 종목을 시장가로 매수
    def run(self):
        accounts = self.kiwoom.GetLoginInfo("ACCNO")
        print(accounts)
        # 7000872631;8003008411;
        account = accounts.split(';')[1]

        # 파일 읽기 부분에 예외 처리 필요

        try:
            f = open('data.db', 'rb')
            codes = pickle.load(f)
            f.close()
            print(codes)
            # ['900270', '900300', '000370', '003300', '012320', '012630', '015760', '017940', '082640', '138930',
            # '139130'] 매수
        except:
            codes = []

        for code in codes:
            self.kiwoom.SendOrder('buy_market_order', '0101', account, 1, code, 10, 0, '03', '')
            time.sleep(0.3)


if __name__ == '__main__':
    pytrader = PyTrader()
    pytrader.run()
