def bin_search(l, n):
    low = 0
    high = len(l)-1

    while high >= low:
        mid = (low + high) // 2
        mid_num = l[mid]

        if n == mid_num:
            return mid

        if n > mid_num:
            low = mid + 1

        if n < mid_num:
            high = mid - 1
    return None

print(bin_search([1, 4, 10, 56, 76, 89], 89))
