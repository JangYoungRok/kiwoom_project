from kiwoom import *
import time
kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

# ---------------------------------------------
# HTS에서 만든 조건식 리스트 불러오기
# ---------------------------------------------
accounts = kiwoom.GetLoginInfo("ACCNO")
account = accounts.split(';')[1]
print(account)
kiwoom.GetConditionLoad()
condition = kiwoom.GetConditionNameList()
print(condition[1][0])
print(condition[1][1])
kiwoom.SendCondition('0101', condition[1][1], condition[1][0], 0)

balance = 30000000
port = 20
max_price = balance/port

print(kiwoom.condition_codes)

for code in kiwoom.condition_codes:
    print('--------------------------')
    print(code)
    kiwoom.SetInputValue('종목코드', code)
    kiwoom.CommRqData('opt10001', 'opt10001', 0, '0101')
    name = kiwoom.GetMasterCodeName(code)
    print(name)
    current_price = int(kiwoom.tr_data['current_price'][1:])
    print(f'현재가 : {current_price}')
    count = int(max_price // current_price)
    print(f'매수 수량 : {count}')
    kiwoom.SendOrder('매수', "0101", account, 1, code, count, current_price, "00", "")
    print('--------------------------')
    time.sleep(0.3)
