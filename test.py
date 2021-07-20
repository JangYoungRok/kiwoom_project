# import datetime
#
# t = ['19750101', '19970528', '19880812', '20000101', '19991231', '19821212', '20120912', '20011212']
#
# date = datetime.datetime.strptime(t[0], '%Y%m%d')
# d = datetime.datetime(1999, 12, 31)
# print(date.strftime('%Y-%m-%d'))
#
# for a in t:
#     a = datetime.datetime.strptime(a, '%Y%m%d')
#     print(a, a > d)


l = ['증거금100%', '거래정지', '관리종목']
for d in l:
    if d == ('ㅁ' or '관리종목'):
        print(d)
