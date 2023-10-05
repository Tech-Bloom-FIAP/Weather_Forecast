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
    with open('./Arquivos/dados.txt', 'r') as arquivo:
        dados = json.load(arquivo)
    while True:
        try:    
            nome = input("Digite seu nome completo: ")
            dados["nome"].append(nome)

            data = formata_dados(nascimento=input("Digite sua data de nascimento: "))[0]
            dados["data"].append(data)

            cpf = formata_dados(cpf = input("Digite seu CPF: "))[1]
            if len(cpf) < 14 or len(cpf) > 14:
                raise CpfError
            dados["cpf"].append(cpf)

            email = input("Digite seu E-mail: ")
            dados["email"].append(email)

            telefone = formata_dados(telefone = input("Digite seu telefone: "))[2]
            if len(telefone) < 15 or len(telefone) > 15:
                raise TelefoneError
            dados["telefone"].append(telefone)

            senha = input("Criar uma senha: ")
            dados["senha"].append(senha)

            with open('./Arquivos/dados.txt', 'w') as arquivo:
                json.dump(dados, arquivo, indent = 4)
            break
        except TelefoneError:
            print("O telefone informado não é válida. \nExemplo: 11912345678 \n")
        except CpfError:
            print("O cpf informado não é valido. \nExemplo: 12345678910 \n")

def verifica():
    verificado = False
    with open('./Arquivos/dados.txt', 'r') as arquivo:
        dados = json.load(arquivo)

    cpf, senha = login()

    cpfs = dados.get("cpf", [])
    senhas = dados.get("senha", [])
    
    for i in range(len(cpfs)):
        if cpf == cpfs[i] and senha == senhas[i]:
            return True
    return False

# MENU SECUNDÁRIO

def preverEmbu(chuva_prevista, nivel_atualEmbu : float = 2.5, limite_maxEmbu : float = 4):
    '''Usa o nível atual do rio e a chuva prevista para saber se há chance de enchente'''

    aumento_por_chuva = chuva_prevista * 0.0125
    nivel_previsto = round(nivel_atualEmbu + aumento_por_chuva, 2)

    if nivel_previsto <= limite_maxEmbu - 1:
        print (f"Baixo risco de alagamento no Rio Embu-Guaçu, Nível previsto: {nivel_previsto}")

    elif nivel_previsto <= limite_maxEmbu - 0.25:
        print (f"Risco de alagamento no Rio Embu-Guaçu, Nível previsto: {nivel_previsto}")

    else :
        print(f"Grande risco de alagamento no Rio Embu-Guaçu, Nível previsto: {nivel_previsto}")

def preverSanta(chuva_prevista ,nivel_atualSanta : float = 2, limite_maxSanta : float = 2.5):
    '''Usa o nivel atual do rio e a chuva prevista para saber se há chance de enchente'''

    aumento_por_chuva = chuva_prevista * 0.0125
    nivel_previsto = round(nivel_atualSanta + aumento_por_chuva, 2)

    if nivel_previsto <= limite_maxSanta - 0.25:
        print (f"Risco de alagamento no Rio Santa Rita, Nível previsto: {nivel_previsto} metros")

    else :
        print(f"Grande risco de alagamento no Rio Santa Rita, Nível previsto: {nivel_previsto} metros ")


def previsoes():
    while True:
        try:
            print('''1- Previsão do Rio Embu-Guaçu
2- Previsão do Rio Santa Rita''')
            opcao = int(input("Escolha uma opção: "))
            print("\n")
            if opcao <= 0 or opcao > 3:
                print("\n")
                raise VerificaError
            if opcao == 1:
                chuva_prevista = float(input("Milímetros previstos: "))
                preverEmbu(chuva_prevista)
            if opcao == 2:
                chuva_prevista = float(input("Milímetros previstos: "))
                preverSanta(chuva_prevista)
            break
        except ValueError:
            print("O valor informado não é um número \n")
        except VerificaError:
                print("Digite apenas as opções exibidas em tela \n")

