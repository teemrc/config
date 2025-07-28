import string as s
def trans(n, c):
    res = ''
    while n >= 10:
        if n%c >= 10:
            res += s.ascii_lowercase[(n%c)-10]
        else:
            res += str(n%c)
        n //= c
    res = res[::-1]
    if not res[0] in s.digits and n == 0:
        return res
    else:
        return str(n) + res

print(trans(1845, 36))
		
