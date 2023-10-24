def traco():
    print('-'*30)

def error():
    traco()
    print('Opção inexistente!')
    traco()

while True:
    traco()
    print('Menu - Guarda-Chuva')
    traco()
    print('1 - Loja')
    print('2 - Controle de Estoque')
    print('3 - Controle de Contas')
    print('4 - Controle de Tarefas')
    print('0 - Sair')
    print('')
    try:
        menu_guarda = int(input('Insira o número referente ao local que deseja ir: '))
        match menu_guarda:
            case 1:
                print('')
            case 2:
                print('')
            case 3:
                print('')
            case 4:
                print('')
            case 0:
                print('')
            case _:
                error()
    except ValueError:
        error()