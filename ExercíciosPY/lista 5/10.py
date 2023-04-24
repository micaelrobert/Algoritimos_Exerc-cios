peso_pessoa = float(input("Digite o peso em kg: "))
altura_2 = float(input("Digite a altura em metros: "))

imc = peso_pessoa / (altura_2 ** 2)
print(f"O IMC é: {imc:.2f}")
