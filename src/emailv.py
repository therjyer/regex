import re

def verificar_email(email):
    email = email.strip()

    pattern = r"^[a-zA-Z0-9._-]*[a-z][a-zA-Z0-9._-]*@[a-zA-Z0-9.-]+\.(br)$"
    
    if re.fullmatch(pattern, email):
        print("\nE-mail válido")
    else:
        print("\nE-mail inválido")

def main():
    while True:
        email = input("Digite o e-mail: ")

        if email.lower() == 'exit':
            break
        
        verificar_email(email)

if __name__ == "__main__":
    main()