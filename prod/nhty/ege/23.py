def f(x, l:list=[]):
    if x < 2: return 0
    if x == 2: 
        res.append(l)
    f(x-2, l + [x-2])
    f(x//2, l + [x//2])

res = []
cnt = 0
f(52)
for i in res:
    if 14 in i:
        cnt += 1

print(cnt)