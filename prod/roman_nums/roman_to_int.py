def f(num):
    nums = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    res = 0
    num = list(num)
    for i in range(len(num)):
        if str(nums[num[i]])[0] == '1' and i != len(num)-1 and nums[num[i]] < nums[num[i+1]]: 
            res -= nums[num[i]]
        else:
            res += nums[num[i]]

    return res
