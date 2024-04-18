def speed(distance, time):
    if time == 0:
        raise ZeroDivisionError
    return distance / time

try:
    s = speed(100, 0)
    print(s)
except ZeroDivisionError:
    print('Qualcosa è andato storto')

try:
    s = speed(100, 10)
    print(s)
except ZeroDivisionError:
    print('Qualcosa è andato storto')
