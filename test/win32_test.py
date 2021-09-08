import win32gui
import win32con
import win32api

# hwnd = win32gui.FindWindow(None, "계산기")
# print(hwnd)
#
# win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

# hwnd = win32gui.FindWindow(None, "*제목 없음 - Windows 메모장")
# print(hwnd)
# for i in range(10):
#     edit = win32gui.GetDlgItem(hwnd, 0xF)
#     win32api.SendMessage(edit, win32con.WM_CHAR, ord('H'), 0)
#     win32api.Sleep(1000)
#     win32api.SendMessage(edit, win32con.WM_CHAR, ord('I'), 0)
#     win32api.Sleep(1000)
# 메모장의 핸들을 가져와서
# 메모장의 내부 위젯을 가져와서 컨트롤 함

# 자동 로그인

