def fatorial(num):
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
    return fat


print(fatorial(5))
