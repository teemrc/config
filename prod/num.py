import os

req ='1111111'
l = ['1101111', '0001001', '1011110', '1011011', '0111001', '1110011', '1110111', '1001001', '1111111', '1111011']

def r(s):
    res=''
    for i in range(7):
        ob1 = '__'
        ob2 = '|'
        if s[i]=='0' and i in [0, 2, 5]:
            ob1 = '  '
        if s[i]=='0' and i in [1,4,3,6]:
            ob2 = ' '
        if i ==0:
            res+=' '
        if i in [1, 4]:
            res += ob2
        if i in [0, 2, 5]:
            res += ob1
        if i in [3, 6]:
            res += ob2
        if i in [0, 3]:
            res+='\n'       

    return res

while True:
    num = int(input())
    os.system('clear')
    print(r(l[num]))
