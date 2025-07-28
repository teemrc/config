from random import choice

colors = [f'\033[{i}m' for i in range(30, 3)]

while True:
    mes = input()
    nmes = [f'{choice(colors)}{i}\033[0m' for i in mes]
    print(''.join(nmes))