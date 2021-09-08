import time
import schedule


def do_something():
    print("do something~")


schedule.every().day.at('13:00').do(do_something)


while True:
    schedule.run_pending()
    time.sleep(1)
