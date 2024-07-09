lista = []

while True:
    elemento = input("Digite algum nome para adicionar à lista (ou 'parar' para sair): ")
    if elemento.lower() == "parar":
        break 
    lista.append(elemento)

print("Lista completa:", lista)