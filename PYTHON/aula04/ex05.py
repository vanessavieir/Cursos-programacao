# O random é um randomizador de elementos de uma lista
# O shuffle é usado para embaralhar e mostrar diferentes ordens numa lista.

import random
n1=str(input('Digite o nome do aluno 1: '))
n2=str(input('Digite o nome do aluno 2: '))
n3=str(input('Digite o nome do aluno 3: '))
n4=str(input('Digite o nome do aluno 4: '))
lista=[n1, n2, n3, n4]
random.shuffle(lista)
print('Os alunos escolhidos foram:')
print(lista)