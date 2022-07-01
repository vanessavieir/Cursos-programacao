p=0
cont=0
ptermo=int(input('Digite o primeiro termo:'))
r=int(input('Digite a razão:'))
decimo=ptermo+(10-1)*r
for c in range(ptermo,decimo+r,r):
 print('{}'.format(c), end='--')
print('E...ACABOU')

