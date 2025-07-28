with open('24.txt', 'r') as f:
    l = f.readline().replace('+', '-').split('-')

s = ''
res = 0

for i in range(len(l)):
    if (l[i] != '' and l[i][0] != '0') or l[i] == '0':
        if s == '':
            s += l[i]
        else:
            s = s + '-' + l[i]
        if s.find('-') != -1:
            res = max(res, len(s))
    else:
        if l[i] != '' and l[i][0] == '0':
            s = l[i].lstrip('0')
        else:
            s = ''

print(res)
