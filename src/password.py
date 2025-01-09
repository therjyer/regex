import re

def verificar_senha(senha):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8}$"
    
    if re.match(pattern, senha):
        print("\nSenha válida")
    else:
        print("\nSenha inválida")

def main():
    while True:
        senha = input("Digite a senha: ")

        if senha.lower() == 'exit':
            break
        
        verificar_senha(senha)

if __name__ == "__main__":
    main()
