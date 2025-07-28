num = int(input('Введите число: '))
numis = int(input('Введите систему счисления числа: '))
numend = int(input('Введите систему счисления в которую надо перевести число: '))

def convert_to(number, base):
    res = ''
    while True:
        ost = number % base
        number = number // base
        res += str(ost)
        if number < base:
            res += str(number)           
            return int(res[::-1])

def i10(num, numis):
    a = int(str(num), numis)
    return a   

if numend == 10:
    print(i10(num, numis))
    

elif numis == 10:
    print(convert_to(num, numend))

else:
    num = (i10(num, numis))
    print(convert_to(num, numend))
