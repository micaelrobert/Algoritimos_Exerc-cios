num = int(input("Digite um número: "))
fatorial = 1
for i in range(2, num+1):
    fatorial *= i

print("O fatorial de", num, "é", fatorial)