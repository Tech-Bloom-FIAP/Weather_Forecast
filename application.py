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

def formata_dados(nascimento: str = "" , cpf: str = "" , telefone: str = "" ):
    nascimento_formatado = f"{nascimento[:2]}/{nascimento[2:4]}/{nascimento[4:]}"
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:11]}"
    
    return nascimento_formatado, cpf_formatado, telefone_formatado

# LOGIN E CADASTRO
def login():
    while True:
        try:    
            cpf = input("Digite seu CPF: ")
            if cpf < 11 or cpf > 11:
                raise CpfError
            senha = input("Criar uma senha: ")
            return cpf, senha
        except CpfError:
            print("O cpf informado não é valido. \nExemplo: 12345678910 \n")
    
def cadastro():
    with open('./arquiva.txt', 'r') as arquivo:
        dados = json.load(arquivo)
    while True:
        try:    
            nome = input("Digite seu nome completo: ")
            dados["Nome"].append(nome)
            data = formata_dados(nascimento=input("Digite sua data de nascimento: "))[0]
            cpf = formata_dados(cpf = input("Digite seu CPF: "))[1]
            if len(cpf) < 14 or len(cpf) > 14 :
                raise CpfError
            email = input("Digite seu E-mail: ")
            telefone = formata_dados(telefone = input("Digite seu telefone: "))[2]
            if len(telefone) < 15 or len(telefone) > 15:
                raise TelefoneError
            senha = input("Criar uma senha: ")
            with open('./arquiva.txt', 'w') as arquivo:
                json.dump(dados, arquivo, indent=4)
            break
        except TelefoneError:
            print("O telefone informado não é válida. \nExemplo: 11912345678 \n")
        except CpfError:
            print("O cpf informado não é valido. \nExemplo: 12345678910 \n")

def dados(opcao):
    match opcao:
        case 1:
            cadastro()
        case 2:
            login()


def menu():
    """
    Função principal que controla o menu principal e as ações do usuário.
    """
    
    print('''1- Cadastro
2- Login''')
    opcao = int(input("Escolha uma opção: "))
    dados(opcao)

    '''
    while opcao != 3:
        while True:
            try:
                print("1 - Ver Produtos")
                print("2 - Depositar Produto(s)")
                print("3 - Finalizar sessão \n")

                opcao = int(input("Escolha a opção desejada: "))
                if opcao <= 0 or opcao > 3:
                    raise VerificaError
                print("\n")

                match opcao:
                        case 1: 
                            escolha_produto()
                        case 2:
                            descarte()
                        case 3:
                            print("ElekSell agradece a sua vinda, muito obrigado !")
                            break
            except ValueError:
                print("O valor informado não é um número \n")
            except VerificaError:
                print("Digite apenas as opções exibidas em tela \n")'''

menu()