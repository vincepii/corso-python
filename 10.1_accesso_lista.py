l = ['corso', 'di', 'python', 2024, True]

print(l[0])
assert l[0] == 'corso'

print(l[1:3])
assert l[1:3] == ['di', 'python']

print(l[-1])
assert l[-1] == True

print(l[:2])
assert l[:2] == ['corso', 'di']

print(l[3:])
assert l[3:] == [2024, True]

try:
  print(l[5])
except IndexError:
  print('Indice fuori range')

l[0] = 150
l[2:4] = ['a', 'b']
print(l)