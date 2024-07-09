numeros = input("Digite os números separados por espaço: ").split()

numeros = list(map(int, numeros))

maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("O maior número na lista é:", maior)
print("O menor número na lista é:", menor)