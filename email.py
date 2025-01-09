import re

def verificar_email(email):
    pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.(br)$"
    
    if re.match(pattern, email):
        print("E-mail válido")
    else:
        print("E-mail inválido")

def main():
    while True:
        email = input("Digite o e-mail: ")

        if email.lower() == 'exit':
            break
        
        verificar_email(email)

if __name__ == "__main__":
    main()
