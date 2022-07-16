n=input('Digite algo: ')
print('O tipo primitivo de A corresponde a ', type(n))
print('Só tem espaço',n.isspace())
print('É um número?', n.isnumeric())
print('É alfanúmerico?',n.isalnum())
print('Contém letras maiúsculas?',n.isupper())
print('Contém letras minúsculas?',n.islower())
print('Está capitalizada?', n.istitle()) # contém letras maiúsculas e minúsculas.