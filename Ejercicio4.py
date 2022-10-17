anos = int(input('Escriba su edad:\n'))

ingresos = float(input('Cuales son sus ingresos?.\n'))

if anos >= 16 and ingresos > 1000:
    print('El solicitante TIENE que tributar')
else:
    print('El solicitante NO TIENE que tributar')