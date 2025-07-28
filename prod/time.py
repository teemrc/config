from time import sleep
import os

t = 0

while True:
    t1 = t//60//60 
    t2 = t//60%60
    t3 = t%60
    os.system('cls')
    print(f'{str(t1).zfill(2)}:{str(t2).zfill(2)}:{str(t3).zfill(2)}')
    t+=1
    sleep(1)