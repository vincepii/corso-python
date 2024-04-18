# Per ogni numero da 1 a 10, elencare tutti i suoi divisori
for n in range(1, 11):
    for d in range(1, n + 1):
        if n % d == 0:
            print(f'{n} è divisibile per {d}')
    print('')
