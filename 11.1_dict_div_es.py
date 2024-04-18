def esercizio(n, d):
    ret = {}
    for i in range(1, n+1):
        if i % d == 0:
            ret[i] = True
        else:
            ret[i] = False
    return ret

res = esercizio(3, 2)
print(res)
