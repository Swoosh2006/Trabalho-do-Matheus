fila_de_atendimento = []

fila_de_atendimento.append("João")
fila_de_atendimento.append("Alessandro")
fila_de_atendimento.append("Avelar")

print("Fila de Atendimento:")
for cliente in fila_de_atendimento:
    print(f" - {cliente}")

if fila_de_atendimento:
    cliente_atendido = fila_de_atendimento.pop(0)
    print(f"\nCliente '{cliente_atendido}' foi atendido e removido da fila.")

fila_de_atendimento.append("Ana")

print("\nFila de Atendimento Atualizada:")
for cliente in fila_de_atendimento:
    print(f" - {cliente}")

if fila_de_atendimento:
    cliente_atendido = fila_de_atendimento.pop(0)
    print(f"\nCliente '{cliente_atendido}' foi atendido e removido da fila.")

print("\nFila de Atendimento Final:")
for cliente in fila_de_atendimento:
    print(f" - {cliente}")