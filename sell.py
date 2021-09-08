from kiwoom import *
import time

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")
"""
	주문일자 = YYYYMMDD (20170101 연도4자리, 월 2자리, 일 2자리 형식)
	SetInputValue("주문일자"	,  "입력값 1");

	계좌번호 = 전문 조회할 보유계좌번호
	SetInputValue("계좌번호"	,  "입력값 2");

	비밀번호 = 사용안함(공백)
	SetInputValue("비밀번호"	,  "입력값 3");

	비밀번호입력매체구분 = 00
	SetInputValue("비밀번호입력매체구분"	,  "입력값 4");

	조회구분 = 1:주문순, 2:역순, 3:미체결, 4:체결내역만
	SetInputValue("조회구분"	,  "입력값 5");

	주식채권구분 = 0:전체, 1:주식, 2:채권
	SetInputValue("주식채권구분"	,  "입력값 6");

	매도수구분 = 0:전체, 1:매도, 2:매수
	SetInputValue("매도수구분"	,  "입력값 7");

	종목코드 = 공백허용 (공백일때 전체종목)
	SetInputValue("종목코드"	,  "입력값 8");
	
	시작주문번호 = 공백허용 (공백일때 전체주문)
	SetInputValue("시작주문번호"	,  "입력값 9");

"""
accounts = kiwoom.GetLoginInfo("ACCNO")
account = accounts.split(';')[1]
password = '0000'

# kiwoom.SetInputValue('주문일자', '20210729')
# kiwoom.SetInputValue('계좌번호', account)
# kiwoom.SetInputValue('비밀번호', '0000')
# kiwoom.SetInputValue('비밀번호입력매체구분', '00')
# kiwoom.SetInputValue('조회구분', '1')
# kiwoom.SetInputValue('주식채권구분', '1')
# kiwoom.SetInputValue('매도수구분', '2')
# kiwoom.SetInputValue('종목코드', '')
# kiwoom.SetInputValue('시작주문번호', '')
#
# kiwoom.CommRqData('OPW00007', 'OPW00007', 0, '0101')
# print(kiwoom.tr_df)

# codes = kiwoom.tr_df['code']
# count = kiwoom.tr_df['count'].astype(int)

# kiwoom.SendOrder('매도', "0101", account, 2, "002430", 10, 0, "03", "")


# for index, d in kiwoom.tr_df.iterrows():
#     print(d['code'][4:])
#     print(int(d['count']))
#     kiwoom.SendOrder('매도', "0101", account, 2, d['code'][4:], int(d['count']), 0, "03", "")
#     kiwoom.SendOrder('매수', "0101", account, 1, "005930", 10, 0, "03", "")

kiwoom.tr_opw00018(account, password)
print('-----------------------------------------')


for index, d in kiwoom.tr_df.iterrows():
    code = d['code']
    count = d['count']
    print('------------------------------------------------')
    print(index)
    print(code)
    print(count)
    kiwoom.SendOrder('매도', "0101", account, 2, code, count, 0, "03", "")
