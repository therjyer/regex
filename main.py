import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import cpf
import phone
import name
import password
import emailv

def main():
    while True:
        print("\nEscolha a opção desejada:")
        print("1. Validar Nome")
        print("2. Validar CPF")
        print("3. Validar Telefone")
        print("4. Validar E-mail")
        print("5. Validar Senha")
        print("6. Encerrar")
        
        opcao = input("Digite o número da opção (1-6): ")
        
        if opcao == '1':
            while True:
                nome_input = input("Digite o nome: ")
                if nome_input.lower() == 's':
                    break
                name.verificar_nome(nome_input)
        
        elif opcao == '2':
            while True:
                cpf_input = input("Digite o CPF: ")
                if cpf_input.lower() == 's':
                    break
                cpf.verificar_cpf(cpf_input)
        
        elif opcao == '3':
            while True:
                telefone_input = input("Digite o telefone: ")
                if telefone_input.lower() == 's':
                    break
                phone.verificar_telefone(telefone_input)
        
        elif opcao == '4':
            while True:
                email_input = input("Digite o e-mail: ")
                if email_input.lower() == 's':
                    break
                emailv.verificar_email(email_input)
        
        elif opcao == '5':
            while True:
                senha_input = input("Digite a senha: ")
                if senha_input.lower() == 's':
                    break
                password.verificar_senha(senha_input)
        
        elif opcao == '6':
            break
        
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()