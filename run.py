from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

# cnt = kiwoom.GetLoginInfo("ACCOUNT_CNT")
# print(cnt)
#
# account = kiwoom.GetLoginInfo("ACCNO")
# print(account)

codeList = kiwoom.GetCodeListByMarket("0")


stock_list = []
for code in codeList:
    stock = kiwoom.GetMasterCodeName(code)
    stock_list.append(stock)
s_list = []


for stock in stock_list:
    # if stock.find("삼성") > -1:
    #     s_list.append(stock)

    if "삼성" in stock:
        s_list.append(stock)
print(s_list)

print(len(s_list))







