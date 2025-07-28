from random import randint

list = []
cnt = 5
random_num = randint(1, 100)

print('Угадайте число за 5 попыток.')

while cnt != 0:
    pers_num = int(input('Введите число от 1 до 100: '))

    if pers_num > random_num:
        print('Меньше')
        cnt -= 1
    if pers_num < random_num:
        print('Больше')
        cnt -= 1
    if pers_num == random_num:
        print('Bingo')
        break
if cnt == 0:
    print('Game over')
    print(random_num)
