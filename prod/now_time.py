import time, os

while True:
    t = time.localtime()
    tt = time.strftime("%H:%M:%S", t)
    os.system('clear')
    print(tt)
    time.sleep(0.01)
