msg1 = 'le stringhe'
msg2 = 'in Python'

msg3 = msg1 + msg2
# Qual'è il problema?
print(msg3)

# Meglio
msg3 = msg1 + ' ' + msg2
print(msg3)
# Oppure
msg3 = f'{msg1} {msg2}'
print(msg3)

chars = len(msg1)
print(f'Caratteri in msg1: {chars}')

msg4 = "Dante ha scritto \"La Divina Commedia\""
print(msg4)

msg5 = 3 * 'ciao'
print(msg5)

msg6 = '''Un messaggio
su diverse
linee.
'''
print(msg6)