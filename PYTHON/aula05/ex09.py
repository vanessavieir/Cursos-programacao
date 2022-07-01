m1=float(input('Digite o primeiro lado do triângulo:'))
m2=float(input('Digite o segundo lado do triângulo:'))
m3=float(input('Digite o terceiro lado do triângulo:'))
if m1+m2>m3 and m1+m3>m2 and m2+m3>m1:
    print('-=-'*20)
    print('O triãngulo é válido')
    print('-=-'*20)
else:
    print('O triângulo é inválido, pois a soma de dois lados é menor que o terceiro')