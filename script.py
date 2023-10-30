'''
1ESPW

Fabrício Saavedra - 97631
Guilherme Akio - 98582
Guilherme Morais - 551981
Matheus Motta - 550352
Vinicius Buzato - 99125
'''

from datetime import datetime, date
import sys #import para uso de sys.exit()

def split():
    print('-'*30)

def error():
    split()
    print('Opção inexistente!')
    split()

#Função para imprimir o a marca da vinheria agnello
def logo():
    print("")
    print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")                                                 
    print(' _____ _     _           _        _____             _ _       ')
    print('|  |  |_|___| |_ ___ ___|_|___   |  _  |___ ___ ___| | |___   ')
    print("|  |  | |   |   | -_|  _| | .'|  |     | . |   | -_| | | . |  ")
    print(" \___/|_|_|_|_|_|___|_| |_|__,|  |__|__|_  |_|_|___|_|_|___|  ")
    print("                                       |___|                  ")   
    print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")

def cp1():
    #vinhos
    a = "1. Merlot"
    b = "2. Cabernet Sauvignon"
    c = "3. Chardonnay"
    d = "4. Pinot noir"
    e = "5. Malbec"
    #valor do vinho
    A = 59.90
    B = 69.90
    C = 79.90
    D = 89.90
    E = 99.90
    #variavel de quantia
    c3 = 0
    d3 = 0
    e3 = 0
    f3 = 0
    g3 = 0
    #variavel de valor
    c4 = 0
    d4 = 0
    e4 = 0
    f4 = 0
    g4 = 0
    #Area de boas vindas e menu
    print("Boas vindas a Vinheria Agnello!")
    maioridade = int(input("Antes de começar, diga a sua idade:"))
    if maioridade < 18:
        print("Desculpe, voce nao tem permissao para entrar em nossa loja, a venda para menores de 18 anos é proibida.")
    else:
        while True:
            a1 = str(input("O que deseja fazer em nosso site?(compras/carrinho/menu/sair)"))
            if a1 == "sair":
                break
            elif a1 == "compras": #sistema de compras e quantidade
                print("Em nossa cartela temos:")
                print(a)
                print(b)
                print(c)
                print(d)
                print(e)
                while True:
                    c1 = str(input("Qual voce deseja comprar?(1/2/3/4/5):"))
                    if c1 == "1": # Compra vinho merlot
                        c2 = str(input("O vinho Merlot tem um valor de R$59,90, comprar este?(sim/nao)"))
                        if c2 == "sim":
                            c3 = int(input("Quantas garrafas voce quer comprar?"))
                            x = A
                            c4 = float(c3) * x
                            print("O valor final sera %.2f voce pode conferir no seu carrinho" % c4)
                            print("Voltando para o menu")
                            break
                        elif c2 == "nao":
                            print("Voltando para o menu")
                            break
                        else:
                            print("Erro insira, insira apenas 'sim' ou 'nao' ")
                            continue
                    elif c1 == "2": # Compra vinho Cabernet
                        c2 = str(input("O vinho Cabernet Sauvignon tem um valor de R$69,90, comprar este?(sim/nao)"))
                        if c2 == "sim":
                            d3 = int(input("Quantas garrafas voce quer comprar?"))
                            x = B
                            d4 = float(d3) * x
                            print("O valor final sera %.2f voce pode conferir no seu carrinho" % d4)
                            print("Voltando para o menu")
                            break
                        elif c2 == "nao":
                            print("Voltando para o menu")
                            break
                        else:
                            print("Erro insira, insira apenas 'sim' ou 'nao' ")
                            continue
                    elif c1 == "3": # Compra vinho Chardonnay
                        c2 = str(input("O vinho Chardonnay tem um valor de R$79,90, comprar este?(sim/nao)"))
                        if c2 == "sim":
                            e3 = int(input("Quantas garrafas voce quer comprar?"))
                            x = C
                            e4 = float(e3) * x
                            print("O valor final sera %.2f voce pode conferir no seu carrinho" % e4)
                            print("Voltando para o menu")
                            break
                        elif c2 == "nao":
                            print("Voltando para o menu")
                            break
                        else:
                            print("Erro insira, insira apenas 'sim' ou 'nao' ")
                            continue
                    elif c1 == "4": # Compra vinho Pinot noir
                        c2 = str(input("O vinho Pinot noir tem um valor de R$89,90, comprar este?(sim/nao)"))
                        if c2 == "sim":
                            f3 = int(input("Quantas garrafas voce quer comprar?"))
                            x = D
                            f4 = float(f3) * x
                            print("O valor final sera %.2f voce pode conferir no seu carrinho" % f4)
                            print("Voltando para o menu")
                            break
                        elif c2 == "nao":
                            print("Voltando para o menu")
                            break
                        else:
                            print("Erro insira, insira apenas 'sim' ou 'nao' ")
                            continue
                    elif c1 == "5": # Compra vinho Malbec
                        c2 = str(input("O vinho Malbec tem um valor de R$99,90, comprar este?(sim/nao)"))
                        if c2 == "sim":
                            g3 = int(input("Quantas garrafas voce quer comprar?"))
                            x = E
                            g4 = float(g3) * x
                            print("O valor final sera %.2f voce pode conferir no seu carrinho" % e4)
                            print("Voltando para o menu")
                            break
                        elif c2 == "nao":
                            print("Voltando para o menu")
                            break
                        else:
                            print("Erro insira, insira apenas 'sim' ou 'nao' ")
                            continue
            elif a1 == "carrinho": #sistema de carrinho
                    print("Carrinho:")
                    if c3 ==0 and d3 == 0 and e3 == 0 and f3 == 0 and g3 == 0:
                        print("o seu carrinho esta vazio")
                    else:
                        z4 = c4 + d4 + e4 + f4 + g4
                        if c3 > 0:
                            print("%d Merlot com valor de %.2f" %(c3,c4))
                        if d3 > 0:
                            print("%d Cabernet Sauvignon com valor de %.2f" %(d3,d4))
                        if e3 > 0:
                            print("%d Chardonnay com valor de %.2f" %(e3,e4))
                        if f3 > 0:
                            print("%d Pinot noir com valor de %.2f" %(f3,f4))
                        if g3 > 0:
                            print("%d Malbec com valor de %.2f" %(g3,g4))
                        if z4 > 0:
                            print("Valor final %.2f(frete calculado apos os dados)" %z4)
                            while True: #valor minimo para compra 100 reais
                                if z4 > 0 and z4 < 100:
                                    print("O valor minimo para fazer uma compra é R$100")
                                    break
                                pagamento = str(input("Deseja seguir com o pagamento?(sim/nao)")) #checkout
                                if pagamento == "sim":
                                    print("Ok vamos prosseguir, para isso precisamos de alguns dados seus")
                                    while True: #verificação de dados
                                        nome = str(input("Nome completo:"))
                                        idade = str(input("Idade:"))
                                        endereco = str(input("Cep:"))
                                        entrega = str(input("Endereço que deve ser entregue:"))
                                        print("Ok agora confira os seus dados e da compra:")
                                        print(nome)
                                        print(idade)
                                        print(endereco)
                                        print(entrega)
                                        if c3 > 0:
                                            print("%d Merlot com valor de %.2f" % (c3, c4))
                                        if d3 > 0:
                                            print("%d Cabernet Sauvignon com valor de %.2f" % (d3, d4))
                                        if e3 > 0:
                                            print("%d Chardonnay com valor de %.2f" % (e3, e4))
                                        if f3 > 0:
                                            print("%d Pinot noir com valor de %.2f" % (f3, f4))
                                        if g3 > 0:
                                            print("%d Malbec com valor de %.2f" % (g3, g4))
                                        if z4 > 0 and z4 < 200:
                                            print("Valor final com frete(R$10.00): %.2f" % (z4+10))
                                            validacao = str(input("Os dados estao corretos?(sim/nao/sair)"))
                                            if validacao == "sim": #finalizaçao do programa e compra
                                                print("Ok,finalizando sua compra")
                                                print(".")
                                                print(".")
                                                print(".")
                                                print(".")
                                                print("Tudo pronto! Sua entrega deve chegar nos proximo 6 dias úteis.")
                                                print("Agradecemos a preferencia por comprar na Agnello! Volte sempre")
                                                sys.exit() #finaliza o programa testado em pycharm
                                            elif validacao == "nao":
                                                print("Voltando para correção dos dados")
                                                pass
                                            elif validacao == "sair":
                                                print("Voltando para o carrinho:")
                                                print("Carrinho:")
                                                if c3 > 0:
                                                    print("%d Merlot com valor de %.2f" % (c3, c4))
                                                if d3 > 0:
                                                    print("%d Cabernet Sauvignon com valor de %.2f" % (d3, d4))
                                                if e3 > 0:
                                                    print("%d Chardonnay com valor de %.2f" % (e3, e4))
                                                if f3 > 0:
                                                    print("%d Pinot noir com valor de %.2f" % (f3, f4))
                                                if g3 > 0:
                                                    print("%d Malbec com valor de %.2f" % (g3, g4))
                                                if z4 > 0:
                                                    print("Valor final %.2f(frete calculado apos os dados)" % z4)
                                                break
                                            else:
                                                print("Erro, por favor insira apenas 'sim' ou 'nao', voltando para os dados")
                                                continue
                                        if z4 > 200:
                                            print("Valor final (Acima de R$200, Frete gratis!): %.2f" % z4)
                                            validacao = str(input("Os dados estao corretos?(sim/nao/sair)"))
                                            if validacao == "sim": #finalizaçao do programa e compra
                                                print("Ok,finalizando sua compra")
                                                print(".")
                                                print(".")
                                                print(".")
                                                print(".")
                                                print("Tudo pronto! Sua entrega deve chegar nos proximo 6 dias úteis.")
                                                print("Agradecemos a preferencia por comprar na Agnello! Volte sempre")
                                                sys.exit() #finaliza o programa testado em pycharm
                                            elif validacao == "nao":
                                                print("Voltando para correção dos dados")
                                                pass
                                            elif validacao == "sair":
                                                print("Voltando para o carrinho:")
                                                print("Carrinho:")
                                                if c3 > 0:
                                                    print("%d Merlot com valor de %.2f" % (c3, c4))
                                                if d3 > 0:
                                                    print("%d Cabernet Sauvignon com valor de %.2f" % (d3, d4))
                                                if e3 > 0:
                                                    print("%d Chardonnay com valor de %.2f" % (e3, e4))
                                                if f3 > 0:
                                                    print("%d Pinot noir com valor de %.2f" % (f3, f4))
                                                if g3 > 0:
                                                    print("%d Malbec com valor de %.2f" % (g3, g4))
                                                if z4 > 0:
                                                    print("Valor final %.2f(frete calculado apos os dados)" % z4)
                                                break
                                            else:
                                                print("Erro, por favor insira apenas 'sim' ou 'nao'volando para os dados")
                                                continue
                                elif pagamento == "nao":
                                    print("Retornando ao menu")
                                    break
                                else:
                                    print("Erro digite sim ou nao")
            elif a1 == "menu":
                continue   #sintaxe "continue" e "pass" buscada na internet para poder recomeçar o loop
            else:
                print("Erro, insira uma opção valida")

