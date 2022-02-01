peso_peixes = eval(input('Digite o peso dos peixes: '))

if peso_peixes  > 50:

 peso_excesso = peso_peixes - 50

 multa = 4 * peso_excesso

 print(f'Hoje João pescou {peso_peixes}Kg de peixes, {peso_excesso}Kg a mais que o estabelecido pelo regulamento e isso gerou uma multa de R${multa:.2f}')

else:

 print(f'Hoje João pescou {peso_peixes}Kg de peixes, está dentro do limite estabelecido pelo regulamento')

