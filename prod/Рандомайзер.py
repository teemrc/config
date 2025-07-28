from random import choice

strint = int(input('Введите число 1 для ввода чисел, 2 для слов: '))
print('Введите ничего для завершения.')

list = []

if strint == 1:
    while (num := input('Введите число: ')) != '':
        list.append(int(num))
        wordd = 'число'

elif strint == 2:
    while (word := input('Введите слово: ')) != '':
        list.append(word)
        wordd = 'слово'

else:
    print('Ошибка.')

list_random = choice(list)
print(f'Ваше {wordd}: {list_random}')
