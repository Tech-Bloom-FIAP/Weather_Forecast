'''
1- Previsão do tempo + Chance de enchentes (Previsão de enchentes)
2- Como se portar em uma enhchente  
3- Psicologia (TeleMedicina)
'''

import json

#Exceções personalizadas
class TelefoneError(Exception):
     pass
class CpfError(Exception):
     pass
class VerificaError(Exception):
     pass

def formata_dados(nascimento: str = "" , cpf: str = "" , telefone: str = "" ):
    nascimento_formatado = f"{nascimento[:2]}/{nascimento[2:4]}/{nascimento[4:]}"
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:11]}"
    
    return nascimento_formatado, cpf_formatado, telefone_formatado

# LOGIN E CADASTRO
def login():
    while True:
        try:    
            cpf = formata_dados(cpf = input("Digite seu CPF: "))[1]
            if len(cpf) < 14 or len(cpf) > 14 :
                raise CpfError
            senha = input("Digite sua uma senha: ")
            return cpf, senha
        except CpfError:
            print("O cpf informado não é valido. \nExemplo: 12345678910 \n")
    
def cadastro():
    with open('./dados.txt', 'r') as arquivo:
        dados = json.load(arquivo)
    while True:
        try:    
            nome = input("Digite seu nome completo: ")
            dados["nome"].append(nome)

            data = formata_dados(nascimento=input("Digite sua data de nascimento: "))[0]
            dados["data"].append(data)

            cpf = formata_dados(cpf = input("Digite seu CPF: "))[1]
            if len(cpf) < 14 or len(cpf) > 14 :
                raise CpfError
            dados["cpf"].append(cpf)

            email = input("Digite seu E-mail: ")
            dados["email"].append(email)

            telefone = formata_dados(telefone = input("Digite seu telefone: "))[2]
            if len(telefone) < 15 or len(telefone) > 15:
                raise TelefoneError
            dados["telefone"].append(nome)

            senha = input("Criar uma senha: ")
            dados["senha"].append(senha)

            with open('./dados.txt', 'w') as arquivo:
                json.dump(dados, arquivo, indent = 4)
            break
        except TelefoneError:
            print("O telefone informado não é válida. \nExemplo: 11912345678 \n")
        except CpfError:
            print("O cpf informado não é valido. \nExemplo: 12345678910 \n")

def verifica():
    verificado = False
    with open('./dados.txt', 'r') as arquivo:
        dados = json.load(arquivo)

    cpf, senha = login()

    cpfs = dados.get("cpf", [])
    senhas = dados.get("senha", [])
    
    for i in range(len(cpfs)):
        if cpf == cpfs[i] and senha == senhas[i]:
            return True
    return False

# MENU SECUNDÁRIO

def menusec():
    while True:
        try: 
            print('''1- Previsões
        2- 
        3- Psicologia''')
            opcao = int(input("Escolha uma opção: "))
            print("\n")
            if opcao <= 0 or opcao > 2:
                print("\n")
                raise VerificaError
        except ValueError:
            print("O valor informado não é um número \n")
        except VerificaError:
                print("Digite apenas as opções exibidas em tela \n")



def menu():
    """
    Função principal que controla o menu principal e as ações do usuário.
    """
    while True:   
        try:
            print('''1- Cadastro
2- Login''')
            opcao = int(input("Escolha uma opção: "))
            print("\n")
            if opcao <= 0 or opcao > 2:
                print("\n")
                raise VerificaError
                
            if opcao == 1:
                cadastro()
            elif opcao == 2:
                if verifica():
                    print("FOI")
                    #menusec()
                    break
                else:
                    print("Login invalido")
        except ValueError:
            print("O valor informado não é um número \n")
        except VerificaError:
                print("Digite apenas as opções exibidas em tela \n")


menu()