import json
import os
import platform


def limpar_tela():
    """
    Limpa a tela do terminal, independentemente do sistema operacional.
    """
    # Verifica o sistema operacional e executa o comando apropriado para limpar o terminal
    if platform.system() == "Windows":
        os.system('cls')  # Comando para Windows
    else:
        os.system('clear')  # Comando para Linux e macOS


def inicializar_arquivos():
    """
    Cria o arquivo JSON de contas caso ele não exista, garantindo que o programa
    sempre tenha onde armazenar os dados do usuário.
    """
    # Verifica se o arquivo de contas não existe
    if not os.path.exists(CONTAS_USUARIOS):
        # Cria o arquivo com uma lista vazia, permitindo que usuários sejam adicionados depois
        with open(CONTAS_USUARIOS, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=4)


def salvar_dados(arquivo, dado):
    """
    Adiciona um novo dicionário ao arquivo JSON especificado, mantendo os dados anteriores.
    """

    # Abre o arquivo para leitura e carrega os dados existentes
    with open(arquivo, 'r') as f:
        dados_existentes = json.load(f)

    # Adiciona o novo dado (um dicionário) à lista de registros já existentes
    dados_existentes.append(dado)

    # Abre o arquivo novamente em modo de escrita para sobrescrever com os dados atualizados
    with open(arquivo, 'w') as f:
        json.dump(dados_existentes, f, indent=4)


def dar_boas_vindas():
    """
    Mostra a tela inicial do programa, oferecendo três opções ao usuário:
    - Fazer login;
    - Cadastrar uma nova conta;
    - Sair do programa.
    """
    print("Bem-vindo ao FeiFood\n")
    print("Selecione uma das opções:")
    
    # Loop que mantém o menu até o usuário escolher uma opção válida
    while True:
        print("[1] Logar / [2] Cadastrar / [3] Sair do Programa")
        opcao_inicial = input("\n> ")
        limpar_tela()

        # Redireciona conforme a escolha do usuário
        if opcao_inicial == "1":
            login()
            break
        elif opcao_inicial == "2":
            cadastrar_usuario()
            break
        elif opcao_inicial == "3":
            exit()  # Encerra o programa imediatamente
        else:
            # Mensagem de erro para entradas inválidas
            print("Por favor, escolha uma das opções corretamente.\n")



def cadastrar_usuario():
    """
    Realiza o cadastro de um novo usuário no sistema.

    O usuário deve escolher um nome e senha (mínimo de 8 caracteres cada).
    Caso o nome de usuário já exista, será solicitado outro.
    Após o cadastro, o usuário informa nome, CEP e número residencial,
    e os dados são salvos no arquivo JSON de contas.
    """

    print("Área de cadastro.\n")
    print("Digite um usuário e senha para entrar na conta:")
    print("(Seu usuário e senha devem conter no mínimo 8 caracteres)\n")

    # Lê todas as contas já existentes
    with open(CONTAS_USUARIOS, 'r') as ler_contas:
        contas_usuarios = json.load(ler_contas)

    # Loop até o cadastro ser válido
    while True:
        cadastrar_usuario = input("Usuário: ")

        # Verifica se o usuário já existe
        usuario_ja_existe = False
        for listar_usuario in contas_usuarios:
            if cadastrar_usuario == listar_usuario["Usuario"]:
                print("\nEste usuário já existe!")
                usuario_ja_existe = True
                break

        # Se já existir, volta para o início do loop
        if usuario_ja_existe:
            continue

        cadastrar_senha = input("Senha: ")

        # Verifica tamanho mínimo de usuário e senha
        if len(cadastrar_usuario) < 8 or len(cadastrar_senha) < 8:
            limpar_tela()
            print("Usuário e senha devem ter pelo menos 8 caracteres.\n")
        else:
            break

    # Salva informações iniciais da conta
    conta_usuario["Usuario"] = cadastrar_usuario
    conta_usuario["Senha"] = cadastrar_senha

    print("\nVamos criar o seu perfil.")
    nome = input("Nome: ")

    # Solicita CEP e número residencial, garantindo que sejam números
    while True:
        try:
            print("\nDigite o seu CEP:")
            cep = int(input("CEP: "))

            print("\nDigite o seu número residencial:")
            n_residencia = int(input("Número: "))
            break
        except ValueError:
            limpar_tela()
            print("Você deve digitar apenas números.\n")

    conta_usuario["Nome"] = nome
    conta_usuario["CEP"] = cep
    conta_usuario["Numero_Residencial"] = n_residencia

    # Salva a conta no arquivo JSON
    salvar_dados(CONTAS_USUARIOS, conta_usuario)
    limpar_tela()
    menu()



