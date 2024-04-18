l = ['Alice', 2, 'Bob']

# len
lunghezza = len(l)
print(lunghezza)

# append
l.append(5)
print(l)

# extend
l.extend([4, 5, 6])
print(l)

l.append([4, 5, 6])
print(l)

# sort
l = [4, 7, 1, 3, 8, 6, 5, 2, 9]
l.sort()
print(l)

# pop
l.pop()
print(l)

# remove
l.remove(1)
print(l)

l = [1, 2, 3, 1, 2]
l.remove(1)
print(l)
