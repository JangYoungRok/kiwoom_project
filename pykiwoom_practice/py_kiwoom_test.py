from pykiwoom.kiwoom import *
import pprint

# kiwoom = Kiwoom()
# kiwoom.CommConnect(block=True)
# blocking login = 해당 로그인이 완료 될때까지 코드가 넘어가지 않음
# print('블록킹 로그인 완료')

# 로그인 정보 받아오기
# account_num = kiwoom.GetLoginInfo("ACCOUNT_CNT")
# accounts = kiwoom.GetLoginInfo("ACCNO")
# user_id = kiwoom.GetLoginInfo("USER_ID")
# user_name = kiwoom.GetLoginInfo("USER_NAME")
# keyboard = kiwoom.GetLoginInfo("KEY_BSECGB")
# firewall = kiwoom.GetLoginInfo("FIREW_SECGB")
#
# print(account_num)
# print(accounts)
# print(user_id)
# print(user_name)
# print(keyboard)
# print(firewall)

# 연결상태 확익
# state = kiwoom.GetConnectState()
#
# if state == 0:
#     print('미 연결')
# elif state == 1:
#     print('연결 완료')
# else:
#     print('unknown')

# 마켓 종목코드 가져오기
# kospi = kiwoom.GetCodeListByMarket('0')
# kosdaq = kiwoom.GetCodeListByMarket('10')
# etf = kiwoom.GetCodeListByMarket('8')

# print(f'kospi // {kospi}')

# 종목명 받아오기
# kospi_name = []
# for code in kospi:
#     name = kiwoom.GetMasterCodeName(code)
#     kospi_name.append(name)
#
# print(kospi_name)

# 종목별 전일종가
# return type 정수

# last_day_price = kiwoom.GetMasterLastPrice('005930')
# print(last_day_price)

# 테마명 얻기
# type = 0 : {'100' : '태양광_폴리실리콘'}
# type =1 : {'태양광_폴리실리콘 : '100'}
#
# theme_group = kiwoom.GetThemeGroupList(type=1)
# pprint.pprint(theme_group)

# for code in theme_group.values():
#     print(code)

# theme_id = theme_group['타이어']
# print(theme_id)

# 테마명 얻기
# tickers = kiwoom.GetThemeGroupCode(theme_id)
#
# for code in tickers:
#     name = kiwoom.GetMasterCodeName(code)
#     print(code, name)

# HTS의 조건식 가져오기
# kiwoom.GetConditionLoad()
# print('blocking load')
# conditions = kiwoom.GetConditionNameList()
# print(conditions)
#
# condition = conditions[0]
# condition_index, condition_name = condition
# 튜플 언팩킹

# 조건식에 해당하는 종목가져오기
# codes = kiwoom.SendCondition('0101', condition_name, condition_index, 0)
# 0 은 일반조회
# print(codes)
#
# for code in codes:
#     name = kiwoom.GetMasterCodeName(code)
#     print(code, name)


# --------------------------------
# 중급 1-4 pykiwoom TR 사용 기초편
# kiwooom 객체 생성시 login=True 로 생성 하면 로그인도 같이
# block_request 함수에 opt값, 그리고 그 opt에 해당하는 인자를 주면
# block 방식 해당 코드다 실행되어서 콜백까지 끝나서 결과값을 받을때 까지 기다렸다가
# 값이 오면 다음 코드 처리하는 방식으로 동작함
# ---------------------------------

# kiwoom = Kiwoom(login=True)  # 객체생성 및 로그인
# df = kiwoom.block_request('opt10001', 종목코드='005930', output='주식기본정보', next=0)
# print(df)

# df.to_excel('samsung.xlsx')


# -------------------------------------
# 중급 1-4 TR 응용편
# -------------------------------------

# kiwoom = Kiwoom(login=True)
# df = kiwoom.block_request("opt10081", 종목코드="005930", 기준일자="20210727", 수정주가구분=1, output="주식일봉차트조회", next=0)
# opt10081 주실 일봉 차트 조회 해ㅈ당 종목의 기준일자 이전의 일봉 데이터를 받아옮
# next = 0을 넣으면 최근의 600개
# print(df.head())
# print(len(df))
# i = 0
# while kiwoom.tr_remained:
#     ++i
#     print(f"{i}번째 실행")
#     df = kiwoom.block_request("opt10081", 종목코드="005930", 기준일자="20210727", 수정주가구분=1, output="주식일봉차트조회", next=2)
#     time.sleep(3.6)
#
# print(len(df))