def login():
    """
    Realiza o login de um usuário já cadastrado.

    Lê o arquivo de contas e verifica se o usuário e senha correspondem a algum registro.
    Caso o login falhe, o usuário pode tentar novamente ou voltar ao menu inicial.
    """

    with open(CONTAS_USUARIOS, 'r') as ler_contas:
        listar_usuarios_senhas = json.load(ler_contas)

    limpar_tela()
    print("\nÁrea de Login\n")

    logar_usuario = input("Digite o seu usuário:\n> ")
    logar_senha = input("Digite a sua senha:\n> ")

    usuario_encontrado = False

    # Percorre as contas para verificar se existe correspondência
    for conta in listar_usuarios_senhas:
        if conta["Usuario"] == logar_usuario and conta["Senha"] == logar_senha:
            limpar_tela()
            print("Login realizado com sucesso!")
            usuario_encontrado = True

    # Caso não encontre, oferece opções ao usuário
    if usuario_encontrado == False:
        print("\nUsuário e/ou senha não encontrados.")
        print("\nDeseja voltar ao início?")
        print("[1] Sim")
        print("[2] Tentar novamente\n")

        while True:
            escolher = input("> ")
            if escolher == "1":
                limpar_tela()
                dar_boas_vindas()
                break
            elif escolher == "2":
                login()  # Chama recursivamente para tentar novamente
                break
            else:
                print("\nPor favor, escolha uma opção corretamente.")
    else:
        menu()



def menu():
    """
    Exibe o menu principal após o login, permitindo:
    - Fazer pedido;
    - Sair da sessão;
    - Encerrar o programa.
    """

    print("Você está logado.\n")
    print("Menu Principal")
    print("Escolha uma das opções:\n")

    print("[1] Fazer Pedido")
    print("[2] Sair da Sessão")
    print("[3] Sair do Programa")

    # Mantém o menu até o usuário escolher uma opção válida
    while True:
        escolher_opcao = input("\n> ")

        if escolher_opcao == "1":
            limpar_tela()
            forma_escolher_pedido()
            break
        elif escolher_opcao == "2":
            dar_boas_vindas()
            break
        elif escolher_opcao == "3":
            exit()
        else:
            print("\nPor favor, escolha uma opção corretamente.")


def forma_escolher_pedido():
    """
    Permite ao usuário escolher como fará seu pedido:
    - Escolher restaurante e ver o cardápio;
    - Buscar alimento por nome;
    - Acessar o carrinho de compras.
    """

    print("Escolha uma das opções abaixo:")
    print("(Digite 's' para voltar.)\n")

    print("[1] Escolher Restaurante")
    print("[2] Buscar o Alimento")
    print("[3] Acessar Meu Carrinho")

    # Mantém o loop até o usuário escolher ou voltar
    while True:
        escolher_opcao = input("> ")

        if escolher_opcao == "s":
            limpar_tela()
            menu()
            break
        elif escolher_opcao == "1":
            escolher_restaurante()
            break
        elif escolher_opcao == "2":
            limpar_tela()
            buscar_pelo_nome()
            break
        elif escolher_opcao == "3":
            limpar_tela()
            acessar_carrinho()
            break
        else:
            print("\nEscolha uma opção corretamente.")



