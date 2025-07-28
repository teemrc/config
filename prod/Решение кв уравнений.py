a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

B = b**2
D = B - 4 * a * c
d = D ** 0.5
x1 = (-b + d) / (2 * a)
x2 = (-b - d) / (2 * a)

if D < 0:
    print('Корней нет')
else:
    print(f'Корни уравнения: \nx1 = {x1} \nx2 = {x2}')
