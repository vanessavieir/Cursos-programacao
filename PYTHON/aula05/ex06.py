from datetime import date
ano=int(input('Digite que ano deseja analisar e caso queira analisar o ano atual, digite 0:'))
if ano==0: 
    ano=date.today().year # pega o anual atual
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('O ano de {} é bisexto!'.format(ano))
else:
    print('O ano {} não é bisexto!'.format(ano))