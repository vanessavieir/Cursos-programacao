num=int(input('Digite um número:'))
mult=0
for c in range(1,11):
    mult=num*c
    print('{} x{:2}={}'.format(num,c,mult))
print('='*20)
print('FIM')