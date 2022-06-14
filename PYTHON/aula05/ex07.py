a=int(input('Digite um número:'))
b=int(input('Digite um número:'))
c=int(input('Digite um número:'))
if a<b and a<c:
    menor=a
if b<a and b<c:
    menor=b
if c<b and c<a:
    menor=c

if a>b and a>c:
    maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
    print('O menor número digitado foi {} e o maior foi {}'.format(menor,maior))
