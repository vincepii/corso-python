def esercizio(lista1, lista2):
    for n in lista2:
        if n not in lista1:
            lista1.append(n)
    return lista1

res = esercizio([1,2,3], [5,3,4])
print(res)