def enchente():
    print('''Mantenha-se informado:
Fique atento às previsões meteorológicas e aos alertas de enchentes emitidos pelas autoridades locais.
Tenha um rádio à pilha ou um dispositivo móvel carregado para receber atualizações de emergência.
          
Planeje com antecedência: 
Crie um plano de evacuação para você e sua família, identificando rotas seguras para deixar a área em caso de enchente.
Monte um kit de emergência com alimentos não perecíveis, água, medicamentos, lanternas, pilhas, cobertores e outros suprimentos essenciais.
Mantenha documentos importantes, como identidade, certidões, apólices de seguro e registros médicos, em um local seguro e à prova d'água.
          
Evacue, se necessário:
Se as autoridades ordenarem a evacuação da área, siga as instruções imediatamente.
Não tente atravessar enchentes de carro ou a pé, pois as águas rápidas e turbulentas podem ser extremamente perigosas.

Proteja sua casa: 
Eleve os objetos de valor e móveis para áreas mais altas da casa, se possível.
Desligue a eletricidade, o gás e a água para evitar riscos de incêndio e vazamentos.
Utilize sacos de areia ou barreiras temporárias para proteger sua casa de inundações, se disponíveis.
          
Mantenha-se seguro durante a enchente:
Evite áreas inundadas, especialmente ruas e estradas alagadas.
Mantenha-se em um local seguro e elevado, como o andar superior de sua casa ou o telhado.
Não nade ou brinque na água das enchentes, pois elas podem esconder perigos, como correntes fortes e detritos.

Após a enchente:
Espere até que as autoridades declarem que é seguro retornar à área afetada.
Não consuma alimentos ou água contaminados pela enchente.
Avalie os danos à sua propriedade e entre em contato com a companhia de seguros.
''')

    print("Dicas adicionais \n")

    print('''Comunique-se:
Mantenha-se em contato com familiares e amigos para informá-los sobre sua situação e seu paradeiro.
Tenha um plano de comunicação de emergência estabelecido.
        
Esteja preparado para ficar isolado:
Em algumas situações, pode não ser possível evacuar imediatamente. Esteja preparado para ficar em casa por vários dias, se necessário.
Tenha suprimentos adicionais, como alimentos não perecíveis e água, para durar durante um período prolongado.
    
Cuide da saúde mental:
Enfrentar uma enchente pode ser estressante e emocionalmente desafiador. Procure apoio emocional de amigos, familiares ou profissionais de saúde mental, se necessário.
    
Monitore as condições:
Esteja atento ao nível da água e às mudanças nas condições climáticas. As enchentes podem continuar a piorar antes de melhorar.
Escute atentamente as atualizações das autoridades e siga as instruções.
    
Ajude os outros:
Se você estiver seguro e em posição de fazê-lo, ajude vizinhos idosos, pessoas com mobilidade reduzida ou outras pessoas em necessidade.
    
Conheça os procedimentos de resgate:
Familiarize-se com os procedimentos de resgate locais e os números de emergência, caso precise de assistência.\n''')

def psico():
    print('''Aguarde por um instante !
Estamos buscando o melhor profissional para você \n''')

def opinioes():
    with open('./Arquivos/project.txt', 'r') as projeto:
        dados_project = json.load(projeto)
    print("Sua opinião é muito importante para nós !\n")
    project = input("Nos fale sobre o que achou do nosso projeto e a sua experiência com o aplicativo: ")
    dados_project.append(project)
    with open('./Arquivos/project.txt', 'w') as projeto:
        json.dump(dados_project, projeto, indent=4)

    with open('./Arquivos/city.txt', 'r') as cidade:
        dados_city = json.load(cidade)
    city = input("O que você melhoraria atualmente na cidade ?: ")
    dados_city.append(city)
    with open('./Arquivos/city.txt', 'w') as cidade:
        json.dump(dados_city, cidade, indent=4)
    
    print("\n")

def sobre():
    print('''Bem-vindo à Tech Bloom!

Somos uma empresa apaixonada por inovação e comprometida em resolver desafios no Brasil por meio da tecnologia e da pesquisa. Nossa jornada começou com a missão de contribuir para o desenvolvimento do nosso país, enfrentando problemas complexos com abordagens criativas.''')
    
    print('''Visão e Valores

A empresa esta focada em soluções tecnológicas para resolver desafios específicos, como enchentes, e tem um compromisso com o desenvolvimento sustentável e a melhoria da qualidade de vida nas cidades em desenvolvimento. Buscamos liderar na resolução de desafios sociais, econômicos e ambientais, tornando o país mais próspero, igualitário e sustentável.''')
    

    print('''Parceria com Passos Mágicos

Acreditamos que a verdadeira inovação vai além das soluções tecnológicas. É por isso que estamos orgulhosamente associados à ONG Passos Mágicos, uma organização que compartilha nossa paixão por criar impacto positivo nas comunidades em desenvolvimento. Juntos, combinamos nossos conhecimentos em tecnologia e nosso compromisso social para abordar desafios complexos e promover mudanças significativas.''')

    print('''Junte-se a Nós

Estamos empenhados em criar um impacto positivo e duradouro. Se você compartilha de nossa paixão pela tecnologia, inovação e soluções criativas, venha fazer parte da Tech Bloom. Juntos, podemos desencadear mudanças significativas e positivas na sociedade e impulsionar o crescimento do Brasil como um líder global em inovação e desenvolvimento.

O futuro é inovação, e nós estamos prontos para florescer nesse futuro. Junte-se a nós nessa jornada emocionante! \n''')

def menusec():
    '''Menu que será exibido após o login efetuado com sucesso'''
    while True:
        try: 
            print('''1- Previsões
2- O que fazer em uma enchente
3- Psicologia
4- Opiniões
5- Sobre nós''')
            
            opcao = int(input("Escolha uma opção: "))
            print("\n")
            if opcao <= 0 or opcao > 5:
                print("\n")
                raise VerificaError
            
            if opcao == 1:
                previsoes()
            elif opcao == 2:
                enchente()
            elif opcao == 3:
                psico()
            elif opcao == 4:
                opinioes()
            elif opcao == 5:
                sobre()
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
                    menusec()
                    break
                else:
                    print("Login invalido")
        except ValueError:
            print("O valor informado não é um número \n")
        except VerificaError:
                print("Digite apenas as opções exibidas em tela \n")


menu()