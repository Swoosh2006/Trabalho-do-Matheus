n = int(input("Quantos termos gerar: "))

f0, f1 = 0, 1

fibonacci = [1] * n

for i in range(1, n):
    fibonacci[i] = f0 + f1
    f0, f1 = f1, fibonacci[i]

print(fibonacci)
b = c