# Python

comandos_permitidos = ('i', 'a', 'l', 's')
lista_compras = []

while True:

    print('Selecione uma opção: ')
    comando = input('[i]nserir [a]pagar [l]istar [s]air: ')

    if comando not in comandos_permitidos:
        print ('Favor digitar uma chave permitida.')
        continue

    if comando == 'i':
        produto_inserir = input('Favor, digite o produto que gostaria de inserir na lista: ')
        lista_compras.append(produto_inserir)
        continue


    if comando == 'a':
        produto_remover = input('Favor, digite o nome ou o indice do produto que gostaria de remover: ')

        if produto_remover.isdigit():
            idx = int(produto_remover)

            if 0 <= idx < len(lista_compras):
                removido = lista_compras.pop(idx)
                print(f'Produto {removido} removido da posição {idx}.')

            else:
                print('Indice Invalido, favor digitar um indice existente')

        else:
                if produto_remover in lista_compras:
                    lista_compras.remove(produto_remover)
                    print(f'Produto {produto_remover} removido.')

                else:
                    print(f'Produto {produto_remover} não encontrado na lista.')
        continue

    if comando == 'l':

        if not lista_compras:
            print('Lista está vazia, favor inserir produtos.')

        for indice, produto in enumerate(lista_compras):
            print(indice, produto)

    if comando == 's':
        print('Saindo... Até a próxima!')
        break
