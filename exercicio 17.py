arquivo = float(input("Informe do tamanho do arquivo em MegaByte: "))
link = float(input("Informe a velocidade do link em Mbps: "))
tempo = ((arquivo * 8) / link) / 60
print ("O tempo aproximado de download é de %.2f minutos" %tempo)
