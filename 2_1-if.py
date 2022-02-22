
var1 = False
var2 = False

entero = 3

if entero < 4:
    print(f'Entero menor a 4: {entero}')

elif entero == 4:
    print('Entero igual a 4')

else:
    print('Entero mayor a 4')


print('  Entero menor a 4') if entero < 4 else print('Etero igual o mayor que 4')