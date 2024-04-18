def stato_acqua(temp):
    if temp <= 0:
        return 'solido'
    if temp >= 100:
        return 'gas'
    return 'liquido'

y = stato_acqua(-10)
print(y)
y = stato_acqua(10)
print(y)
y = stato_acqua(105)
print(y)
