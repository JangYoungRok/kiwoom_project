import app

kiwoom.GetConditionLoad()
condition = kiwoom.GetConditionNameList()
print(condition[1][0])
print(condition[1][1])

kiwoom.SendCondition('0101', condition[1][1], condition[1][0], 0)
print(kiwoom.condition_codes)