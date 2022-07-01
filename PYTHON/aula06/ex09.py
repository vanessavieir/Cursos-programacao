from datetime import date
atual=date.today().year
totmaior=0
totmenor=0
for pess in range(1,8):
    ano=int(input('Digite aqui seu ano de nascimento:'))
    idade=atual-ano
    if idade>=21:
       totmaior+=1
    else:
       totmenor+=1
print('Ao todo tivemos {} pessoas maior de idade'.format(totmaior))
print('E também tivemos {} pessoas menor de idade'.format(totmenor))