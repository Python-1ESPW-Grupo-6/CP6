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
                    if c3 == 0 and d3 == 0 and e3 == 0 and f3 == 0 and g3 == 0:
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
    #Importação da biblioteca sys para funcionamento da função Exit
    import sys

    #Definindo variável de estoque
    Estoque = [[1, "Vinho Agnello Pinot", 5], [2, "Vinho Agnello Chardonay", 10], [3, "Vinho Agnello Merlot", 15],
            [4, "Vinho Agnello Cabernet", 20], [5, "Rotulo 30x40", 150], 
            [6, "Rolha de cortiça", 100], [7, "Garrafa de vidro 750ml", 50],
            [8, "Barril 10 Litros", 10], [9, "Caixa p/ 3 garrafas", 25], [10, "Caixa p/ 1 garrafa", 250]]

    '''
    No estoque estarão disponíveis os seguintes itens, seguidos de seu código numérico:
    0 - Vinho Agnello Pinot
    1 - Vinho Agnello Chardonay
    2 - Vinho Agnello Merlot
    3 - Vinho Agnello Cabernet
    4 - 100/Rotulo 30x40
    5 - 100/Rolha de cortiça
    6 - 100/Garrafa de vidro 750ml
    7 - 10/Barril 10 Litros
    8 - 10/Caixa p/ 3 garrafas
    9 - 100/Caixa p/ 1 garrafa
    '''

    #Definindo variável de histórico do estoque em formato de lista
    historicoEstoque = []

    #Definindo variáveis de itens para a loja
    quantidadeRotulo = 0
    precoFinalRotulos = 0
    quantidadeBarril = 0
    precoFinalBarril = 0
    quantidadeCaixa1 = 0
    precoFinalCaixa1 = 0
    quantidadeCaixa3 = 0
    precoFinalCaixa3 = 0
    quantidadeGarrafa = 0
    precoFinalGarrafa = 0
    quantidadeRolha = 0
    precoFinalRolha = 0
    quantidadeRotulo = 0
    precoFinalRotulos = 0

    '''
    Estarão disponíveis para a compra os seguintes itens (seguidos de sua quantidade por lote, preço unitário e CNPJ de fornecedor):
    #--------------------------
    #100 - Rotulo 30x40 - R$ 5,99 - CNPJ: 53.949.134/0001-10
    #100 - Rolha de cortiça - R$ 7,99 - CNPJ: 71.065.307/0001-19
    #100 - Garrafa de vidro 750ml  - R$ 159,99 - CNPJ: 99.732.744/0001-68
    #10 - Barril 10 Litros - R$ 259,99 - CNPJ: 81.738.182/0001-02
    #10 - Caixa p/ 3 garrafas - R$ 29,99 - CNPJ: 60.206.032/0001-70
    #100 - Caixa p/ 1 garrafa - R$ 159,99 - CNPJ: 65.369.277/0001-31
    #------------------------
    A compra de qualquer um destes itens é imediatamente adicionada ao estoque
    As retiradas do estoque só podem ser feitas em quantidades de 1 a 100 unidades (por retirada)
    '''

    #Mensagem de boas vindas
    print('--------------------------------------------------')
    print('Bem vindo ao hub do funcionario - Vinheria Agnello')
    print('--------------------------------------------------')

    #Menu principal do programa
    while True:
        print('')
        print('----')
        print('Menu')
        print('----')
        print('1 - Estoque')
        print('2 - Compras')
        print('3 - Historico')
        print('0 - Sair')
        print('')

        #Seleção de qual função do menu deseja utilizar
        menuBase = int((input('Qual aba quer acessar?(Número referente ao item): ')))
        match menuBase:

            #Funcionamento da função Estoque
            case 1:      
                while True:
                    print('-------')
                    print('Estoque')
                    print('-------')
                    for x in Estoque:
                        print(' - '.join(str(i) for i in x))
                        pass
                    print('')
                    retirada = input("Deseja retirar ou adicionar manualmente algo do estoque?(Digite 'Retirar', 'Adicionar' ou '0' para sair, se deseja acessar suas compras digite 'Carrinho'): ").lower()
                    match retirada:
                        case "retirar":
                            while True:
                                print('')
                                retirarItemEstoque = int(input("O que deseja retirar do estoque?(Número referente o item!): "))
                                retirarQuantiaEstoque = int(input(f'Quanto deseja retirar do item?: '))
                                if retirarQuantiaEstoque <= 0:
                                    print('----------------')
                                    print('Quantia invalida')
                                    print('----------------')
                                elif (Estoque[retirarItemEstoque - 1][2] - retirarQuantiaEstoque) <0: #testando se o estoque ficará negativo
                                    print('------------------------------------')
                                    print('Itens insuficientes para esta ação!')
                                    print('Voltando para o menu Estoque')
                                    print('------------------------------------')
                                    break
                                else: #retirar do estoque e adicionar ao historicos
                                    Estoque[retirarItemEstoque - 1][2] = Estoque[retirarItemEstoque - 1][2] - retirarQuantiaEstoque
                                    historicoEstoque.append(["Retirado", Estoque[retirarItemEstoque - 1][1], retirarQuantiaEstoque])
                                    break
                        case "adicionar":
                            while True:
                                print('')
                                adicionarItemEstoque = int(input("O que deseja adicionar ao estoque?(Número referente o item!): "))
                                print('')
                                adicionarQuantiaEstoque = int(input("Quanto deseja adicionar deste item?: "))
                                print('')

                                if adicionarQuantiaEstoque <= 0:
                                    print('----------------')
                                    print('Quantia invalida')
                                    print('----------------')
                                else: #retirar do estoque e adicionar ao historicos
                                    Estoque[adicionarItemEstoque - 1][2] = Estoque[adicionarItemEstoque - 1][2] + adicionarQuantiaEstoque
                                    historicoEstoque.append(["Adicionado", Estoque[adicionarItemEstoque - 1][1], adicionarQuantiaEstoque])
                                    break
                        case "0":
                            print('')
                            print('Voltando para o menu')
                            break
                        
                        #Funcionamento da função Carrinho dentro da função estoque
                        case 'carrinho':
                            print('---------')
                            print('Carrinho:')
                            print('---------')
                            if precoFinalRotulos == 0 and precoFinalRolha == 0 and precoFinalBarril == 0 and precoFinalCaixa1 == 0 and precoFinalCaixa3 == 0 and precoFinalGarrafa == 0:
                                print("o seu carrinho esta vazio")
                            else:
                                somaFinal = precoFinalBarril + precoFinalCaixa1 + precoFinalCaixa3 + precoFinalGarrafa + precoFinalRolha + precoFinalRotulos
                                if precoFinalRolha > 0:
                                    print("%d Lote(s) de rolhas com valor de R$ %.2f" %(quantidadeRolha, precoFinalRolha))
                                if precoFinalRotulos > 0:
                                    print("%d Lote(s) de rotulos com valor de R$ %.2f" %(quantidadeRotulo, precoFinalRotulos))
                                if precoFinalGarrafa > 0:
                                    print("%d lote(s) de garrafas com valor de R$ %.2f" %(quantidadeGarrafa,precoFinalGarrafa))
                                if precoFinalBarril > 0:
                                    print("%d lote(s) de barril com valor de R$ %.2f" %(quantidadeBarril, precoFinalBarril))
                                if precoFinalCaixa1 > 0:
                                    print("%d Lote(s) de caixas p/ 1 garrafa com valor de R$ %.2f" %(quantidadeCaixa1, precoFinalCaixa1))
                                if precoFinalCaixa3 > 0:
                                    print("%d Lote(s) de caixas p/ 3 garrafa com valor de R$ %.2f" %(quantidadeCaixa3, precoFinalCaixa3))
                                if somaFinal > 0:
                                    print("Valor final: %.2f" %somaFinal)
                                    while True:
                                        pagamento = str(input("Deseja seguir com o pagamento?(sim/nao)")) #checkout
                                        if pagamento == "sim":
                                            print("Ok vamos prosseguir, para isso precisamos confirmas os dados da empresa")
                                            while True:
                                                Nome = str(input("Nome da empresa:"))
                                                cnpj = str(input("CNPJ:"))
                                                endereco = str(input("Cep:"))
                                                entrega = str(input("Endereço que deve ser entregue:"))
                                                print("Ok agora confira os seus dados e da compra:")
                                                print(Nome)
                                                print(cnpj)
                                                print(endereco)
                                                print(entrega)
                                                print("Valor final: %.2f" %somaFinal)
                                                validacao = str(input("Os dados estao corretos?(Digite 'sim', 'nao' ou '0' para sair): ")).lower()
                                                match validacao:
                                                    case "sim":
                                                        if precoFinalRolha > 0:
                                                            Estoque[5][2] = Estoque[5][2] + quantidadeRolha
                                                            historicoEstoque.append(["Adicionado compras ao estoque", Estoque[5][1], quantidadeRolha])
                                                        if precoFinalRotulos > 0:
                                                            Estoque[4][2] = Estoque[4][2] + quantidadeRotulo
                                                            historicoEstoque.append(["Adicionado compras ao estoque", Estoque[4][1], quantidadeRotulo])
                                                        if precoFinalGarrafa > 0:
                                                            Estoque[6][2] = Estoque[6][2] + quantidadeGarrafa
                                                            historicoEstoque.append(["Adicionado compras ao estoque", Estoque[6][1], quantidadeGarrafa])
                                                        if precoFinalBarril > 0:
                                                            Estoque[7][2] = Estoque[7][2] + quantidadeBarril
                                                            historicoEstoque.append(["Adicionado compras ao estoque", Estoque[7][1], quantidadeBarril])
                                                        if precoFinalCaixa1 > 0:
                                                            Estoque[9][2] = Estoque[9][2] + quantidadeCaixa1
                                                            historicoEstoque.append(["Adicionado compras ao estoque", Estoque[9][1], quantidadeCaixa1])
                                                        if precoFinalCaixa3 > 0:
                                                            Estoque[8][2] = Estoque[8][2] + quantidadeCaixa3
                                                            historicoEstoque.append(["Adicionado compras ao estoque", Estoque[8][1], quantidadeCaixa3])
                                                        quantidadeRotulo = 0   #reset parcial das variaveis caso haja outra compra ou erros
                                                        precoFinalRotulos = 0
                                                        quantidadeBarril = 0
                                                        precoFinalBarril = 0
                                                        quantidadeCaixa1 = 0
                                                        precoFinalCaixa1 = 0
                                                        quantidadeCaixa3 = 0
                                                        precoFinalCaixa3 = 0
                                                        quantidadeGarrafa = 0
                                                        precoFinalGarrafa = 0
                                                        quantidadeRolha = 0
                                                        precoFinalRolha = 0
                                                        quantidadeRotulo = 0
                                                        precoFinalRotulos = 0
                                                        print("Ok,finalizando sua compra")
                                                        print(".")
                                                        print(".")
                                                        print(".")
                                                        print(".")
                                                        print("Tudo pronto! Sua entrega deve chegar nos proximo 6 dias úteis.")
                                                        break
                                                    case "nao":
                                                        print("Voltando para correção dos dados")
                                                        pass
                                                    case "0":
                                                        print('Voltando ao')
                                                        break
                                                    case _:
                                                        print('--------------------------------')
                                                        print('Opção invalida! Tente novamente!')
                                                        print('--------------------------------')
                                                        pass
                                        else:
                                            print('Voltando para o menu')
                                            break
                                        break
                        case _:
                            print("--------------")
                            print("Opção invalida, insira novamente!")
                            print("--------------")
                            pass

            #Funcionamento da função Carrinho
            case 2:
                while True:
                    print('--------------------')
                    print('Menu de compras!')
                    print('--------------------')
                    print('1 - Mostrar catálogo')
                    print('2 - Consultar estoque')
                    print('3 - Consultar carrinho')
                    print('0 - Voltar para o menu')
                    print('')
                    menuCompras = int(input('Oque deseja fazer? (Número referente ao item!): '))
                    print('')
                    match menuCompras:
                        case 1: ##catalogo
                            while True:
                                print('---------')
                                print('Catálogo!')
                                print('---------')
                                print('1 - Rotulo 30x40cm - quantidade do lote = 100 unidades')
                                print('2 - Rolha de cortiça - quantidade do lote = 100 unidades')
                                print('3 - Garrafa de vidro 750ml - quantidade do lote = 100 unidades')
                                print('4 - Barril 10 litros - quantidade do lote = 10 unidades')
                                print('5 - Caixa p/ 3 garrafas - quantidade do lote = 10 unidades')
                                print('6 - Caixa p/ 1 garrafa - quantidade do lote = 100 unidades')
                                print('')
                                selecionarItem = int(input('Qual item deseja comprar? (Número referente o item ou "0" para sair) '))
                                match selecionarItem:
                                    case 1:
                                        while True:
                                            print('')
                                            print('Item Selecionado (Rotulo)')
                                            print('')
                                            print('Fornecedor:')
                                            print('Grafica Neto - CNPJ: 53.949.134/0001-10')
                                            print('Especificações:')
                                            print('Rotulos Personalizados 30x40cm')
                                            print('Lote com 100 unidades')
                                            print('Valor: R$5.99')
                                            print('')
                                            quantidadeRotulo = int(input('Qual a quantidade de lotes deseja comprar? (0 para sair) '))
                                            if quantidadeRotulo < 0:
                                                print('--------------------')
                                                print('Quantidade invalida!')
                                                print('--------------------')
                                                pass
                                            elif quantidadeRotulo == 0:
                                                print('')
                                                print('Voltando para a aba de Compras!')
                                                print('')
                                                break
                                            else:
                                                while True:
                                                    precoFinalRotulos = quantidadeRotulo*5.99
                                                    print('A quantia final vai ser de R$ ',precoFinalRotulos)
                                                    confirmarCompraRotulos = input('Deseja adicionar ao carrinho? (sim/não) ').lower()
                                                    if confirmarCompraRotulos == 'sim':
                                                        print('')
                                                        print('Rotulos adicionados ao carrinho!')
                                                        print('')
                                                        break
                                                    elif confirmarCompraRotulos == 'não':
                                                        print('')
                                                        print('Compra Cancelada!')
                                                        print('')
                                                        print('Voltando para a aba de Compras!')
                                                        print('')
                                                        break
                                                    else:
                                                        print('--------------------------------')
                                                        print('Opção invalida! Tente novamente!')
                                                        print('--------------------------------')
                                                        pass
                                                break
                                    case 2:
                                        while True:
                                            print('')
                                            print('Item Selecionado (Rolha de cortiça)')
                                            print('')
                                            print('Fornecedor:')
                                            print('Marcenaria São João - CNPJ: 71.065.307/0001-19')
                                            print('Rolha de cortiça')
                                            print('Lote com 100 unidades')
                                            print('Valor:')
                                            print('R$7.99')
                                            print('')
                                            quantidadeRolha = int(input('Qual a quantidade de lotes deseja comprar? (0 para sair) '))
                                            if quantidadeRolha < 0:
                                                print('--------------------')
                                                print('Quantidade invalida!')
                                                print('--------------------')
                                                pass
                                            elif quantidadeRolha == 0:
                                                print('')
                                                print('Voltando para a aba de Compras!')
                                                print('')
                                                break
                                            else:
                                                while True:
                                                    precoFinalRolha = quantidadeRolha*7.99
                                                    print('A quantia final vai ser de R$ ',precoFinalRolha)
                                                    confirmarCompraRolha = input('Deseja adicionar ao carrinho? (sim/não) ').lower()
                                                    if confirmarCompraRolha == 'sim':
                                                        print('')
                                                        print('Rolhas adicionados ao carrinho!')
                                                        print('')
                                                        break
                                                    elif confirmarCompraRolha == 'não':
                                                        print('')
                                                        print('Compra Cancelada!')
                                                        print('')
                                                        print('Voltando para a aba de Compras!')
                                                        print('')
                                                        break
                                                    else:
                                                        print('--------------------------------')
                                                        print('Opção invalida! Tente novamente!')
                                                        print('--------------------------------')
                                                        pass
                                                break
                                    case 3:
                                        while True:
                                            print('')
                                            print('Item Selecionado (Garrafa de vidro 750ml)')
                                            print('')
                                            print('Fornecedor:')
                                            print('Vidraçaria Monteiro - CNPJ: 99.732.744/0001-68')
                                            print('Especificações:')
                                            print('Garrafa de vidro 750ml')
                                            print('Lote com 100 unidades')
                                            print('Valor: R$159.99')
                                            print('')
                                            quantidadeGarrafa = int(input('Qual a quantidade de lotes deseja comprar? (0 para sair) '))
                                            if quantidadeGarrafa < 0:
                                                print('--------------------')
                                                print('Quantidade invalida!')
                                                print('--------------------')
                                                pass
                                            elif quantidadeGarrafa == 0:
                                                print('')
                                                print('Voltando para a aba de Compras!')
                                                print('')
                                                break
                                            else:
                                                while True:
                                                    precoFinalGarrafa = quantidadeGarrafa*159.99
                                                    print('A quantia final vai ser de R$ ',precoFinalGarrafa)
                                                    confirmarCompraGarrafa = input('Deseja adicionar ao carrinho? (sim/não) ').lower()
                                                    if confirmarCompraGarrafa == 'sim':
                                                        print('')
                                                        print('Garrafas de vidro adicionadas ao carrinho!')
                                                        print('')
                                                        break
                                                    elif confirmarCompraGarrafa == 'não':
                                                        print('')
                                                        print('Compra Cancelada!')
                                                        print('')
                                                        print('Voltando para a aba de Compras!')
                                                        print('')
                                                        break
                                                    else:
                                                        print('--------------------------------')
                                                        print('Opção invalida! Tente novamente!')
                                                        print('--------------------------------')
                                                        pass
                                                break
                                    case 4:
                                        while True:
                                            print('')
                                            print('Item Selecionado (Barril 10 Litros)')
                                            print('')
                                            print('Fornecedor:')
                                            print('Marcenaria São João - CNPJ: 71.065.307/0001-19')
                                            print('Especificações:')
                                            print('Barril 10 Litros')
                                            print('Lote com 10 unidades')
                                            print('Valor: R$259.99')
                                            print('')
                                            quantidadeBarril = int(input('Qual a quantidade de lotes deseja comprar? (0 para sair) '))
                                            if quantidadeBarril < 0:
                                                print('--------------------')
                                                print('Quantidade invalida!')
                                                print('--------------------')
                                                pass
                                            elif quantidadeBarril == 0:
                                                print('')
                                                print('Voltando para a aba de Compras!')
                                                print('')
                                                break
                                            else:
                                                while True:
                                                    precoFinalBarril = quantidadeBarril*259.99
                                                    print('A quantia final vai ser de R$ ',precoFinalBarril)
                                                    confirmarCompraBarril = input('Deseja adicionar ao carrinho? (sim/não) ').lower()
                                                    if confirmarCompraBarril == 'sim':
                                                        print('')
                                                        print('Barris adicionados ao carrinho!')
                                                        print('')
                                                        break
                                                    elif confirmarCompraBarril == 'não':
                                                        print('')
                                                        print('Compra Cancelada!')
                                                        print('')
                                                        print('Voltando para a aba de Compras!')
                                                        print('')
                                                        break
                                                    else:
                                                        print('--------------------------------')
                                                        print('Opção invalida! Tente novamente!')
                                                        print('--------------------------------')
                                                        pass
                                                break
                                    case 5:
                                        while True:
                                            print('')
                                            print('Item Selecionado (Caixa p/ 3 garrafas)')
                                            print('')
                                            print('Fornecedor:')
                                            print('Embalagens Aparecida - CNPJ: 60.206.032/0001-70')
                                            print('Especificações:')
                                            print('Rotulos Personalizados 30x40cm')
                                            print('Caixa personalizada p/ 3 garrafas')
                                            print('Lote com 100 unidades')
                                            print('Valor:')
                                            print('R$29.99')
                                            print('')
                                            quantidadeCaixa3 = int(input('Qual a quantidade de lotes deseja comprar? (0 para sair) '))
                                            if quantidadeCaixa3 < 0:
                                                print('--------------------')
                                                print('Quantidade invalida!')
                                                print('--------------------')
                                                pass
                                            elif quantidadeCaixa3 == 0:
                                                print('')
                                                print('Voltando para a aba de Compras!')
                                                print('')
                                                break
                                            else:
                                                while True:
                                                    precoFinalCaixa3 = quantidadeCaixa3*29,99
                                                    print('A quantia final vai ser de R$ ',precoFinalCaixa3)
                                                    confirmarCompraCaixa3 = input('Deseja adicionar ao carrinho? (sim/não) ').lower()
                                                    if confirmarCompraCaixa3 == 'sim':
                                                        print('')
                                                        print('Caixas p/ 3 garrafas adicionados ao carrinho!')
                                                        print('')
                                                        break
                                                    elif confirmarCompraCaixa3 == 'não':
                                                        print('')
                                                        print('Compra Cancelada!')
                                                        print('')
                                                        print('Voltando para a aba de Compras!')
                                                        print('')
                                                        break
                                                    else:
                                                        print('--------------------------------')
                                                        print('Opção invalida! Tente novamente!')
                                                        print('--------------------------------')
                                                        pass
                                                break
                                    case 6:
                                        while True:
                                            print('')
                                            print('Item Selecionado (Caixa p/ 1 garrafa)')
                                            print('')
                                            print('Fornecedor:')
                                            print('Embalagens Aparecida - CNPJ: 60.206.032/0001-70')
                                            print('Especificações:')
                                            print('Caixa personalizada p/ 1 garrafa')
                                            print('Lote com 100 unidades')
                                            print('Valor: R$159.99')
                                            print('')
                                            quantidadeCaixa1 = int(input('Qual a quantidade de lotes deseja comprar? (0 para sair) '))
                                            if quantidadeCaixa1 < 0:
                                                print('--------------------')
                                                print('Quantidade invalida!')
                                                print('--------------------')
                                                pass
                                            elif quantidadeCaixa1 == 0:
                                                print('')
                                                print('Voltando para a aba de Compras!')
                                                print('')
                                                break
                                            else:
                                                while True:
                                                    precoFinalCaixa1 = quantidadeCaixa1*159,99
                                                    print('A quantia final vai ser de R$ ',precoFinalCaixa1)
                                                    confirmarCompraCaixa1 = input('Deseja adicionar ao carrinho? (sim/não) ').lower()
                                                    if confirmarCompraCaixa1 == 'sim':
                                                        print('')
                                                        print('Caixas p/ 1 garrafa adicionados ao carrinho!')
                                                        print('')
                                                        break
                                                    elif confirmarCompraCaixa1 == 'não':
                                                        print('')
                                                        print('Compra Cancelada!')
                                                        print('')
                                                        print('Voltando para a aba de Compras!')
                                                        print('')
                                                        break
                                                    else:
                                                        print('--------------------------------')
                                                        print('Opção invalida! Tente novamente!')
                                                        print('--------------------------------')
                                                        pass
                                                break
                                    case 0:
                                        print('---------------------')
                                        print('Voltanddo para o menu')
                                        print('---------------------')
                                        break
                                    case _:
                                        print('--------------------------------')
                                        print('Opção invalida! Tente novamente!')
                                        print('--------------------------------')
                                        pass
                        
                        #Funcionamento da função Estoque dentro do carrinho
                        case 2: 
                            print('-------')
                            print('Estoque')
                            print('-------')
                            for x in Estoque:
                                print(' - '.join(str(i) for i in x))
                                pass
                        #Funcionamento do carrinho = checkout
                        case 3:
                            print('---------')
                            print('Carrinho:')
                            print('---------')
                            if precoFinalRotulos == 0 and precoFinalRolha == 0 and precoFinalBarril == 0 and precoFinalCaixa1 == 0 and precoFinalCaixa3 == 0 and precoFinalGarrafa == 0:
                                print("o seu carrinho esta vazio")
                            else:
                                somaFinal = precoFinalBarril + precoFinalCaixa1 + precoFinalCaixa3 + precoFinalGarrafa + precoFinalRolha + precoFinalRotulos
                                if precoFinalRolha > 0:
                                    print("%d Lote(s) de rolhas com valor de R$ %.2f" %(quantidadeRolha, precoFinalRolha))
                                if precoFinalRotulos > 0:
                                    print("%d Lote(s) de rotulos com valor de R$ %.2f" %(quantidadeRotulo, precoFinalRotulos))
                                if precoFinalGarrafa > 0:
                                    print("%d lote(s) de garrafas com valor de R$ %.2f" %(quantidadeGarrafa,precoFinalGarrafa))
                                if precoFinalBarril > 0:
                                    print("%d lote(s) de barril com valor de R$ %.2f" %(quantidadeBarril, precoFinalBarril))
                                if precoFinalCaixa1 > 0:
                                    print("%d Lote(s) de caixas p/ 1 garrafa com valor de R$ %.2f" %(quantidadeCaixa1, precoFinalCaixa1))
                                if precoFinalCaixa3 > 0:
                                    print("%d Lote(s) de caixas p/ 3 garrafa com valor de R$ %.2f" %(quantidadeCaixa3, precoFinalCaixa3))
                                if somaFinal > 0:
                                    print("Valor final: %.2f" %somaFinal)
                                    while True:
                                        pagamento = str(input("Deseja seguir com o pagamento?(sim/nao)")) #checkout
                                        if pagamento == "sim":
                                            print("Ok vamos prosseguir, para isso precisamos confirmar os dados da empresa")
                                            while True:
                                                Nome = str(input("Nome da empresa:"))
                                                cnpj = str(input("CNPJ:"))
                                                endereco = str(input("Cep:"))
                                                entrega = str(input("Endereço que deve ser entregue:"))
                                                print("Ok agora confira os seus dados e da compra:")
                                                print(Nome)
                                                print(cnpj)
                                                print(endereco)
                                                print(entrega)
                                                print("Valor final: %.2f" %somaFinal)
                                                validacao = str(input("Os dados estao corretos?(Digite 'sim', 'nao' ou '0' para sair): ")).lower()
                                                match validacao:
                                                    case "sim":
                                                        if precoFinalRolha > 0:
                                                            Estoque[5][2] = Estoque[5][2] + (quantidadeRolha*100)
                                                            historicoEstoque.append(["Adicionado compras ao estoque", Estoque[5][1], quantidadeRolha])
                                                        if precoFinalRotulos > 0:
                                                            Estoque[4][2] = Estoque[4][2] + (quantidadeRotulo*100)
                                                            historicoEstoque.append(["Adicionado compras ao estoque", Estoque[4][1], quantidadeRotulo])
                                                        if precoFinalGarrafa > 0:
                                                            Estoque[6][2] = Estoque[6][2] + (quantidadeGarrafa*100)
                                                            historicoEstoque.append(["Adicionado compras ao estoque", Estoque[6][1], quantidadeGarrafa])
                                                        if precoFinalBarril > 0:
                                                            Estoque[7][2] = Estoque[7][2] + (quantidadeBarril*10)
                                                            historicoEstoque.append(["Adicionado compras ao estoque", Estoque[7][1], quantidadeBarril])
                                                        if precoFinalCaixa1 > 0:
                                                            Estoque[9][2] = Estoque[9][2] + (quantidadeCaixa1*100)
                                                            historicoEstoque.append(["Adicionado compras ao estoque", Estoque[9][1], quantidadeCaixa1])
                                                        if precoFinalCaixa3 > 0:
                                                            Estoque[8][2] = Estoque[8][2] + (quantidadeCaixa3*10)
                                                            historicoEstoque.append(["Adicionado compras ao estoque", Estoque[8][1], quantidadeCaixa3])
                                                        quantidadeRotulo = 0   #reset parcial das variaveis caso haja outra compra ou erros
                                                        precoFinalRotulos = 0
                                                        quantidadeBarril = 0
                                                        precoFinalBarril = 0
                                                        quantidadeCaixa1 = 0
                                                        precoFinalCaixa1 = 0
                                                        quantidadeCaixa3 = 0
                                                        precoFinalCaixa3 = 0
                                                        quantidadeGarrafa = 0
                                                        precoFinalGarrafa = 0
                                                        quantidadeRolha = 0
                                                        precoFinalRolha = 0
                                                        quantidadeRotulo = 0
                                                        precoFinalRotulos = 0
                                                        print("Ok,finalizando sua compra")
                                                        print(".")
                                                        print(".")
                                                        print(".")
                                                        print(".")
                                                        print("Tudo pronto! Sua entrega deve chegar nos proximo 6 dias úteis.")
                                                        break
                                                    case "nao":
                                                        print("Voltando para correção dos dados")
                                                        pass
                                                    case "0":
                                                        print('Voltando ao')
                                                        break
                                                    case _:
                                                        print('--------------------------------')
                                                        print('Opção invalida! Tente novamente!')
                                                        print('--------------------------------')
                                                        pass
                                        else:
                                            print('Voltando para o menu')
                                            break
                                        break
                        case 0:
                            print('--------------------')
                            print('Voltando para o menu')
                            print('--------------------')
                            break
                        case _:
                            print('--------------------------------')
                            print('Opção invalida! Tente novamente!')
                            print('--------------------------------')
                            pass
            #Funcionamento da função Histórico
            case 3:
                while True:
                    print('---------')
                    print('Historico')
                    print('---------')
                    if len(historicoEstoque) == 0:
                        print('Nenhum historico registrado, faça alguma movimentação para alterar isto')
                        break
                    else:
                        for w in historicoEstoque:
                            print(' - '.join(str(z) for z in w))
                            print('')
                        print('Fim.')
                        print('')
                        print('--------------------')
                        print('Voltando para o menu')
                        print('--------------------')
                        break
            #Função de fechar o programa
            case 0:
                print('--------------------')
                print('Fechando o aplicativo')
                print('--------------------')
                sys.exit()
            #Função para outras seleções
            case _:
                print('--------------------------------')
                print('Opção invalida! Tente novamente!')
                print('--------------------------------')
                pass