def buscar_pelo_nome():
    """
    Permite ao usuário pesquisar um alimento pelo nome em todos os restaurantes disponíveis.
    Exibe os cardápios completos, realiza a busca pelo nome do alimento e oferece a opção de 
    adicioná-lo ao carrinho, caso encontrado.
    """

    with open(RESTAURANTES, 'r') as f:
        restaurantes = json.load(f)  # Carrega os dados do arquivo JSON com os restaurantes

    print("Cardápio:\n")

    # Mostra todos os alimentos disponíveis em todos os restaurantes
    for restaurante in restaurantes:
        for alimento in restaurante["Alimentos"]:
            for chave, valor in alimento.items():
                print(f"{chave}: {valor}")
            print("-" * 30)

    while True:
        print("\nDigite o nome do alimento que deseja buscar: ")
        print("(Digite 's' para voltar.)\n")
        busca = input("> ").lower()  # Recebe o nome do alimento e converte para minúsculas
        
        if busca == "s":
            limpar_tela()
            forma_escolher_pedido()  # Retorna ao menu anterior
            break

        encontrado = False  # Flag para verificar se o alimento foi encontrado
        for restaurante in restaurantes:
            for alimento in restaurante["Alimentos"]:
                if alimento["Nome"].lower() == busca:
                    print(f"\nEncontrado no restaurante {restaurante['Restaurante']}!\n")
                    for chave, valor in alimento.items():
                        print(f"{chave}: {valor}")
                    encontrado = True  # Marca como encontrado
        
        # Caso o alimento não seja encontrado, repete o processo
        if not encontrado:
            print("\nAlimento não encontrado em nenhum restaurante.")
            continue
        else:
            busca = busca.capitalize()  # Ajusta a formatação do nome
            # Pergunta se o usuário deseja adicionar o item ao carrinho
            print("\nDeseja adicioná-lo ao carrinho?")
            print("[1] Sim")
            print("[2] Não")

            while True:
                sim_nao = input("\n> ")
                if sim_nao == "1":
                    carrinho.append(busca)  # Adiciona o alimento ao carrinho
                    print(f"\n{busca} adicionado ao carrinho.")
                    break
                elif sim_nao == "2":
                    print(f"\n{busca} não foi adicionado.")
                    break
                else:
                    print("\nDigite uma opção corretamente.")
                    continue


def escolher_restaurante():
    """
    Exibe a lista de restaurantes disponíveis e permite que o usuário selecione um deles 
    pelo número. Após a escolha, o cardápio do restaurante é aberto para seleção de alimentos.
    """

    limpar_tela()
    print("Escolha um restaurante pelo número:")
    print("(Digite 's' para sair)\n")

    with open(RESTAURANTES, 'r') as f:
        restaurantes = json.load(f)  # Carrega os dados dos restaurantes

    # Exibe todos os restaurantes com seus respectivos índices
    for indice_restaurante, r in enumerate(restaurantes):
        print(f"[{indice_restaurante}] {r['Restaurante']}")

    while True:
        escolher_restaurante = input("\n> ")
        if escolher_restaurante == "s":
            limpar_tela()
            forma_escolher_pedido()  # Retorna ao menu anterior
            break
        try:
            # Converte a escolha em número e abre o cardápio do restaurante escolhido
            escolher_restaurante = int(escolher_restaurante)
            escolher_alimento_por_restaurante(escolher_restaurante)
            break
        except (IndexError, ValueError):
            print("\nPor favor, digite o número do restaurante corretamente.")


def escolher_alimento_por_restaurante(indice_alimento):
    """
    Exibe o cardápio de um restaurante específico com base no índice informado. 
    Permite que o usuário selecione um alimento e o adicione ao carrinho.
    """

    limpar_tela()
    alimento_especifico = int(indice_alimento)  # Guarda o índice original do restaurante
    indice_alimento = int(indice_alimento)
    with open(RESTAURANTES, 'r') as f:
        restaurantes = json.load(f)  # Carrega todos os restaurantes

    print("Cardápio:\n")

    # Exibe todos os alimentos do restaurante selecionado
    for i, alimento in enumerate(restaurantes[indice_alimento]["Alimentos"]):
        print(f"[{i}]")  # Mostra o índice do alimento
        for chave, valor in alimento.items():
            print(f"{chave}: {valor}")
        print("-" * 30)
        indice_alimento += 1  # Incrementa para percorrer os alimentos (não afeta o loop diretamente)

    print("\nEscolha um alimento pelo indice para adicionar ao seu carrinho:")
    print("(Digite 's' para voltar.)\n")

    while True:
        fazer_pedido = input("> ")
        if fazer_pedido.lower() == "s":
            limpar_tela()
            forma_escolher_pedido()  # Volta ao menu anterior
            break
        try:
            # Converte o índice escolhido e adiciona o alimento correspondente ao carrinho
            indice_especifico = int(fazer_pedido)
            item = restaurantes[alimento_especifico]["Alimentos"][indice_especifico]["Nome"]
            carrinho.append(item)
            print(f"{item} adicionado ao carrinho.")
        except (IndexError, ValueError):
            # Trata erros caso o usuário digite um índice inválido
            print("\nPor favor, selecione um alimento corretamente.")

