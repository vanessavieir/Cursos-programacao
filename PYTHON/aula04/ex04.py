# Com o uso do choice se pode gerar um nome aleatório de um aluno numa lista.

from random import choice
n1=input('Digite o nome do aluno 1: ')
n2=input('Digite o nome do aluno 2: ')
n3=input('Digite o nome do aluno 3: ')
n4=input('Digite o nome do aluno 4: ')
lista=(n1, n2, n3, n4)
alunoescolhido=choice(lista)
print('O aluno escolhido foi: {}'.format(alunoescolhido))