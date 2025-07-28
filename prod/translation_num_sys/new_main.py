import string as s

def translate_from_10(n, c):
    res = ''
    if c < 10:
        nc = c
    else:
        nc = 10
    while n >= nc:
        if n%c >= 10:
            res += s.ascii_lowercase[(n%c)-10]
        else:
            res += str(n%c)
        n //= c
    res = res[::-1]
    if res != '' and  not res[0] in s.digits and n == 0:
        return res
    else:
        return str(n) + res
num = input('Enter your number: ')
sys1 = int(input('Enter number system from: '))
sys2 = int(input('Enter number system to: '))

if sys1 == 10:
    print(translate_from_10(int(num), sys2))
elif sys2 == 10:
    print(int(num, sys1))
else:
    print(translate_from_10(int(num, sys1), sys2))