def cp2():
    #Dicionário com os itens do estoque
    estoque = {
        'rolhas': 48,
        'garrafas': 48,
        'rotulos': 48,
        'caixas': 6,
    }

    #Dicionário para o histórico do estoque
    historico_estoque = {
        'rolhas': [48],
        'garrafas': [48],
        'rotulos': [48],
        'caixas': [6]
    }

    #Lista de pedidos dos clientes
    pedidos_clientes = []

    #Variáveis para cálculo do frete
    preco_frete_fixo = 10.00
    taxa_preparacao_percentual = 0.10
    taxa_preparacao_fixa = 10.00

    #Função para validação dos dados inseridos de forma inválida
    def opcao_invalida():
        print("Opção inválida, por favor digite conforme solicitado!")

    #Função para exibir os items em estoque
    def exibir_estoque():
        print("Estoque:")
        for item, quantidade in estoque.items():
            print(f"{item.capitalize()}: {quantidade}")

    #Função para atualizar os items em estoque
    def registrar_entrada_itens():
        while True:
            print("Itens disponíveis no estoque:")
            for item in estoque:
                print(item.capitalize())
            
            item_escolhido = input("\nEscolha o item que deseja adicionar ou digite 'parar' para sair (escreva o nome do item): ").lower()
            
            if item_escolhido == 'parar':
                atualizar_historico_estoque()
                break
            
            if item_escolhido in estoque:
                while True:
                    try: 
                        quantidade_adicionada = int(input(f"Digite a quantidade de {item_escolhido} a ser adicionada: "))
                        estoque[item_escolhido] += quantidade_adicionada
                        print(f"Itens adicionados ao estoque!")
                        print("")
                        break
                    except ValueError:
                        opcao_invalida()
            else:
                print("Item não encontrado. Por favor, escolha um item válido ou digite 'parar' para sair.")
                print("")

    #Função para atualizar histórico do estoque
    def atualizar_historico_estoque():
        for item in estoque:
            historico_estoque[item].append(estoque[item])

    #Função para realização do pedido 
    def realizar_pedido():
        garrafas_disponiveis = min(estoque['garrafas'], estoque['rolhas'], estoque['rotulos'])
        
        print(f"Garrafas prontas disponíveis: {garrafas_disponiveis}")
        
        while True:
            tipo_pedido = input("Deseja comprar uma CAIXA (6 ou 12) ou GARRAFAS individuais? (Escreva caixa/garrafas) ").lower()
            if tipo_pedido == 'caixa':
                try:
                    tipo_caixa = int(input("Digite o tipo de caixa (6 ou 12): "))
                    caixas_disponiveis = estoque['caixas']         
                    if tipo_caixa == 6 or tipo_caixa == 12:
                        quantidade_caixas = int(input(f"Quantas caixas de {tipo_caixa} garrafas deseja comprar? "))
                        garrafas_pedido = tipo_caixa * quantidade_caixas
                        
                        if caixas_disponiveis <= (caixas_disponiveis * quantidade_caixas) and garrafas_pedido <= garrafas_disponiveis:
                            estoque['garrafas'] -= garrafas_pedido
                            estoque['caixas'] -= quantidade_caixas
                            estoque['rolhas'] -= garrafas_pedido
                            estoque['rotulos'] -= garrafas_pedido

                            cep = input("Digite o CEP para entrega (Exemplo: 00000-000): ")
                            data_entrega = input("Digite a data desejada para entrega (Exemplo: DD/MM/AAAA): ")
                            pedido_atual = (garrafas_pedido, quantidade_caixas, cep, data_entrega)
                            pedidos_clientes.append(pedido_atual)
                            atualizar_historico_estoque()
                            print('')
                            print("Pedido realizado com sucesso!")
                            print('')
                            print("Pedido Atual:")
                            listar_pedido(pedido_atual)
                            break
                        else:
                            print("Estoque insuficiente para atender ao pedido.")
                            break
                    else:
                        print("Tipo de caixa inválido.")
                except:
                    opcao_invalida()
            elif tipo_pedido == 'garrafas':
                try:
                    garrafas_pedido = int(input("Quantas garrafas individuais deseja comprar? "))
                    
                    if garrafas_pedido <= garrafas_disponiveis:
                        estoque['garrafas'] -= garrafas_pedido
                        estoque['rolhas'] -= garrafas_pedido
                        estoque['rotulos'] -= garrafas_pedido
                        cep = input("Digite o CEP para entrega (Exemplo: 00000-000): ")
                        data_entrega = input("Digite a data desejada para entrega (Exemplo: DD/MM/AAAA): ")
                        pedido_atual = (garrafas_pedido, 0, cep, data_entrega)
                        pedidos_clientes.append(pedido_atual)
                        atualizar_historico_estoque()
                        print("Pedido realizado com sucesso.")
                        print("Pedido Atual:")
                        listar_pedido(pedido_atual)
                        break
                    else:
                        print("Estoque insuficiente para atender ao pedido.")
                        break
                except ValueError:
                    opcao_invalida()
                    break
            else:
                opcao_invalida()

    #Função para o calculo do frete
    def calcular_frete(total_garrafas):
        frete = preco_frete_fixo + (total_garrafas * 10.00) + (sum(p[0] for p in pedidos_clientes) * taxa_preparacao_percentual) + taxa_preparacao_fixa
        return frete

    #Função para listar estoque
    def listar_historico_estoque():
        print("Histórico de Estoque:")
        for item in historico_estoque:
            print(f"Histórico de {item.capitalize()}: {', '.join(map(str, historico_estoque[item]))}")
        print("------------------")

    #Função para listar pedido
    def listar_pedido(pedido):
        total_garrafas = pedido[0]
        frete = calcular_frete(total_garrafas)
        print(f"Pedido: {total_garrafas} garrafas, Entrega CEP {pedido[2]}, Data de Entrega {pedido[3]}, Frete: R${frete:.2f}")
        print("------------------")

    #Função para listar histórico
    def listar_historico_pedidos():
        print("Histórico de Pedidos:")
        for i, pedido in enumerate(pedidos_clientes, start=1):
            total_garrafas = pedido[0]
            frete = calcular_frete(total_garrafas)
            print(f"Pedido {i}: {total_garrafas} garrafas, Entrega CEP {pedido[2]}, Data de Entrega {pedido[3]}, Frete: R${frete:.2f}")
        print("------------------")

    #Menu com estrutura de repetição    
    while True:
        print("\nMenu:")
        print("1 - Registrar Entrada de Itens")
        print("2 - Exibir Estoque")
        print("3 - Realizar Pedido do Cliente")
        print("4 - Histórico de Estoque")
        print("5 - Listar Pedidos Feitos")
        print("6 - Encerrar o Programa")
        
        opcao = input("Digite o número da opção desejada: ")
        print("")
        
        if opcao.isnumeric():
            opcao = int(opcao)
            match opcao:
                case 1:
                    registrar_entrada_itens()
                case 2:
                    exibir_estoque()
                case 3:
                    realizar_pedido()
                case 4:
                    listar_historico_estoque()
                case 5:
                    listar_historico_pedidos()
                case 6:
                    arquivo_estoque = open('relatorio_estoque.txt', 'w')

                    arquivo_estoque.write('Histórico de Estoque:\n\n')
                    for item in historico_estoque:
                        arquivo_estoque.write(f"Histórico de {item.capitalize()}: {', '.join(map(str, historico_estoque[item]))}\n")

                    arquivo_estoque.write('\nHistórico de Pedidos:\n\n')
                    for i, pedido in enumerate(pedidos_clientes, start=1):
                        total_garrafas = pedido[0]
                        frete = calcular_frete(total_garrafas)
                        arquivo_estoque.write(f"Pedido {i}: {total_garrafas} garrafas, Entrega CEP {pedido[2]}, Data de Entrega {pedido[3]}, Frete: R${frete:.2f}\n")

                    arquivo_estoque.close()
                    
                    print("Encerrando o programa.")
                    break
                case _:
                    print("\nOpção inválida. Por favor, escolha uma opção das opções listadas.")
        else:
            print("Opção inválida. Por favor, escolha uma as opções listadas.")

