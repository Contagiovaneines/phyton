qr = float(input("Quanto você guanha por hora: "));
ht = float(input("Quantas horas você trabalhou: "));
salario_bruto=(qr*ht);
ir=(11/100)*(salario_bruto);
inss=(8/100)*(salario_bruto);
sindicato=(5/100)*(salario_bruto);
desconto=(ir+inss+sindicato);
salario_liquido=(salario_bruto-desconto);
print("Valor dos impostos:");
print ("IR: %.2f" %ir);
print ("INSS: %.2f" %inss);
print ("Sindicato: %.2f" %sindicato);
print("SEU SALARIO LIQUIDO É : %.2f" %salario_liquido);