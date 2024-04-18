lato = 5
print(f'Tipo della variabile lato: {type(lato)}')

pi = 3.14159265359
print(type(pi))

nome = 'Vincenzo'
print(type(nome))

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# foo = lato + nome

foo = 5 # str(lato) + nome
print("Il perimetro del quadrato è " + str(foo))
