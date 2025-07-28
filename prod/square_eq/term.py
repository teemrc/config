def reh(a, b, c):
    d = (b**2)-4*a*c
    if d < 0:
        return None
    elif d == 0:
        return ((d**0.5)-b)/(2*a)
    else:
        return ((d**0.5)-b)/(2*a), (-(d**0.5)-b)/(2*a)

inp = [int(i) for i in input().split(' ')]

print(reh(inp[0], inp[1], inp[2]))
