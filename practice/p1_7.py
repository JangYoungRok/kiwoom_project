from kiwoom import *
import datetime

kiwoom = Kiwoom()
kiwoom.CommConnect()

print("Login Success")

kospi = kiwoom.GetCodeListByMarket("0")
kosdaq = kiwoom.GetCodeListByMarket("10")

code_list = kospi + kosdaq

for code in code_list:
    data = kiwoom.GetMasterListedStockDate(code)
    stock_name = kiwoom.GetMasterCodeName(code)
    # stock_date = datetime.datetime.strptime(data, '%Y%m%d')
    # if stock_date > datetime.datetime(2019, 12, 31):
    #     print(code, stock_name, stock_date.strftime('%Y-%m-%d'))
    stock_state = kiwoom.GetMasterStockState(code).split("|")

    for d in stock_state:
        if d == '거래정지' or d == '관리종목' or d == '투자유의종목':
            print(code, stock_name, stock_state)
