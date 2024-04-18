# Trova l'utente di nome Charlie

utenti = [
    'Alice',   # 0
    'Bob',     # 1
    'Charli', # 2
    'Derek',   # 3
    'Ellie',   # 4
    'Frank',   # 5,
    'Georg'
]

indice = 0
while True:
    utente = utenti[indice]
    if utente == 'Charlie':
        print(f'Trovato Charlie in posizione {indice}')
        break
    if indice == len(utenti) - 1:
        print('Lista utenti finita')
        break
    indice += 1
