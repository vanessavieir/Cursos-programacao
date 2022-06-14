from random import randint
from time import sleep
computador=randint(0,5) # faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tentem adivinhar...')
print('-=-' * 20)
print('Pensei no número... {}'.format(computador))
jogador=int(input('Em que o número eu pensei?'))
print('PROCESSANDO...')
sleep(3)
if jogador==computador:
    print('Parabéns! Você conseguiu me vencer!!')
else:
    print('Você perdeu! Pois meu número sorteado foi {} e o seu foi {}'.format(computador, jogador))    