def mostrar_preco_carrinho():
    """
    Calcula e exibe o preço total dos itens no carrinho.
    Para cada alimento presente no carrinho, busca o preço correspondente
    no arquivo 'restaurantes.json' e soma ao total.
    """

    total = 0.0  # Acumulador do valor total

    # Abre o arquivo de restaurantes
    with open(RESTAURANTES, 'r') as f:
        restaurantes = json.load(f)

    # Percorre cada alimento no carrinho
    for alimento_carrinho in carrinho:
        for restaurante in restaurantes:
            for alimento in restaurante["Alimentos"]:
                if alimento["Nome"] == alimento_carrinho:
                    total += alimento["Preco"]  # Soma o preço ao total

    # Mostra o valor final do carrinho
    print(f"\nValor total do carrinho: R$ {total:.2f}")


def acessar_carrinho():
    """
    Exibe o conteúdo atual do carrinho do usuário e oferece opções para:
    - Finalizar a compra;
    - Editar (remover itens do carrinho);
    - Voltar para adicionar mais alimentos.
    Caso o carrinho esteja vazio, permite apenas retornar ao menu principal.
    """

    print("Meu Carrinho:\n")
    print(*carrinho, sep=", ")  # Exibe os itens do carrinho separados por vírgula
    mostrar_preco_carrinho()
    
    # Se o carrinho contiver itens
    if len(carrinho) > 0:

        print("\nO que deseja fazer?")
        print("[1] Finalizar Compra")
        print("[2] Editar Carrinho")
        print("[3] Voltar")

        while True:
            finalizar_ou_nao = input("\n> ")

            # Opção de finalizar compra
            if finalizar_ou_nao == "1":
                limpar_tela()
                finalizar_compra()
                break

            # Opção de editar o carrinho (remover itens)
            elif finalizar_ou_nao == "2":
                limpar_tela()
                while True:
                    print("Escolha um alimento que deseja excluir:")
                    print("(Digite 's' para voltar)\n")

                    # Exibe cada item com seu índice
                    for indice, alimento in enumerate(carrinho):
                        print(f"[{indice}] {alimento}")

                    excluir_alimento = input("> ")

                    # Retorna ao carrinho se o usuário quiser sair
                    if excluir_alimento == "s":
                        limpar_tela()
                        acessar_carrinho()
                        break

                    try:
                        excluir_alimento = int(excluir_alimento)  # Converte o índice informado
                        carrinho.pop(excluir_alimento)  # Remove o item escolhido
                    except (ValueError, IndexError):
                        print("\nDigite uma opção correta.")

            # Voltar para o menu de escolha de pedidos
            elif finalizar_ou_nao == "3":
                limpar_tela()
                forma_escolher_pedido()
                break
            else:
                print("\nDigite uma opção corretamente.")

    # Caso o carrinho esteja vazio
    else:
        print("\n[1] Voltar ao Menu.")
        digitar_um = input("> ")
        if digitar_um == "1":
            limpar_tela()
            menu()


