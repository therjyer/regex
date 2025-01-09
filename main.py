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
            nome_input = input("Digite o nome: ")
            name.verificar_nome(nome_input)
        
        elif opcao == '2':
            cpf_input = input("Digite o CPF: ")
            cpf.verificar_cpf(cpf_input)
        
        elif opcao == '3':
            telefone_input = input("Digite o telefone: ")
            phone.verificar_telefone(telefone_input)
        
        elif opcao == '4':
            email_input = input("Digite o e-mail: ")
            emailv.verificar_email(email_input)
        
        elif opcao == '5':
            senha_input = input("Digite a senha: ")
            password.verificar_senha(senha_input)
        
        elif opcao == '6':
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()