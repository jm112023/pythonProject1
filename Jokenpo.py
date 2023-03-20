from random import randint
from time import sleep
print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
itens = ('PEDRA','PAPEL','TESOURA')
jogador = int(input('Escolha sua jogada: '))
computador = randint(0, 2)
print ('Jo')
sleep(1)
print('Ken')
sleep(2)
print('Poo!')
print('O Jogador jogou {} e a maquina jogou {}'.format(itens[jogador],itens[computador]))
if jogador == 0:
    if computador == 0:
        sleep(1)
        print('EMPATE!')
    if computador == 1:
        sleep(1)
        print('COMPUTADOR VENCEU!')
    if computador == 2:
        sleep(1)
        print('JOGADOR VENCEU!')
elif jogador == 1:
    if computador == 0:
        sleep(1)
        print('JOGADOR VENCEU!')
    if computador == 1:
        sleep(1)
        print('EMPATE!')
    if computador == 2:
        sleep(1)
        print('COMPUTADOR VENCEU!')
elif jogador == 2:
    if computador == 0:
        sleep(1)
        print('COMPUTADOR VENCEU!')
    if computador == 1:
        sleep(1)
        print('JOGADOR VENCEU!')
    if computador == 2:
        sleep(1)
        print('EMPATE!')
else:
    print('Joda invalida!')