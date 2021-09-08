from kiwoom import *
import time

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

# cnt = kiwoom.GetLoginInfo("ACCOUNT_CNT")
# print(cnt)
#
# account = kiwoom.GetLoginInfo("ACCNO")
# print(account)

# codeList = kiwoom.GetCodeListByMarket("0")
#
#
# stock_list = []
# for code in codeList:
#     stock = kiwoom.GetMasterCodeName(code)
#     stock_list.append(stock)
# s_list = []
#
#
# for stock in stock_list:
#     # if stock.find("삼성") > -1:
#     #     s_list.append(stock)
#
#     if "삼성" in stock:
#         s_list.append(stock)
# print(s_list)
#
# print(len(s_list))
#

# -------------------------------------

# data = kiwoom.GetMasterListedStockCnt("005930")
# print(data)
#
# date = kiwoom.GetMasterListedStockDate("005930")
# print(date, type(date))
#
# last_price = kiwoom.GetMasterLastPrice("005930")
# print(last_price, type(last_price))
#
# condition = kiwoom.GetMasterConstruction("005930")
# print(condition, type(condition))
#
# state = kiwoom.GetMasterStockState("005930")
# print(state, type(state))

# ---------------------------------------------

# result = kiwoom.GetThemeGroupList(1)
# pprint.pprint(result)
# theme_names = list(result.keys())
#
# for n in theme_names:
#     if '태양광' in n:
#         print(n, result[n])
# theme_grp = kiwoom.GetThemeGroupList(0)
# print('테마명 : ' + theme_grp['100'])
# data = kiwoom.GetThemeGroupCode('100')
# for code in data:
#     name = kiwoom.GetMasterCodeName(code)
#     print(code, name)

# ---------------------------------------------
# tr opt10001 사용하기
# ---------------------------------------------
# koastudio에서 확인 가능

# kiwoom.SetInputValue('종목코드', '005930')
# kiwoom.CommRqData('opt10001', 'opt10001', 0, '0101')
# 첫번째 인자 : request 인자 ( 값은 무관 하지만 trname이랑 같이 쓰는 것이 편함)
# 두번째 인자 : trname
# 세번째 인자 : 0 번째 만약 받는 데이터가 2차원이면 row 데이터 위치
# 네번째 인자 : screen no 아무거나
# print('main window')
# print(kiwoom.tr_data)

# ---------------------------------------------
# PER PBR 콤보 전략
# ---------------------------------------------
#
# codes = kiwoom.GetCodeListByMarket('0') + kiwoom.GetCodeListByMarket('10')
# per_result = []
# for code in codes[:50]:
#     print(code)
#     kiwoom.SetInputValue('종목코드', code)
#     kiwoom.CommRqData('opt10001', 'opt10001', 0, '0101')
#
#     per = kiwoom.tr_data['PER']
#     per = kiwoom.tr_data['PBR']
#
#     try:
#         per = float(per)
#     except:
#         per = 0
#
#     try:
#         pbr = float(pbr)
#     except:
#         pbr = 0
#
#     if 2.5 <= per <= 10:
#         per_result.append((code, per, pbr))
#
#     time.sleep(0.2)
#
# print(per_result)
#
# per_result_sorted = sorted(per_result, key=lambda x: x[2])
# print(per_result_sorted)
#
# for i in per_result_sorted:
#     print(i[0], i[1], i[2])

# ---------------------------------------------
# 멀테 데이터 opt10081 주식 일봉 데이터
# ---------------------------------------------

# kiwoom.SetInputValue('종목코드', '005930')
# kiwoom.SetInputValue('기준일자', '20200504')
# kiwoom.SetInputValue('수정주가구분', 1)
# kiwoom.CommRqData('opt10081', 'opt10081', 0, '0101')

# ---------------------------------------------
# 멀테 데이터 opt10081 주식 일봉 데이터 연속으로 데이터 받기
# ---------------------------------------------

# 첫번째 조회
# kiwoom.SetInputValue('종목코드', '005930')
# kiwoom.SetInputValue('기준일자', '20210718')
# kiwoom.SetInputValue('수정주가구분', 1)
# kiwoom.CommRqData('opt10081', 'opt10081', 0, '0101')
#
# while kiwoom.remained:
#     kiwoom.SetInputValue('종목코드', '005930')
#     kiwoom.SetInputValue('기준일자', '20200504')
#     kiwoom.SetInputValue('수정주가구분', 1)
#     kiwoom.CommRqData('opt10081', 'opt10081', 2, '0101')
#     time.sleep(3.6)

# ---------------------------------------------
# 연습문제 opt10081 출력값의 주요 데이터를 DataFrame 객체로 저장
# 날짜는 인덱스
# 컬럼은 시가 고가 저가 종가 거래량
# ---------------------------------------------

# kiwoom.SetInputValue('종목코드', '005930')
# kiwoom.SetInputValue('기준일자', '20210718')
# kiwoom.SetInputValue('수정주가구분', 1)
# kiwoom.CommRqData('opt10081', 'opt10081', 0, '0101')
# print(kiwoom.tr_df)
#
# kiwoom.tr_df.to_excel('samsung.xlsx')

# ---------------------------------------------
# 주문 (매수)
# ---------------------------------------------
# 8003-0084


# accounts = kiwoom.GetLoginInfo("ACCNO")
# account = accounts.split(';')[1]
#
# print(f'accounts : {accounts}')
# print(f'account : {account}')
#
# kiwoom.SendOrder('매수', "0101", account, 1, "005930", 10, 0, "03", "")

# ---------------------------------------------
# HTS에서 만든 조건식 불러 오기
# ---------------------------------------------

# kiwoom.GetConditionLoad()


# ---------------------------------------------
# HTS에서 만든 조건식 리스트 불러오기
# ---------------------------------------------
# accounts = kiwoom.GetLoginInfo("ACCNO")
# account = accounts.split(';')[1]
# print(account)
# kiwoom.GetConditionLoad()
# condition = kiwoom.GetConditionNameList()
# print(condition[1][0])
# print(condition[1][1])
# kiwoom.SendCondition('0101', condition[1][1], condition[1][0], 0)
#
# print(kiwoom.condition_codes)

# ---------------------------------------------
# 미체결 리스트 조회
# ---------------------------------------------
# accounts = kiwoom.GetLoginInfo("ACCNO")
# account = accounts.split(';')[1]
# print(account)
#
# kiwoom.tr_opt10075(account)
# print(kiwoom.tr_df)

# kiwoom.SendOrder('매수취소', "0101", account, 3, '335810', 0, 0, "", "0113214")
