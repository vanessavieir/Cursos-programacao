salario=float(input('Digite o seu salário:'))
if salario<=1250:
    Nsalario=salario+(salario*0.15)
    print('O seu salário com 15% de aumento será de R${:.2f}'.format(Nsalario))
else:
    Nsalario=salario+(salario*0.10)
    print('O seu salário com 10% de aumento será de R${:.2f}'.format(Nsalario))