num = int(input("Digite um número inteiro positivo: "))

if num <= 0:
    print("O número não é positivo.")
else:
    soma_divisores = 0
    
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i
    
    if soma_divisores == num:
        print(f"{num} é um número perfeito.")
    else:
        print(f"{num} não é um número perfeito.")
