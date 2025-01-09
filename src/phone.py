import re

def verificar_telefone(telefone):
    pattern = r"^(\(\d{2}\)\s9\d{4}-?\d{4}|\d{2}\s9\d{8})$"
    
    if re.match(pattern, telefone):
        print("\nTelefone válido")
    else:
        print("\nTelefone inválido")

def main():
    while True:
        telefone = input("Digite o telefone: ")

        if telefone.lower() == 'exit':
            break
        
        verificar_telefone(telefone)

if __name__ == "__main__":
    main()