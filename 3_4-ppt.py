
import random

opt = ('piedra', 'papel', 'tijera')

continuar = True


while continuar:    
    usuario = random.choice(opt)
    PC = random.choice(opt)


    print(f'usuario: {usuario}')
    print(f'PC: {PC}')


    if usuario == PC:
        print('Empate!')
    else:
        if usuario == 'piedra':
            if PC == 'papel':
                print('Perdiste!')
            else:
                print('Ganaste!')

        elif usuario == 'papel':
            if PC == 'tijera':
                print('Perdiste!')
            else:
                print('Ganaste!')
        else: # usuario == tijera
            if PC == 'piedra':
                print('Perdiste!')
            else:
                print('Ganaste!')

    ret = input('Deseas continuar [s/N]: ')

    if ret == 'N' or ret == 'n':
        break


print('El juego ha terminado')