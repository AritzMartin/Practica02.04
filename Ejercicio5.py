nombre = input('Escriba su nombre:\n')
sexo = input('Escriba su sexo (h o m):\n')

if sexo == 'm':
    if nombre[0].lower() < 'm':
        print('Estas en el grupo A')
    else:
        print('Estas en el grupo B')
elif sexo == 'h':
    if nombre[0].lower() > 'n':
        print('Estas en el grupo A')
    else:
        print('Estas en el grupo B')
