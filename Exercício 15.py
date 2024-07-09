comidas = ['leite', 'couve', 'computador', 'tomate', 'garfo', 'facao', 'tablet', 'suco']
bebidas = ['uva', 'colher', 'TV', 'vinho', 'cerveja', 'celular', 'banana']
talheres = ['arroz', 'iPhone', 'concha', 'whisky', 'red bull', 'feijão', 'colher de chá']

eletronicos = [] 
eletronicos.extend(["computador", "tablet", "TV", "celular", "iPhone"])

for item in eletronicos:
    if item in comidas:
        comidas.remove(item)
    if item in bebidas:
        bebidas.remove(item)
    if item in talheres:
        talheres.remove(item)

for item in ["leite", "garfo", "facao", "suco"]:
    if item in comidas:
        comidas.remove(item)

for item in ["uva", "colher", "banana"]:
    if item in bebidas:
        bebidas.remove(item)

for item in ["arroz", "whisky", "red bull", "feijão"]:
    if item in talheres:
        talheres.remove(item)

comidas.extend(["uva", "banana", "arroz", "feijão"])
bebidas.extend(["leite", "suco", "whisky", "red bull"])
talheres.extend(["garfo", "facao", "colher"])

print(f"comidas: {comidas}")
print(f"bebidas: {bebidas}")
print(f"talheres: {talheres}")
print(f"eletronicos: {eletronicos}")