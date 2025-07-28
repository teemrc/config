from random import randint

min_num = int(input('Введите минимальное число: '))
max_num = int(input('Введите максимальное число: '))

random_num = randint(min_num, max_num)

print('Ваше число :', random_num)
