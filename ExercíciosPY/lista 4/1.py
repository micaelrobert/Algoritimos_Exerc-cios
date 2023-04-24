x = 3
y = 4
z = 6

print(x + x * x **( y*x)/z)
print(((not(x + z < y))or (x + x * z >= y)) and True)
#no primeiro print python da prioridade a expressão dentro do primeiro parênteses, depois faz a divisão, e exibe o resultado
#no segundo print python segue a mesma linha de prioridade dos parenteses em "not"
#depois python da prioridade ao segundo parênteses, em seguida resolve a expressão completa e exibe o resultado.