alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
    if nome.lower() == "fim":
        break
    alunos.append(nome) 

print("Lista de alunos:")
for aluno in alunos:
    print(aluno)