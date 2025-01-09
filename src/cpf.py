import re

def verificar_cpf(cpf):
    pattern = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    
    if re.match(pattern, cpf):
        print("\nCPF válido")
    else:
        print("\nCPF inválido")

def main():
    cpf = input("Digite o CPF: ")
    verificar_cpf(cpf)

if __name__ == "__main__":
    main()