def cp3():
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
                    while True:
                        escolha_relatorio = input('Deseja criar um relatório desse sistema? (sim, não) ')
                        if escolha_relatorio == 'sim':
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
                            print('Relatório criado.')
                            print("Encerrando o programa...")
                            break
                        elif escolha_relatorio == 'não' or 'nao':
                            print("Encerrando o programa...")
                            break
                        else:
                            error()
                        
                    break
                case _:
                    print("\nOpção inválida. Por favor, escolha uma opção das opções listadas.")
        else:
            print("Opção inválida. Por favor, escolha uma as opções listadas.")

def cp4():
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
                    while True:
                        escolha_relatorio = input('Deseja criar um relatório desse sistema? (sim, não) ')
                        if escolha_relatorio == 'sim':
                            arquivo_contas = open('relatorio_contas.txt', 'w')

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
                            print('Relatório criado.')
                            print("Encerrando o programa...")
                            break
                        elif escolha_relatorio == 'não' or 'nao':
                            print("Encerrando o programa...")
                            break
                        else:
                            error()
                    
                    break
                case _:
                    opcao_nao_encontrada()
        except ValueError:
            opcao_nao_encontrada()

def cp5():
    # Inicializar estruturas de dados para armazenar as tarefas
    tarefas = []

    #Função para espaçamento entre retornos do código
    def paragrafo():
        print("")

    # Função para adicionar tarefa
    def adicionar_tarefa():
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
                while True:
                        escolha_relatorio = input('Deseja criar um relatório desse sistema? (sim, não) ')
                        if escolha_relatorio == 'sim':
                            arquivo_tarefa = open('relatório_tarefas.txt', 'w')

                            arquivo_tarefa.write('Lista de Tarefas:\n\n')

                            for i, tarefa in enumerate(tarefas, start=1):
                                arquivo_tarefa.write(f"Tarefa {i}:\n")
                                arquivo_tarefa.write(f"Descrição: {tarefa['descricao']}\n")
                                arquivo_tarefa.write(f"Data inicial: {tarefa['data_inicial']}\n")
                                arquivo_tarefa.write(f"Data final: {tarefa['data_final']}\n")
                                arquivo_tarefa.write(f"Completude real: {tarefa['completude_real']:.0f}%\n")
                                arquivo_tarefa.write(f"Completude planejada: {tarefa['completude_planejada']:.0f}%\n")
                                arquivo_tarefa.write(f"Responsável: {tarefa['responsavel']}\n")
                                data_final = datetime.strptime(tarefa['data_final'], '%d/%m/%Y')
                                if data_final < datetime.now() and 'concluida' not in tarefa:
                                    arquivo_tarefa.write('Esta tarefa está atrasada!\n\n')
                                if 'plano' in tarefa:
                                    arquivo_tarefa.write(f"Plano: {tarefa['plano']}\n\n")
                                if 'concluida' in tarefa:
                                    arquivo_tarefa.write("Tarefa concluida\n\n")

                            arquivo_tarefa.close()
                            print('Relatório criado.')
                            print("Encerrando o programa...")
                            break
                        elif escolha_relatorio == 'não' or 'nao':
                            print("Encerrando o programa...")
                            break
                        else:
                            error()

                break
            case _:
                error()

while True:
    logo()
    split()
    print('Menu - Guarda-Chuva')
    split()
    print('1 - Loja')
    print('2 - Controle de Estoque Produtos')
    print('3 - Controle de Estoque Matéria Prima')
    print('4 - Controle de Contas')
    print('5 - Controle de Tarefas')
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
            
            case 5:
                cp5()

            case 0:
                print('')
                break

            case _:
                error()

    except ValueError:
        error()