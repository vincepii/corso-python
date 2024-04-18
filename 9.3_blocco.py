def blocco(lato, carattere):
    for _ in range(lato):
        for _ in range(lato):
            print(carattere, end='')
        print('')

blocco(5, '#')