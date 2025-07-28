import  random

low = 'QWERTYUIOPASDFGHJKLZXCVBNM'
upp = 'qwertyuiopasdfghjklzxcvbnm'
nums = '0123456789'
sym = '!@#$%^&*№:?'

string = low + upp + nums
len = 13
password = ''.join((random.sample(string, len)))

print(f'Ваш пароль: {password}')
