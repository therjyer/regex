import re

def verificar_senha(senha):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8}$"
    
    if re.match(pattern, senha):
        print("Senha válida")
    else:
        print("Senha inválida")

def main():
    while True:
        senha = input("Digite a senha: ")

        if senha.lower() == 'exit':
            break
        
        verificar_senha(senha)

if __name__ == "__main__":
    main()
