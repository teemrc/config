def qsort(l):
    if len(l) <= 1:
        return l
    n = l[0]

    low = [i for i in l if i < n]
    high = [i for i in l if i > n]

    return qsort(low) + [n] + qsort(high)

print(qsort([45, 98, 67, 89, 101, 34, 56]))
