import random

print('*********************')
print(' Jogo Da Adivinhação ')
print('*********************')

numero_ia = random.choice(range(1,10))

palpite = input('Digite um número: ')

palpite_int = int(palpite)

if palpite_int == numero_ia:
    print('Voce Acertou!')
else:
    print('Voce Errou!')
    print('O numero certo era:', numero_ia)

