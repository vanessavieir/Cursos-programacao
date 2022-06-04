# calculando o valor a pagar por um período de aluguel de carro

dias=int(input('Digite a quantidade de dias que o motorista usou o carro:'))
km=float(input('Digite a quantidade de quilômetros percorrridos por ele:'))
dia=60
quilômetro=0.15
preco=(dias*dia)+(km*quilômetro)
print('O valor a ser pago será: {} '.format(preco))