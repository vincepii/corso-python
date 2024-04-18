# Eliminare tutti gli utenti con nome lungo più di 3 caratteri

utenti = [
    'Alice',   # 0
    'Bob',     # 1
    'Charlie', # 2
    'Derek',   # 3
    'Ellie',   # 4
    'Frank',   # 5
]

indice = 0
while indice < len(utenti):
    if (len(utenti[indice]) <= 3):
        indice += 1
        continue
    utenti.pop(indice)
print(utenti)

# Modi migliori per farlo #1
keep = []
for utente in utenti:
    if len(utente) <= 3:
        keep.append(utente)
print(keep)

# Modi migliori per farlo #2
print(list(filter(lambda x: len(x) <= 3, utenti)))
