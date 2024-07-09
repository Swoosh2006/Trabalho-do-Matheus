soma = 0
while True:
    try:
        valor_digitado = float(input("Digite um valor para a soma (ou 0 para encerrar): "))
        if valor_digitado == 0:
            break
        soma += valor_digitado
    except ValueError:
        print("Por favor, digite um número válido.")

print(f"Resultado da soma: {soma}")