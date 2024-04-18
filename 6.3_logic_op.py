username = 'foo'
password = 'bar'
login = username == 'foo' and password == 'bar'
print(login)

temperatura = 20
liquido = temperatura > 0 and temperatura < 100
print(liquido)

# Comunemente, gli operatori logici sono usati direttamente sulle istruzioni
# if o elif
if temperatura > 0 and temperatura < 100:
    print('liquido')
else:
    print('non liquido')

if temperatura < 0 or temperatura > 100:
    print('non liquido')
else:
    print('liquido')

if not (temperatura < 0):
    print('non solido')
else:
    print('solido')

# James non esce di casa se fa freddo o se piove

# Caso 1:
print('caso 1')
freddo = True
piove = True

if freddo or piove:
    print('James non esce')

if not freddo and not piove:
    print('James esce')

# Caso 2:
print('caso 2')
freddo = False
piove = True

if freddo or piove:
    print('James non esce')

if not freddo and not piove:
    print('James esce')

# Caso 3:
print('caso 2')
freddo = True
piove = False

if freddo or piove:
    print('James non esce')

if not freddo and not piove:
    print('James esce')

# Caso 4:
print('caso 4')
freddo = False
piove = False

if freddo or piove:
    print('James non esce')

if not freddo and not piove:
    print('James esce')

# Nota: avremmo potuto semplicemente scrivere come sotto
# ma non avrebbe dimostrato l'uso di not e and.
if freddo or piove:
    print('James non esce')
else:
    print('James esce')
