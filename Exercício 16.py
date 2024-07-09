palavras = ["python", "java", "c", "javascript", "html", "css", "ruby"]

letra = input("Digite a letra inicial para filtrar as palavras: ")

for palavra in palavras:
    if palavra.startswith(letra):
        print(palavra)