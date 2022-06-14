distancia=float(input('Digite a sua distância percorrida em Km:'))
preco1=distancia*0.5
preco2=distancia*0.45
if distancia<=200:
    print('O preço final da sua passagem será de R${:.2f}'.format(preco1))
else:
    print('O preço final da sua passagem será de R${:.2f}'.format(preco2))