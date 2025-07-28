def f(num):
    nums = {
        1:'I',
        5:'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }

    def razrad(num):
        ost = []
        for i in list(nums.keys())[::-1]:
            ost.append([num//i, i])
            num %= i

        for i in range(6, 0, -1):
            if ost[i][0] != 0 and i % 2 == 0 and ost[i][0] == 4:
                ost[i][0] = -1
                ost[i-1][0] += 1
            elif ost[i][0] != 0 and i % 2 == 0 and ost[i][0] == 5:
                ost[i][0] = 0
                ost[i-1][0] += 1
            elif ost[i][0] != 0 and i % 2 == 1 and ost[i][0] == 2:
                ost[i][0] = 0
                ost[i-1][0] += 1
        return ost

    sn = list(str(num))
    ost = []
    res = ''

    for i in range(len(sn)-1, -1, -1):    
        for j in razrad(int(sn[len(sn)-1-i])*(10**i)):
            if j[0] < 0:
                res = res[:-1] + nums[j[1]] + res[-1]
            for i in range(j[0]):
                res += nums[j[1]]

    return res