def cp3():
        #Parte a pagar
    nota_fiscal_pagar = []
    nota_fiscal_pagar_paga = []
    cnpj_pagar = []
    cnpj_pago = []
    valor_conta_pagar = []
    valor_conta_pagar_paga = []
    descricao_pagar = []
    descricao_pagar_paga = []

    #Parte a receber
    nota_fiscal_receber = []
    nota_fiscal_receber_paga = []
    cpf_receber = []
    cpf_receber_pago = []
    valor_conta_receber = []
    valor_conta_receber_paga = []
    descricao_receber = []
    descricao_receber_paga = []

    #Calculo contas 
    pagar_total = sum(valor_conta_pagar)
    receber_total = sum(valor_conta_receber_paga)
    saldo_soma = receber_total - pagar_total

    #Função de consulta do saldo geral
    def saldo_geral():
        print('Consultando saldo geral')
        print('')
        print('Total a pagar: R$%s' % pagar_total)
        print('Total a receber: R$%s' % receber_total)
        print('Saldo geral: R$%s' % saldo_soma)
        print('')
        pago = sum(valor_conta_pagar_paga)
        print('Contas já pagas: R$%s' % pago)

    #Mensagem de erro padrão
    def opcao_nao_encontrada():
        print('-'*40)
        print('Opção não encontrada! Tenta novamente!')
        print('-'*40)

    #Inicio do menu
    while True:
        print('Menu Principal')
        print('')
        print('1 - Contas a pagar')
        print('2 - Contas a receber')
        print('3 - Saldo geral')
        print('4 - Sair do programa')
        print('')
        try:
            menu_principal = int(input('Digite o número referente ao local onde quer ir:\n'))
            match menu_principal:
                #Contas a pagar
                case 1:
                    while True:
                        print('Menu de Contas a pagar')
                        print('')
                        print('1 - Inserir nova conta')
                        print('2 - Consultar contas a pagar')
                        print('3 - Consultar saldo geral')
                        print('4 - Voltar ao menu principal')
                        print('')
                        try:
                            menu_pagar = int(input('Digite o número referente ao local onde quer ir:\n'))
                            match menu_pagar:
                                #Nova conta
                                case 1:
                                    #Cadastro
                                    print('Opção selecionada: Inserir nova uma conta')
                                    print('')
                                    nota_fiscalC = int(input('Insira o número da Nota Fiscal: '))
                                    cnpj = int(input('Insira o CNPJ do fornecedor: '))
                                    valor_conta = int(input('Insira o valor total da nota: '))
                                    descricao_notaC = input('Insira uma descrição sobre a nota: ')
                                    while True:
                                        pagamentoC = input('O pagamento da nota já foi efetuado? (sim, não) ').lower() #normalização
                                        if pagamentoC == 'sim':
                                            nota_fiscal_pagar_paga.append(nota_fiscalC)
                                            cnpj_pago.append(cnpj)
                                            valor_conta_pagar_paga.append(valor_conta)
                                            descricao_pagar_paga.append(descricao_notaC)
                                            print('Nota adicionada')
                                            break
                                        elif pagamentoC == 'não' or pagamentoC == 'nao':
                                            nota_fiscal_pagar.append(nota_fiscalC)
                                            cnpj_pagar.append(cnpj)
                                            valor_conta_pagar.append(valor_conta)
                                            descricao_pagar.append(descricao_notaC)
                                            print('Nota adicionada')
                                            break
                                        else:
                                            opcao_nao_encontrada()                                   
                                        print('')
                                #Consulta das contas cadastradas        
                                case 2:
                                    print('Opção selecionada: Consultar contas a pagar')
                                    print('')
                                    print('Contas pagas: ')
                                    for i, nota_pagar in enumerate(nota_fiscal_pagar_paga):
                                        print(f'{i + 1}. Nota fiscal: {nota_pagar}, CNPJ: {cnpj_pago[i]}, Valor: R${valor_conta_pagar_paga[i]}, Descrição: {descricao_pagar_paga[i]}')
                                    print('')
                                    print('Contas a pagar: ')
                                    for i, nota_pagar in enumerate(nota_fiscal_pagar):
                                        print(f'{i + 1}. Nota fiscal: {nota_pagar}, CNPJ: {cnpj_pagar[i]}, Valor: R${valor_conta_pagar[i]}, Descrição: {descricao_pagar[i]}')
                                    print('')
                                    while True:
                                        deseja_pagar = input('Deseja pagar algum deles? (sim/não)')
                                        print('')
                                        if deseja_pagar == 'sim':
                                            try:
                                                opcao = int(input("Digite o número referente a conta que quer pagar: "))
                                                indice = opcao - 1
                                                if indice >= 0 and indice <= len(nota_fiscal_receber):
                                                    nota_fiscal_pagar_paga.append(nota_fiscal_pagar[indice])
                                                    cnpj_pago.append(cnpj_pagar[indice])
                                                    valor_conta_pagar_paga.append(valor_conta_pagar[indice])
                                                    descricao_pagar_paga.append(descricao_pagar[indice])
                                                    valor_pago = nota_fiscal_pagar.pop(indice)
                                                    cnpj_pagar.pop(indice) and valor_conta_pagar.pop(indice) and descricao_pagar.pop(indice)
                                                    print(f"Nota fiscal da conta paga: {valor_pago}")
                                                else:
                                                    opcao_nao_encontrada()
                                            except ValueError:
                                                opcao_nao_encontrada()
                                                print('')
                                            break
                                        elif deseja_pagar == 'não' or deseja_pagar == 'nao':
                                            print('Ok, voltando para o Menu de contas a receber')
                                            break
                                        else:
                                            opcao_nao_encontrada()
                                #Saldo Geral
                                case 3:
                                    print('Opção selecionada: Consultar saldo geral')
                                    print('')
                                    saldo_geral()
                                #Menu
                                case 4:
                                    print('Opção selecionda: Voltar ao menu principal')
                                    print('')
                                    break
                                case _:
                                    opcao_nao_encontrada()
                        except ValueError:
                            opcao_nao_encontrada()
                #Contas a receber
                case 2:
                    while True:
                        print('Menu de contas a receber')
                        print('')
                        print('1 - Inserir nova conta')
                        print('2 - Consultar contas a receber')
                        print('3 - Consultar saldo geral')
                        print('4 - Voltar ao menu principal')
                        print('')
                        try:
                            menu_receber = int(input('Digite o número referente ao local onde quer ir:\n'))
                            match menu_receber:
                            #Nova conta
                                case 1:
                                    print('Opção selecionada: Inserir nova uma conta')
                                    print('')
                                    nota_fiscalR = int(input('Insira o número da Nota Fiscal: '))
                                    cpf = int(input('Insira o CPF do cliente: '))
                                    valor_nota = int(input('Insira o valor total da nota: '))
                                    descricao_notaR = input('Insira uma descrição sobre a nota: ')
                                    nota_fiscal_receber_paga.append(nota_fiscalR)
                                    cpf_receber_pago.append(cpf)
                                    valor_conta_receber_paga.append(valor_nota)
                                    descricao_receber_paga.append(descricao_notaR)
                                    print('Nota adicionada')
                                    break
                                #Consultar contas a receber
                                case 2:
                                    print('Opção selecionada: Consultar contas recebidas')
                                    print('')
                                    print('Contas recebidas: ')
                                    for i, nota_receber in enumerate(nota_fiscal_receber_paga):
                                        print(f'{i + 1}. Nota fiscal: {nota_receber}, CNPJ: {cpf_receber_pago[i]}, Valor: R${valor_conta_receber_paga[i]}, Descrição: {descricao_receber_paga[i]}')
                                    print('')
                                #Saldo geral
                                case 3:
                                    print('Opção selecionada: Consultar saldo geral')
                                    print('')
                                    saldo_geral()
                                #Menu
                                case 4:
                                    print('Opção selecionda: Voltar ao menu principal')
                                    print('')
                                    break
                                case _:
                                    opcao_nao_encontrada()
                        except ValueError:
                            opcao_nao_encontrada()
                #Saldo Geral
                case 3:
                    saldo_geral()

                #Encerramento
                case 4:
                    arquivo_contas = open('relatorio_contas', 'w')

                    arquivo_contas.write('Tabela de contas a pagar:\n\n')
                    for i, nota_pagar in enumerate(nota_fiscal_pagar_paga):
                        arquivo_contas.write(f'{i + 1}. Nota fiscal: {nota_pagar}, CNPJ: {cnpj_pago[i]}, Valor: R${valor_conta_pagar_paga[i]}, Descrição: {descricao_pagar_paga[i]}\n')

                    arquivo_contas.write('\nTabela de contas pagas:\n\n')
                    for i, nota_pagar in enumerate(nota_fiscal_pagar):
                        arquivo_contas.write(f'{i + 1}. Nota fiscal: {nota_pagar}, CNPJ: {cnpj_pagar[i]}, Valor: R${valor_conta_pagar[i]}, Descrição: {descricao_pagar[i]}\n')

                    arquivo_contas.write('\nTabela de contas recebidas:\n\n')
                    for i, nota_receber in enumerate(nota_fiscal_receber_paga):
                        arquivo_contas.write(f'{i + 1}. Nota fiscal: {nota_receber}, CNPJ: {cpf_receber_pago[i]}, Valor: R${valor_conta_receber_paga[i]}, Descrição: {descricao_receber_paga[i]}\n')
                    
                    arquivo_contas.write('\nSaldo geral: R$%s' % saldo_soma)

                    arquivo_contas.close()
            
                    print('Encerrando o programa...')
                    break
                case _:
                    opcao_nao_encontrada()
        except ValueError:
            opcao_nao_encontrada()

