from random import randint

print('Угадайте случайное число от 1 до 100 за 10 попыток.')

list = []
cnt = 10

for i in range(10):
    random_num = randint(1, 100)
    if random_num in list:
        continue
    else:
        list.append(random_num)

for i in range(cnt):
    pers_num = int(input('Введите число от 1 до 100: '))
    if pers_num in list:
        print('Bingo')
        break
    else:
        print('Fail')
        cnt -= 1
if cnt == 0:
    print('Game over.')

print(list)
