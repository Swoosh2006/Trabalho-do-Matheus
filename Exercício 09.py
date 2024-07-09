while True:

    print("\nSelecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Digite o número da operação desejada: ")

    if opcao == '5':
        print("Encerrando a calculadora.")
        break 

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if opcao == '1':
        resultado = numero1 + numero2
        print(f"A soma de {numero1} + {numero2} é:", resultado)
    elif opcao == '2':
        resultado = numero1 - numero2
        print(f"A subtração de {numero1} - {numero2} é:", resultado)
    elif opcao == '3':
        resultado = numero1 * numero2
        print(f"A multiplicação de {numero1} * {numero2} é:", resultado)
    elif opcao == '4':
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"A divisão de {numero1} / {numero2} é:", resultado)
        else:
            print("Erro: divisão por zero!")
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")