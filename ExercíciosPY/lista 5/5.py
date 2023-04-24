ganho_hora = float(input("Digite o valor ganho por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_mensal = ganho_hora * horas_trabalhadas

print(f"O seu salário mensal é: R$ {salario_mensal:.2f}")