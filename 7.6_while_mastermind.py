import random
random = random.randint(1, 10)
while True:
    numero = int(input('inserisci numero: '))
    if numero < random:
        print('Troppo basso')
    elif numero > random:
        print('Troppo alto')
    else:
        print(f'Bravo, il numero è {random}')
        break
