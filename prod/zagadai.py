check = input('Загадайте целое число до 1000 y/n: ')

if check != 'y':
    exit()

bingo = True
end = 1000
start = 0

while 1:
    num = (end-start)//2+start
    next = input(f'Ваше число больше или меньше или равно >/</= {num}: ')
    if next == '=':
       print('BINGO!')
       break
    elif next == '>':
        start = num
    elif next == '<':
        end = num
    else:
        continue

