# Metodo 1: moltiplico ogni valore da 1..10 per ogni valore da 1..10:
end = 11
for x in range(1, end):
    for y in range(1, end):
        print(f'{x*y:>3}', end=' ')
    print(' ')

print('\n\n####', end='\n\n\n')

# Metodo 2: genero ogni riga della tabella usando lo step della funzione range
start = 1
end = 10
step = 1
for y in range(1, 11):
    for x in range(start * y, end * y + 1, step * y):
        print(f'{x:>3}', end=' ')
    print('')
