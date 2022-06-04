# teorema de Pitágoras

from math import sqrt
n=float(input('Digite um valor para o cateto oposto:'))
n1=float(input('Digite um valor para o cateto adjacente:'))
hipo=sqrt(n*2+n1*2)
print('O valor do cateto oposto vale {} , do cateto adjacente {} e o valor da hipotenusa {:.2f}'.format(n , n1 , hipo))