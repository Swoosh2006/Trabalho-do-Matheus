
vagas = []

while True:
    print("\n### Sistema de Gerenciamento de Vagas de Emprego ###")
    print("1. Cadastrar nova vaga")
    print("2. Visualizar vagas cadastradas")
    print("3. Sair")

    escolha = input("Escolha uma opção (1/2/3): ")

    if escolha == '1':
        print("\n### Cadastro de Nova Vaga ###")
        empresa = input("Nome da empresa: ")
        cargo = input("Cargo: ")
        salario = input("Salário: ")
        descricao = input("Descrição da vaga: ")

        nova_vaga = {
            'Empresa': empresa,
            'Cargo': cargo,
            'Salário': salario,
            'Descrição': descricao
        }

        vagas.append(nova_vaga)
        print("Vaga cadastrada com sucesso!")

    elif escolha == '2':
        print("\n### Vagas Cadastradas ###")
        if len(vagas) == 0:
            print("Não há vagas cadastradas no momento.")
        else:
            for idx, vaga in enumerate(vagas, start=1):
                print(f"\nVaga {idx}:")
                print(f"Empresa: {vaga['Empresa']}")
                print(f"Cargo: {vaga['Cargo']}")
                print(f"Salário: {vaga['Salário']}")
                print(f"Descrição: {vaga['Descrição']}")

    elif escolha == '3':
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1/2/3).")
