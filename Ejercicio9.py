linea = int(input('Introduce un número entero:\n'))
for linea in range(linea + 1):
    for numeros in range(linea, 0, -1):
        print((numeros * 2 -1), end=' ')
    print('')