def cp4():
    # Inicializar estruturas de dados para armazenar as tarefas
    tarefas = []

    #Função para espaçamento entre retornos do código
    def paragrafo():
        print("")

    # Função para adicionar tarefa
    def adicionar_tarefa():
        global tarefas
        tarefa = {}
        tarefa['descricao'] = input("Descrição da tarefa: ")

        while True:
            try:
                tarefa['data_inicial'] = datetime.strptime(input("Data inicial da tarefa (formato dd/mm/aaaa): "), "%d/%m/%Y").date()
                tarefa['data_inicial'] = tarefa['data_inicial'].strftime("%d/%m/%Y")
                break
            except ValueError:
                error()
                                    
        while True:
            try:
                tarefa['data_final'] = datetime.strptime(input("Data final da tarefa (formato dd/mm/aaaa): "), "%d/%m/%Y").date()
                tarefa['data_final'] = tarefa['data_final'].strftime("%d/%m/%Y")
                if tarefa['data_final'] < tarefa['data_inicial']:
                    print("A data final da nova tarefa não pode ser antes da data inicial, por favor revise sua tarefa")
                else:
                    break
            except ValueError:
                error()

        while True:
            try:
                tarefa['completude_real'] = float(input("Percentual de completude real da tarefa: "))
                break
            except ValueError: 
                error()

        while True:
            try:
                tarefa['completude_planejada'] = float(input("Percentual de completude planejada da tarefa: "))
                break
            except ValueError:
                error()

        tarefa['responsavel'] = input("Responsável pela tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso.")

    # Função para atualizar tarefa
    def atualizar_tarefa():
        global tarefas
        listar_tarefas()
        while True:
            try:
                num_tarefa = int(input("Digite o número da tarefa que deseja atualizar: ")) - 1
                paragrafo()
                if 0 <= num_tarefa < len(tarefas):
                    tarefa = tarefas[num_tarefa]
                    print("Atualize os campos (deixe em branco para manter os valores atuais):")

                    tarefa['descricao'] = input("Nova descrição da tarefa: ") or tarefa['descricao']

                    while True:
                        try:
                            nova_data_inicial = input("Nova data inicial (dd/mm/aaaa): ")
                            if nova_data_inicial != "":
                                tarefa['data_inicial'] = datetime.strptime(nova_data_inicial, "%d/%m/%Y").date()
                                tarefa['data_inicial'] = tarefa['data_inicial'].strftime("%d/%m/%Y")
                                break
                            else:
                                break
                        except ValueError:
                            error()

                    while True:
                        try:
                            nova_data_final = input("Nova data final (dd/mm/aaaa): ")
                            if nova_data_final != "":
                                tarefa['data_final'] = datetime.strptime(nova_data_final, "%d/%m/%Y").date()
                                tarefa['data_final'] = tarefa['data_final'].strftime("%d/%m/%Y")
                                if tarefa['data_final'] < tarefa['data_inicial']:
                                    print("A data final da nova tarefa não pode ser antes da data inicial, por favor revise sua tarefa")
                                else:
                                    break
                            else:
                                break
                        except ValueError:
                            error()

                    while True:
                        nova_complet_real = input("Novo percentual de completude real (apenas números): ")
                        if nova_complet_real == "":
                                break
                        try:
                            tarefa['completude_real'] = float(nova_complet_real)
                            break
                        except ValueError:
                            error()

                    while True:
                        nova_complet_plan = input("Novo percentual de completude planejada (apenas números): ")
                        if nova_complet_plan == "":
                                break
                        try:
                            tarefa['completude_planejada'] = float(nova_complet_plan)
                            break
                        except ValueError:
                            error()
                                        
                    tarefa['responsavel'] = input(f"Novo responsável ({tarefa['responsavel']}): ") or tarefa['responsavel']

                    plano_atraso = input(f"Insira um  plano caso a tarefa esteja atrasada ou vá atrasar (deixei em branco caso não seja necessário): ")
                    if plano_atraso != "":
                        tarefa['plano'] = plano_atraso

                        
                    while True:
                        try:
                            conclusao_tarefa = input(f"Deseja marcar a tarefa como concluida? 'Sim' ou vazio para continuar: ").capitalize()
                            if conclusao_tarefa == "Sim":
                                tarefa['completude_real'] = tarefa['completude_planejada']
                                tarefa['concluida'] = conclusao_tarefa
                            break
                        except ValueError:
                            error()

                    print("Tarefa atualizada com sucesso.")

                    break
                else:
                    print("Número de tarefa inexistente.")
            except ValueError:
                error()

    # Função para listar tarefas
    def listar_tarefas():
        print("[Lista de tarefas]")
        paragrafo()
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"Tarefa {i}:")
            print(f"Descrição: {tarefa['descricao']}")
            print(f"Data inicial: {tarefa['data_inicial']}")
            print(f"Data final: {tarefa['data_final']}")
            print(f"Completude real: {tarefa['completude_real']:.0f}%")
            print(f"Completude planejada: {tarefa['completude_planejada']:.0f}%")
            print(f"Responsável: {tarefa['responsavel']}")
            data_final = datetime.strptime(tarefa['data_final'], '%d/%m/%Y')
            if data_final < datetime.now() and 'concluida' not in tarefa:
                print('Esta tarefa está atrasada!')
            if 'plano' in tarefa:
                print(f"Plano: {tarefa['plano']}")
            if 'concluida' in tarefa:
                print("Tarefa concluida")
            paragrafo()

    # Função para resumo da operação
    def resumo_operacao():
        print("Resumo da operação:")
        if len(tarefas) == 0:
            print("Nenhuma tarefa realizada")
        else:
            listar_tarefas()

    # Loop principal
    print("Bem vindo ao gerenciador de tarefas de vinheria Agnello.")

    while True:
        escolha = input('''\n O que você deseja fazer hoje?:
        [1] Adicionar tarefa
        [2] Atualizar tarefa
        [3] Listar tarefas
        [4] Encerrar programa\nEscolha uma opção: ''')
        paragrafo()

        match escolha:
            case "1":
                adicionar_tarefa()
            case "2":
                atualizar_tarefa()
            case "3":
                listar_tarefas()
            case "4":
                resumo_operacao()
                break
            case _:
                error()

while True:
    split()
    print('Menu - Guarda-Chuva')
    split()
    print('1 - Loja')
    print('2 - Controle de Estoque')
    print('3 - Controle de Contas')
    print('4 - Controle de Tarefas')
    print('0 - Sair')
    print('')
    try:
        menu_guard = int(input('Insira o número referente ao local que deseja ir: '))
        match menu_guard:

            case 1:
                cp1()

            case 2:
                cp2()

            case 3:
                cp3()

            case 4:
                cp4()
            
            case 0:
                print('')
                break

            case _:
                error()

    except ValueError:
        error()