def finalizar_compra():
    """
    Realiza o processo de finalização da compra:
    - Exibe opções de pagamento;
    - Confirma o método escolhido;
    - Permite avaliar o pedido ou retornar ao menu principal.
    Após finalizar, o carrinho é esvaziado.
    """

    print("Hora de finalizar a compra!\n")
    print("Qual será o seu metodo de pagamento?")
    print("(O pagamento será realizado com o entregador)\n")

    print("[1] Cartão de Crédito")
    print("[2] Cartão de Débito")
    print("[3] Pix")
    print("[4] Dinheiro")

    while True:
        escolher_pagamento = input("> ")

        # Verifica se a opção de pagamento é válida
        if escolher_pagamento in ["1", "2", "3", "4"]:

            limpar_tela()
            print("Forma de pagamento escolhido com sucesso!")
            print("Estamos preparando o seu pedido e logo estará a caminho!")
            print("Tenha um bom apetite!")

            print("\nO que deseja fazer?")
            print("[1] Avaliar Pedido")
            print("[2] Voltar ao Menu")

            # Após o pagamento, o usuário pode avaliar o pedido ou voltar
            while True:
                avaliar_ou_nao = input("> ")

                if avaliar_ou_nao == "1":
                    avaliar_pedido()
                    break
                elif avaliar_ou_nao == "2":
                    carrinho.clear()  # Limpa o carrinho após a finalização
                    limpar_tela()
                    menu()
                    break
                else:
                    print("Por favor, escolha uma opção corretamente.")
            break
        else:
            print("Por favor, escolha uma opção corretamente.")



def avaliar_pedido():
    """
    Função responsável por solicitar ao usuário uma avaliação (de 0 a 5) para cada alimento presente no carrinho.
    Cada alimento é avaliado uma única vez, mesmo que apareça mais de uma vez no carrinho, pois duplicatas são removidas.
    Após receber as avaliações, a função atualiza a média simples de cada alimento no arquivo JSON de restaurantes
    e salva as modificações. Por fim, limpa o carrinho e retorna ao menu principal.
    """

    # Converte o carrinho em um conjunto para eliminar alimentos repetidos
    alimentos_unicos = list(set(carrinho))
    
    # Abre o arquivo de restaurantes e carrega os dados em memória
    with open(RESTAURANTES, 'r') as f:
        restaurantes = json.load(f)
    
    # Itera sobre cada alimento único do carrinho
    for alimento_nome in alimentos_unicos:
        while True:
            try:
                # Solicita nota de 0 a 5 para o alimento
                avaliacao = float(input(f"Avalie '{alimento_nome}' de 0 a 5: "))
                if 0 <= avaliacao <= 5:
                    break  # Sai do loop se a avaliação for válida
                else:
                    print("Digite um número entre 0 e 5.")
            except ValueError:
                # Captura erro caso o usuário digite algo que não seja número
                print("Digite um número válido.")
        
        # Procura o alimento no JSON e atualiza sua avaliação
        for restaurante in restaurantes:
            for alimento in restaurante["Alimentos"]:
                if alimento["Nome"] == alimento_nome:
                    # Incrementa o número de avaliações do alimento
                    alimento["Quantidade_Avaliacoes"] += 1
                    # Atualiza a média de avaliação (forma simplificada)
                    alimento["Avaliacao"] = (alimento["Avaliacao"] + avaliacao) / alimento["Quantidade_Avaliacoes"]
    
    # Salva as alterações no arquivo de restaurantes
    with open(RESTAURANTES, 'w') as f:
        json.dump(restaurantes, f, indent=4)
    
    # Limpa a tela e exibe mensagem de sucesso
    limpar_tela()
    print("\nAvaliações registradas com sucesso!")
    print("Voltando ao menu...\n")
    # Esvazia o carrinho após as avaliações
    carrinho.clear()

    # Retorna ao menu principal
    menu()


# Caminhos dos arquivos JSON utilizados pelo sistema
CONTAS_USUARIOS = "contas_usuarios.json"
RESTAURANTES = "restaurantes.json"

# Estrutura base de uma conta de usuário
conta_usuario = {
    "Usuario": "",
    "Senha": "",
    "Nome": "",
    "CEP": "",
    "Numero_Residencial": ""
}

# Lista que armazena temporariamente os alimentos selecionados pelo usuário
carrinho = []

# Inicializa o sistema, exibe a mensagem de boas-vindas e abre o menu principal
inicializar_arquivos()
dar_boas_vindas()