# ---------------------------------------
# 중급 pykiwoom 매수
# ---------------------------------------

# kiwoom = Kiwoom()
# kiwoom.CommConnect()
#
# accounts = kiwoom.GetLoginInfo("ACCNO")
# stock_account = accounts[1]
#
# kiwoom.SendOrder("시장가매수", "0101", stock_account, 2, "005930", 10, 0, "03", "")
# 시장가매수 라는 이름으로
# 0101 화면에
# stock_account 계좌로 거래하는데
# 005930이라는 종목을
# 10주
# 0원에 *시장가로 주문시 0원으로 입력
# 03 시장가로 주문
# "" 매수취소나 매수정정이 아니니 때문에 원주문 번호는 빈 문자열

# ---------------------------------------
# 중급 예수금 조회
# ---------------------------------------

# kiwoom = Kiwoom(login=True)
# account_list = kiwoom.GetLoginInfo("ACCNO")
# account = account_list[1]
#
# df = kiwoom.block_request("opw00001", 계좌번호=account, 비밀번호="", 비밀번호입력매체구분="00", 조회구분=1, output="예수금상세현황", next=0)
# print(df)
# print(int(df['주문가능금액'][0]))
# df.to_excel("예수금현황.xlsx")

# ---------------------------------------
# 모멘텀 전략 구현
# 전 종목 일봉 데이터
# ---------------------------------------

# import datetime
# import time
#
# kiwoom = Kiwoom()
# kiwoom.CommConnect()
#
# kospi = kiwoom.GetCodeListByMarket('0')
# kosdaq = kiwoom.GetCodeListByMarket('10')
# codes = kospi + kosdaq
#
# today = datetime.datetime.now().strftime('%Y%m%d')
#
# for i, code in enumerate(codes):
#     print(f'{i}/{len(codes)} {code}')
#
#     df = kiwoom.block_request('opt10081', 종목코드=code, 기준일자=today, 수정주가구분=1, output='주식일보차트조회', next=0)
#     out_name = f'{code}.xlsx'
#     df.to_excel('./save/' + out_name)
#     time.sleep(3.6)


# ---------------------------------------
# 모멘텀 전략 구현
# 전 종목 일봉 데이터를 하나의 엑셀로 합치기
# ---------------------------------------
import pandas as pd
import os

# file_list = os.listdir('./save')
# # print(file_list)
# xlsx_list = [x for x in file_list if x.endswith('.xlsx')]
# # list comprehension
# close_data = []
# for xls in xlsx_list:
#     print(xls)
#     code = xls[:6]
#     df = pd.read_excel('./save/'+xls)
#     df_copy = df[['현재가', '일자']].copy()
#     df_copy.rename(columns={'현재가': code}, inplace=True)
#     df_copy = df_copy.set_index('일자')
#     df_copy = df_copy[::-1]  # 역순으로 뒤집기
#
#     close_data.append(df_copy)
#
# close_df = pd.concat(close_data, axis=1)
# close_df.to_excel('./save/merge.xlsx')

# df = pd.read_excel('./save/000020.xlsx')
# df_copy = df[['현재가', '일자']].copy()
# print(df_copy)
#
# # 컬럼이름 변경
# df_copy.rename(columns={'현재가': '000020'}, inplace=True)
# df_copy = df_copy.set_index('일자')
# df_copy = df_copy[::-1] # 역순으로 뒤집기
# print(df_copy)

# ---------------------------------------
# 모멘텀 전략 구현
# jupyter notebook 으로 구현된
# ---------------------------------------


import pandas as pd
import time

df = pd.read_excel('momentum_df.xlsx', dtype={"종목코드": str, "모멘텀": float, "순위": int})
# print(df)
# df.columns = ['종목코드', '모멘텀', '순위']

kiwoom = Kiwoom(login=True)
codes = df['종목코드']
# print(codes)
names = []
for code in codes:
    name = kiwoom.GetMasterCodeName(code)
    names.append(name)

df['종목명'] = pd.Series(data=names)
# print(df)

# 매수코드
accounts = kiwoom.GetLoginInfo("ACCNO")
account = accounts[1]

for code in codes:
    kiwoom.SendOrder('시장가매수', '0101', account, 1, code, 10, 0, '03', '')
    time.sleep(0.3)
    print(f'{code} 종목 시장가 주문 완료')



