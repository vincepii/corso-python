print('Lato 1:')
lato1 = input()
print('Lato 2:')
lato2 = input()
print('Lato 3:')
lato3 = input()

print(f'Lati: {lato1}, {lato2}, {lato3}')

if lato1 == lato2 == lato3:
    print('Equilatero')
elif lato1 == lato2 or lato1 == lato3 or lato2 == lato3:
    print('Isoscele')
else:
    print('Scaleno')
