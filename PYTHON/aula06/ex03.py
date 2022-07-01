cont=0
s=0
for c in range(1,500):
 if c%2!=0 and c%3==0:
    cont=cont+1
    s=s+c
print('A soma dos {} valores equivale a: {}' .format(cont,s))