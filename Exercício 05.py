lista = [1, 2, 3, 4, 2, 3, 5, 6, 1, 7, 8, 9, 7]

lista_sem_duplicatas = []

for elemento in lista:
    if elemento not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(elemento)

print("Lista sem duplicatas:", lista_sem_duplicatas)