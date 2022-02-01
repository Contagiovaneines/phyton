import math

m2 = float(input('informe a quantidade de METRO QUADRADO (m²) a ser pintado: '))
consumo_litro = m2 / 6
print('\no consumo de tinta é: {:.2f} LITROS\n'.format(consumo_litro))
qtd_latas18 = consumo_litro / 18
qtd_latas36 = consumo_litro / 3.6
print('a quantidade de GALOES de 18 LITROS a ser usado é: {}'.format(math.ceil(qtd_latas18)))
print('a quantidade de LATAS de 3,6 LITROS a ser usado é: {}\n'.format(math.ceil(qtd_latas36)))
valor_total18 = math.ceil(qtd_latas18) * 80
valor_total36 = math.ceil(qtd_latas36) * 25
print('o valor total em GALOES de 18 LITROS é: R${}'.format(valor_total18))
print('o valor total em LATAS de 3,6 LITROS é: R$ {}\n'.format(valor_total36))
print('considerando o menor desperdíciode tinta, temos: \n')

qtd_latas_mistas18 = ((consumo_litro * 0.10) + consumo_litro) / 18
qtd_litros18 = math.trunc(qtd_latas_mistas18) * 18
resto18 = ((consumo_litro * 0.10) + consumo_litro) - qtd_litros18
qtd_latas_mistas36 = resto18 / 3.6
qtd_latas_mistas_total = math.trunc(qtd_latas_mistas18) + math.ceil(qtd_latas_mistas36)
valor_misto18 = math.trunc(qtd_latas_mistas18) * 80
valor_misto36 = math.ceil(qtd_latas_mistas36) * 25
total_misto = valor_misto18 + valor_misto36

print('quantidade de latas de 18 litros: {}'.format(math.trunc(qtd_latas_mistas18)))
print('qtd latas de 3,6: {}'.format(math.ceil(qtd_latas_mistas36)))
print('qtd latas mistas: {}'.format(qtd_latas_mistas_total))
print('\no valor total considerando GALOES e LATAS é (acresentando 10% de quebra): R$ {}'.format(total_misto))
