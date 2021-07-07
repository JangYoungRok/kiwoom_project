import win32com.client
# Component Object Model (com)
# 해당 라이브러리는 윈도우 마이크로 소프트 기반의 프로그램 제어와
# 다른 언어로 만들어진 예를 들어 C++ 같은 언어로 만들어진 객체를
# binary interface 형태로 가져와 다른 언어에서도 쉽게 사용할 수 있는 라이브러리 입니다.
# 키움 API가 C++로 제작 되어 있지만
# COM 라이브러리를 통해서 보다 손쉽게 해당 객체들을 python 환경에서 사용 할 수 있다.
# 다만 해달 라이브러리가 마이크로 소프트 기반이기 때문에 윈도우에서만 사용이 가능하고
# 리눅스나 Apple에서는 사용이 안된다는 단점이 있다.


# ie = win32com.client.Dispatch("InternetExplorer.Application")
# ie.Visible = True

# excel = win32com.client.Dispatch("Excel.Application")
# excel.Visible = True
#
# wb = excel.Workbooks.Add()
# ws = wb.Worksheets("Sheet1")
# ws.Range("A1:A10").Value = "hello"
# ws.Cells(2, 2).Value = 5

