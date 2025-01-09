import re

def verificar_nome(nome):
    pattern = r"^[A-Z][a-z]+(?: [A-Z][a-z]+)+$"
    
    if re.match(pattern, nome):
        print("\nNome válido")
    else:
        print("\nNome inválido")

def main():
    while True:
        nome = input("Digite o nome: ")

        if nome.lower() == 'exit':
            break
        
        verificar_nome(nome)

if __name__ == "__main__":
    main()