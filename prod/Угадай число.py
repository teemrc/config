from random import randrange

print('Угадайте случайное число от 1 до 10 за 7 попыток.')

def rand():
    list = []
    cnt = 7

    random_num = randrange(1, 10)

    list.append(random_num)

    for i in range(cnt):
        pers_num = int(input('Введите число от 1 до 10: '))

        if pers_num in list:
            return 'Bingo'
            
        else:
            cnt -= 1
            print('Fail')

    if cnt == 0:
        return 'Game over.'

print(rand())
