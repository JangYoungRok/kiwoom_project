from kiwoom import *
import pickle

class PyMon:
    def __init__(self):
        # 키움클래스의 객체 생성
        self.kiwoom = Kiwoom()
        self.kiwoom.CommConnect()
        self.kiwoom.GetConditionLoad()

    def run(self):
        # 조건식에 해당하는 종목 리스트 얻기
        self.kiwoom.SendCondition('0101', 'perpbr', '000', 0)
        codes = self.kiwoom.condition_codes

        # 파일쓰기 종목 리스트를
        # pickle를 사용해서 file로 저장
        # 피클을 쓰는 이유
        # 파이썬 데이터 타입을 유지 한채 그래도 저장하고 다시 원본 데이터 타입으로 만듦

        f = open('data.db', 'wb')
        pickle.dump(codes, f)
        f.close()


if __name__ == '__main__':
    pymon = PyMon()
    pymon.run()
