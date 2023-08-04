'''
Métodos úteis:
    append - adiciona um item ao final: lista.append('item')
    insert - adiciona um item no indice escolhido
        lista.insert(-indice-, -valor-)
    pop - remove item do final ou do indice escolhido lista.pop()
    del - apaga um indice escolhido del lista[-indice-]
    clear - limpa a lista lista.clear()
    extend - estende a lista 
        lista_a.extend(lista_b)
    + - concatena listas
        lista_c = lista_a + lista_b

    para acessar o último item, utilizar -1 como
    índice pra não adivinhar ou chamar o último indice

'''

'''
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre 
com erros de indices inexistentes na lista.
'''

lista_compras = []

while True:

    escolha = (input('O que deseja fazer? [i]nserir, [a]pagar ou [l]istar? Ainda, para sair digite [sair]')).lower()

    if escolha == 'i':
        adicionar = input('Digite o item que deseja adicionar: ')
        if adicionar in lista_compras:
            print(f'O item {adicionar} já está na lista de compras!')
            continue
        else:
            lista_compras.append(adicionar)
            print(f'{adicionar} adicionado à lista de compras.')
            continue
    elif escolha == 'a':
        apagar = int(input('Digite o índice que quer apagar: '))
        if apagar < len(lista_compras):
            apagado = lista_compras[apagar]
            del lista_compras[apagar]
            print(f'{apagado} removido da lista.')
            continue
        else:
            print(f'O índice {apagar} não existe na lista de compras!')
            print('Confira a lista de compras atual abaixo:')
            i=0
            for nome in lista_compras:
                print(i, nome)
                i += 1
            continue
    elif escolha == 'l':
        i=0
        if lista_compras == []:
            print('A lista de compras está vazia')
            continue
        else:
            for nome in lista_compras:
                print(i, nome)
                i += 1
                continue
    elif escolha == 'sair':
        print('Você encerrou o programa "Lista de Compras"')
        if lista_compras == []:
            print('A sua Lista de Compras está vazia.')
            break
        else:
            print('A sua lista final é:')
            i=0
            for nome in lista_compras:
                print(i, nome)
                i += 1
            break
    else:
        print(f'{escolha} não é uma opção válida')
        continue