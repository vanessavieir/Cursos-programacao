velocidade=int(input('Digite a velocidade do carro:'))
print('Bom dia! dirija com cuidado <3')
multa=(velocidade-80)*7
if velocidade<=80:
    print('Você está dentro do limite de velocidade!')
else:
    print( 'ATENÇÃO! Você excedeu o  limite de 80Km/h e sua multa será de R${:.2F}'.format(multa))
    