import string as s

res = []
n = 506

while n >= 10:
    res.append(n%16)
    n //= 16
res.append(n)
print(sum(res))
