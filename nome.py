import re

pattern = r"^[A-Z][a-z]+(?: [A-Z][a-z]+)+$"

while True:
    nome = input("Digite o nome: ")

    if nome.lower() == 'exit':
        break

    if re.match(pattern, nome):
        print("Nome válido")
    else:
        print("Nome inválido")
